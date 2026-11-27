"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối model thật: điền .env (chép từ .env.example), rồi viết nhánh gọi API ở dưới theo docs/connect-model.md
(có ví dụ OpenAI, Claude, model chạy trên máy, và cách nối nhà cung cấp khác). Không dán API key vào file này.
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOW_RAW = False  # đổi thành True để in nguyên phản hồi API khi cần debug trường JSON


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()
API_BASE_URL = (os.environ.get("API_BASE_URL") or "").strip()

URL_OPENAI = "https://api.openai.com/v1/chat/completions"
URL_CLAUDE = "https://api.anthropic.com/v1/messages"
URL_OLLAMA = "http://localhost:11434/api/chat"
URL_GEMINI_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"


def post_json(url, headers, body, timeout=60):
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib)."""
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers),
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


def call_openai(system: str, user: str) -> dict:
    """Gọi OpenAI hoặc API tương thích chuẩn OpenAI (Groq, DeepSeek, OpenRouter qua API_BASE_URL)."""
    url = API_BASE_URL or URL_OPENAI
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(url, {"Authorization": "Bearer " + API_KEY}, {"model": MODEL_NAME, "messages": messages})
    u = data["usage"]
    return {
        "text": data["choices"][0]["message"]["content"] or "",
        "tokens_in": int(u["prompt_tokens"]),
        "tokens_out": int(u["completion_tokens"]),
    }


def call_claude(system: str, user: str) -> dict:
    """Gọi Anthropic Claude Messages API."""
    url = API_BASE_URL or URL_CLAUDE
    data = post_json(
        url,
        {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
        {
            "model": MODEL_NAME,
            "max_tokens": 1024,
            "system": system or "",
            "messages": [{"role": "user", "content": user}],
        },
    )
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    u = data["usage"]
    return {
        "text": text,
        "tokens_in": int(u["input_tokens"]),
        "tokens_out": int(u["output_tokens"]),
    }


def call_gemini(system: str, user: str) -> dict:
    """Gọi Google Gemini REST API (generativelanguage v1beta), không cần cài SDK."""
    model_id = urllib.parse.quote(MODEL_NAME, safe="-._")
    url = API_BASE_URL or (URL_GEMINI_TMPL % model_id)
    body = {"contents": [{"role": "user", "parts": [{"text": user}]}]}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(url, {"x-goog-api-key": API_KEY}, body)
    candidates = data.get("candidates") or []
    if not candidates:
        raise RuntimeError("Gemini không trả về candidates: %s" % json.dumps(data, ensure_ascii=False)[:300])
    parts = (candidates[0].get("content") or {}).get("parts") or []
    # Bỏ các phần thought (nếu model có suy luận riêng), chỉ ghép phần trả lời chính
    text_parts = [p.get("text", "") for p in parts if isinstance(p, dict) and not p.get("thought")]
    text = "".join(text_parts)
    u = data.get("usageMetadata") or {}
    tokens_in = int(u.get("promptTokenCount") or 0)
    cand_tokens = int(u.get("candidatesTokenCount") or 0)
    thought_tokens = int(u.get("thoughtsTokenCount") or 0)
    total_tokens = int(u.get("totalTokenCount") or 0)
    # Hợp đồng yêu cầu tokens_out gồm cả token suy luận nếu API tính riêng
    tokens_out = cand_tokens + thought_tokens
    if tokens_out == 0 and total_tokens > tokens_in:
        tokens_out = total_tokens - tokens_in
    return {"text": text, "tokens_in": tokens_in, "tokens_out": tokens_out}


def call_ollama(system: str, user: str) -> dict:
    """Gọi model chạy trên máy qua Ollama."""
    url = API_BASE_URL or URL_OLLAMA
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(url, {}, {"model": MODEL_NAME, "messages": messages, "stream": False}, timeout=300)
    return {
        "text": (data.get("message") or {}).get("content", ""),
        "tokens_in": int(data.get("prompt_eval_count") or 0),
        "tokens_out": int(data.get("eval_count") or 0),
    }


def _check_config():
    if not MODEL_NAME:
        raise RuntimeError("Thiếu MODEL_NAME trong .env (MODEL_PROVIDER=%s) — xem docs/connect-model.md" % MODEL_PROVIDER)
    if MODEL_PROVIDER != "ollama" and not API_KEY:
        raise RuntimeError("Thiếu API_KEY trong .env (MODEL_PROVIDER=%s) — xem docs/connect-model.md" % MODEL_PROVIDER)


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}

    _check_config()
    if MODEL_PROVIDER == "gemini":
        r = call_gemini(system, user)
    elif MODEL_PROVIDER == "openai":
        r = call_openai(system, user)
    elif MODEL_PROVIDER == "anthropic":
        r = call_claude(system, user)
    elif MODEL_PROVIDER == "ollama":
        r = call_ollama(system, user)
    else:
        raise NotImplementedError(
            "MODEL_PROVIDER=%s chưa được hỗ trợ trong codebase/ai.py "
            "(hỗ trợ: fake, gemini, openai, anthropic, ollama; dùng API_BASE_URL với openai cho Groq/DeepSeek/OpenRouter)"
            % MODEL_PROVIDER
        )
    return {
        "text": r["text"],
        "model": MODEL_NAME,
        "tokens_in": int(r["tokens_in"]),
        "tokens_out": int(r["tokens_out"]),
    }
