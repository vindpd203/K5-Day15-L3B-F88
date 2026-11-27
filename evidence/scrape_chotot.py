"""Cào N review Google Play VN mới nhất (mọi mức sao) của app Chợ Tốt, gắn nhãn thô bằng từ khoá.
Chạy: python -X utf8 evidence/scrape_chotot.py [N, mặc định 1000]
Ra: evidence/raw-chotot_reviews.csv (id, date, score, content, labels, nhan_tay) — KHÔNG có tên người viết.
Không commit nguyên file lên repo công khai (luật: trích tối đa 2 câu / review).
shortcut: nhãn từ khoá chỉ để lọc nhanh; bằng chứng nộp phải gắn nhãn tay theo định nghĩa trong evidence/data-mining.md.
"""
import csv, os, sys
from collections import Counter
from google_play_scraper import reviews, Sort

APP_ID = "com.chotot.vn"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw-chotot_reviews.csv")

LABELS = {
    "lua_dao": ["lừa đảo", "lừa", "scam", "giả mạo", "mạo danh", "gian lận", "bịp"],
    "coc_chuyen_tien": ["cọc", "chuyển khoản", "chuyển tiền", "mất tiền", "ck trước"],
    "tin_ao_sai_mo_ta": ["tin ảo", "ảo", "treo đầu dê", "không đúng", "không giống", "hàng giả", "giá ảo", "câu khách"],
    "nguoi_ban_khong_tin": ["người bán", "đánh giá người bán", "uy tín", "xác thực", "danh tính"],
    "khoa_tai_khoan": ["khóa", "khoá", "bị chặn", "cấm"],
}

if os.path.exists(OUT):
    raise SystemExit("Đã có snapshot raw. Giữ nguyên file gốc; đổi OUT trước khi lấy snapshot mới.")
rs, _ = reviews(APP_ID, lang="vi", country="vn", sort=Sort.NEWEST, count=N)
rows = []
for i, r in enumerate(rs, 1):
    text = (r["content"] or "").lower()
    rows.append({"id": f"C{i:04d}", "date": r["at"].date(), "score": r["score"], "content": r["content"],
                 "labels": "|".join(k for k, kws in LABELS.items() if any(w in text for w in kws)), "nhan_tay": ""})

with open(OUT, "x", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["id", "date", "score", "content", "labels", "nhan_tay"])
    w.writeheader(); w.writerows(rows)

n = len(rows)
d = [r["date"] for r in rows]
c = Counter(l for r in rows for l in r["labels"].split("|") if l)
if not n:
    raise SystemExit("Không lấy được review; không công bố tỷ lệ.")
print(f"N={n}  {min(d)} → {max(d)}  1-2 sao={sum(r['score'] <= 2 for r in rows)}  → {OUT}")
for k in LABELS:
    print(f"  {k}: {c[k]}/{n} ({c[k] / n:.1%})")
