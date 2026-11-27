# Chi phí khi dùng thật

> Chấm ở rubric R6. Số liệu chép trực tiếp từ `cost/simulate-2-summary.md` sinh bởi `python run.py simulate --rate-from eval/run-3.csv` (không tự nhẩm tay), chạy trên **model chốt của nhóm `openai/gpt-4o-mini`**. Lúc phát triển gọi qua gói trả phí theo token thực tế và tính theo bảng giá niêm yết cho lúc vận hành thật. Lượt mô phỏng cũ trên Gemini giữ ở mục 5.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu người mua đồ cũ khớp `spec.md` §2 và `docs/de-xuat-do-cu.md` §6 (tổng `share = 1.0`):
  - `mua_thinh_thoang` (`share = 0.6`, `0.5` phiên/tháng, `1` lượt/phiên) — *(tự ước tính)* theo giả thuyết `docs/de-xuat-do-cu.md` §6.
  - `san_mot_mon` (`share = 0.3`, `4` phiên/tháng, `2` lượt/phiên) — tần suất `4` lần/tháng lấy từ phỏng vấn người thật `MUA-01` (kiểm 5 người bán/30 ngày) và `MUA-02` (kiểm 3 người bán/30 ngày) trong `evidence/interviews/`; tỷ lệ `share` và số lượt/phiên là *(tự ước tính)*.
  - `mua_di_ban_lai` (`share = 0.1`, `18` phiên/tháng, `2` lượt/phiên) — *(tự ước tính)* theo khoảng 15–20 lần/tháng ở `docs/de-xuat-do-cu.md` §6.
- **Số người dùng thật** 3 kịch bản: thấp **10.000** · cơ sở **100.000** · cao **500.000** người/tháng. Nguồn: Chợ Tốt công bố hơn 10 triệu người dùng ([Dân Việt 15/06/2022](https://thegioitiepthi.danviet.vn/thi-truong-do-secondhand-51-ty-usd-va-cach-giai-bai-toan-niem-tin-cua-cho-tot-20220615151315565-d13435.html) — số tự công bố năm 2022); tỷ lệ người mua bật tính năng kiểm trước khi cọc ở 3 kịch bản `0,1% · 1% · 5%` là *(tự ước tính)* theo `docs/de-xuat-do-cu.md` §6.
- **Giá** 2 mức model (từ bảng giá BTC phát [`further-reading/model-prices.md`](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/main/further-reading/model-prices.md) mục OpenAI, nguồn gốc `https://developers.openai.com/api/docs/pricing`; nhóm xem 28/11/2026):
  - Mức rẻ / **vận hành chính (model chốt)**: **`gpt-4o-mini`** (`$0.15 / 1M` token vào · `$0.60 / 1M` token ra)
  - Mức mạnh đối chứng (tầng Lớn): **`gpt-6.2-sol`** (`$2.00 / 1M` token vào · `$10.00 / 1M` token ra)
- **Tỉ lệ đạt** dùng để tính: **11/20 (55%)** — lượt `run-3@20261128-001143` (`eval/run-3.csv`, Lượt 3 trên model chốt).
- **Đo token trên model `openai/gpt-4o-mini`** (gọi qua OpenRouter), tính giá trên **`gpt-4o-mini`** (cùng model) và **`gpt-6.2-sol`** (cùng hãng OpenAI; bộ tách token có thể lệch). Tỷ giá tham khảo: `1 USD = 25.400 ₫` *(tự ước tính, 27/11/2026)*.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-2.csv` · run ID `simulate-2@20261128-001559` · **50** phiên (`0/50` lỗi) · seed **42**

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| mua_thinh_thoang | 26 | 1 | 1944 | 386 | 2.0 | 4.0 |
| san_mot_mon | 21 | 2 | 3748 | 759 | 4.0 | 7.8 |
| mua_di_ban_lai | 3 | 2 | 3735 | 766 | 4.0 | 8.0 |

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10.000 người) | Chi phí / tháng — cơ sở (100.000 người) | Chi phí / tháng — cao (500.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.00076 (≈ 19 ₫) | $0.0014 (≈ 35 ₫) | $0.00093 (≈ 24 ₫) | $32.14 (≈ 816.378 ₫) | $321.41 (≈ 8.163.780 ₫) | $1,607.04 (≈ 40.818.901 ₫) | $0.0032 (≈ 82 ₫) |
| gpt-6.2-sol (vào 2.0 · ra 10.0 $/1M) | $0.0113 (≈ 286 ₫) | $0.0205 (≈ 521 ₫) | $0.0139 (≈ 352 ₫) | $476.66 (≈ 12.107.239 ₫) | $4,766.63 (≈ 121.072.394 ₫) | $23,833.15 (≈ 605.361.968 ₫) | $0.0477 (≈ 1.211 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (`55%`) — **không coi như đạt 100%**.

## 3. So với impact

- **Impact / người / tháng** (`spec.md` §2 & `evidence/summary.md`):
  - **Thời gian tự kiểm:** Theo phỏng vấn `MUA-01` và `MUA-02` (`evidence/interviews/`), người đang tìm mua điện thoại cũ kiểm **3–5 người bán / tháng**, mỗi lần mất **15–25 phút** tự soi trang cá nhân, so giá và nhắn hỏi (≈ **45–125 phút/tháng** ở nhóm đang săn món).
  - **Rủi ro mất tiền cọc:** Tiền cọc bị đòi hoặc mất trong dữ liệu bằng chứng dao động từ **100.000 ₫** (review `C2567`) đến **200.000 ₫** (`MUA-01`), và với điện thoại tầm trung cọc giữ máy thường **200.000–500.000 ₫/vụ** *(tự ước tính theo mặt bằng cọc 5–10%)*.
- **Chi phí / người / tháng** (kịch bản cơ sở 100.000 người, model chốt **`gpt-4o-mini`**): **`$0.0032` (≈ `82 ₫` / người / tháng)** — tương đương **`35 ₫` cho mỗi task kiểm cọc thành công** (dùng `gpt-6.2-sol` thì ≈ `1.211 ₫ / người / tháng`).
- **Kết luận một dòng — đáng làm không:** **Đáng làm** — với `gpt-4o-mini`, chi phí vận hành chỉ **~82 ₫/người/tháng** (`~8,2 triệu ₫/tháng` cho 100.000 người dùng), nghĩa là chỉ cần giúp **1 trên ~2.450 người dùng** tránh mất một khoản cọc 200.000 ₫ mỗi tháng (~0,04%) là đủ bù toàn bộ chi phí gọi model, chưa kể thời gian tự kiểm. Đổi lại, tỉ lệ câu trả lời đạt đủ tiêu chí chỉ 55% (Lượt 3) so với 90% của Gemini ở Lượt 2 — mức kết luận vẫn đúng 17/17 nhưng lý do kém chi tiết hơn.

## 4. Độ nhạy & cần gạt tối ưu thêm

- **Chọn tầng model (`gpt-4o-mini` vs `gpt-6.2-sol`):** Dùng `gpt-4o-mini` giảm **93% chi phí** so với `gpt-6.2-sol` (`$321.41` so với `$4,766.63`/tháng ở 100.000 người). Chưa đo `gpt-6.2-sol` có tăng tỉ lệ đạt hay không.
- **So với lượt mô phỏng Gemini cũ (`simulate-1`):** `gemini-3.1-flash-lite` tốn `$0.0020`/phiên so với `$0.00076`/phiên của `gpt-4o-mini`, nhưng tỉ lệ đạt 90% so với 55%, nên chi phí / task thành công là `$0.0022` so với `$0.0014` — `gpt-4o-mini` vẫn rẻ hơn ~37% tính trên task thành công.
- **Chặn sớm bằng luật cứng / ngoài phạm vi trước Bước 4:** Các ca ngoài phạm vi (`tu_choi`) dừng ngay sau Bước 1 chỉ tốn 1 lần gọi model; nếu các ca đã có tín hiệu đỏ rõ rệt từ công cụ (`tk_canh_bao`, `anh_trung`) dùng mẫu cảnh báo cố định thay vì gọi Bước 4 thì tiết kiệm thêm ~35–45% token đầu ra trên nhóm ca lừa rõ *(tự ước tính, chưa đo)*.
- **Prompt caching cho `SYSTEM_EXTRACT` và `SYSTEM_DECIDE`:** Phần system prompt cố định chiếm ~40% token đầu vào *(tự ước tính, chưa đo)*; giá token vào đã cache của `gpt-4o-mini` là `$0.075 / 1M`, bằng 1/2 giá thường (`further-reading/model-prices.md`), nên bật caching ở quy mô thật giúp giảm thêm ~20% chi phí token vào *(tự ước tính từ hai số trên)*.

## 5. Lượt mô phỏng trước (giữ để đối chiếu)

`cost/simulate-1.csv` · `simulate-1@20261127-212619` · 50 phiên · token đo trên `google/gemini-3.1-flash-lite`, tỉ lệ đạt 18/20 (90%) từ `eval/run-2.csv`: `gemini-3.1-flash-lite` $0.0022 (≈ 57 ₫) / task thành công, $850.76 / tháng ở 100.000 người; `gemini-4-hydrogen` $0.0119 / task thành công. Chi tiết: `cost/simulate-1-summary.md`.
