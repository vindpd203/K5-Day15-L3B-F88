# Chi phí khi dùng thật

> Chấm ở rubric R6. Số liệu chép trực tiếp từ `cost/simulate-1-summary.md` sinh bởi `python run.py simulate --rate-from eval/run-2.csv` (không tự nhẩm tay). Lúc phát triển gọi qua gói trả phí theo token thực tế và tính theo bảng giá niêm yết cho lúc vận hành thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu người mua đồ cũ khớp `spec.md` §2 và `docs/de-xuat-do-cu.md` §6 (tổng `share = 1.0`):
  - `mua_thinh_thoang` (`share = 0.6`, `0.5` phiên/tháng, `1` lượt/phiên) — *(tự ước tính)* theo giả thuyết `docs/de-xuat-do-cu.md` §6.
  - `san_mot_mon` (`share = 0.3`, `4` phiên/tháng, `2` lượt/phiên) — tần suất `4` lần/tháng lấy từ phỏng vấn người thật `MUA-01` (kiểm 5 người bán/30 ngày) và `MUA-02` (kiểm 3 người bán/30 ngày) trong `evidence/interviews/`; tỷ lệ `share` và số lượt/phiên là *(tự ước tính)*.
  - `mua_di_ban_lai` (`share = 0.1`, `18` phiên/tháng, `2` lượt/phiên) — *(tự ước tính)* theo khoảng 15–20 lần/tháng ở `docs/de-xuat-do-cu.md` §6.
- **Số người dùng thật** 3 kịch bản: thấp **10.000** · cơ sở **100.000** · cao **500.000** người/tháng. Nguồn: Chợ Tốt công bố hơn 10 triệu người dùng ([Dân Việt 15/06/2022](https://thegioitiepthi.danviet.vn/thi-truong-do-secondhand-51-ty-usd-va-cach-giai-bai-toan-niem-tin-cua-cho-tot-20220615151315565-d13435.html) — số tự công bố năm 2022); tỷ lệ người mua bật tính năng kiểm trước khi cọc ở 3 kịch bản `0,1% · 1% · 5%` là *(tự ước tính)* theo `docs/de-xuat-do-cu.md` §6.
- **Giá** 2 mức model (từ bảng giá mẫu BTC phát / tài liệu giá Google Gemini `https://ai.google.dev/gemini-api/docs/pricing`, xem 27/11/2026):
  - Mức rẻ / vận hành chính: **`gemini-3.1-flash-lite`** (`$0.25 / 1M` token vào · `$1.50 / 1M` token ra)
  - Mức mạnh đối chứng: **`gemini-4-hydrogen`** (`$1.50 / 1M` token vào · `$7.50 / 1M` token ra)
- **Tỉ lệ đạt** dùng để tính: **18/20 (90%)** — lượt `run-2@20261127-212020` (`eval/run-2.csv`, Lượt 2).
- **Đo token trên model `google/gemini-3.1-flash-lite`**, tính giá trên **`gemini-3.1-flash-lite`** (cùng model, không lệch bộ tách token) và **`gemini-4-hydrogen`** (cùng họ Gemini). Tỷ giá tham khảo: `1 USD = 25.400 ₫` *(tự ước tính, 27/11/2026)*.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261127-212619` · **50** phiên (`0/50` lỗi) · seed **42**

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| mua_thinh_thoang | 26 | 1 | 1995 | 573 | 2.0 | 4.0 |
| san_mot_mon | 21 | 2 | 3902 | 1151 | 4.0 | 8.0 |
| mua_di_ban_lai | 3 | 2 | 3879 | 1153 | 4.0 | 8.0 |

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10.000 người) | Chi phí / tháng — cơ sở (100.000 người) | Chi phí / tháng — cao (500.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0020 (≈ 51 ₫) | $0.0022 (≈ 57 ₫) | $0.0015 (≈ 38 ₫) | $85.08 (≈ 2.160.933 ₫) | $850.76 (≈ 21.609.330 ₫) | $4,253.81 (≈ 108.046.649 ₫) | $0.0085 (≈ 216 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0107 (≈ 273 ₫) | $0.0119 (≈ 303 ₫) | $0.0081 (≈ 205 ₫) | $456.04 (≈ 11.583.433 ₫) | $4,560.41 (≈ 115.834.331 ₫) | $22,802.03 (≈ 579.171.655 ₫) | $0.0456 (≈ 1.158 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (`90%`) — **không coi như đạt 100%**.

## 3. So với impact

- **Impact / người / tháng** (`spec.md` §2 & `evidence/summary.md`):
  - **Thời gian tự kiểm:** Theo phỏng vấn `MUA-01` và `MUA-02` (`evidence/interviews/`), người đang tìm mua điện thoại cũ kiểm **3–5 người bán / tháng**, mỗi lần mất **15–25 phút** tự soi trang cá nhân, so giá và nhắn hỏi (≈ **45–125 phút/tháng** ở nhóm đang săn món).
  - **Rủi ro mất tiền cọc:** Tiền cọc bị đòi hoặc mất trong dữ liệu bằng chứng dao động từ **100.000 ₫** (review `C2567`) đến **200.000 ₫** (`MUA-01`), và với điện thoại tầm trung cọc giữ máy thường **200.000–500.000 ₫/vụ** *(tự ước tính theo mặt bằng cọc 5–10%)*.
- **Chi phí / người / tháng** (kịch bản cơ sở 100.000 người, model **`gemini-3.1-flash-lite`**): **`$0.0085` (≈ `216 ₫` / người / tháng)** — tương đương **`57 ₫` cho mỗi task kiểm cọc thành công** (kể cả dùng `gemini-4-hydrogen` cũng chỉ ≈ `1.158 ₫ / người / tháng`).
- **Kết luận một dòng — đáng làm không:** **Rất đáng làm** — với `gemini-3.1-flash-lite`, chi phí vận hành chỉ **~216 ₫/người/tháng** (`~21,6 triệu ₫/tháng` cho 100.000 người dùng), nghĩa là chỉ cần giúp **1 trên ~925 người dùng** tránh mất một khoản cọc 200.000 ₫ mỗi tháng (tỷ lệ ngăn chặn ~0,11%) là giá trị bảo vệ tiền thật cho người mua đã vượt toàn bộ chi phí gọi model, chưa kể hàng chục phút tự kiểm tra tiết kiệm được.

## 4. Độ nhạy & cần gạt tối ưu thêm

- **Chọn tầng model (`gemini-3.1-flash-lite` vs `gemini-4-hydrogen`):** Dùng `gemini-3.1-flash-lite` (đã đạt `18/20 = 90%` ở Lượt 2) giảm **81% chi phí** so với `gemini-4-hydrogen` (`$850.76` so với `$4,560.41`/tháng ở 100.000 người).
- **Chặn sớm bằng luật cứng / ngoài phạm vi trước Bước 4:** Các ca ngoài phạm vi (`tu_choi`) dừng ngay sau Bước 1 chỉ tốn 1 lần gọi model; nếu các ca đã có tín hiệu đỏ rõ rệt từ công cụ (`tk_canh_bao`, `anh_trung`) dùng mẫu cảnh báo cố định thay vì gọi Bước 4 thì tiết kiệm thêm ~35–45% token đầu ra trên nhóm ca lừa rõ.
- **Prompt caching cho `SYSTEM_EXTRACT` và `SYSTEM_DECIDE`:** Phần system prompt cố định chiếm ~40% token đầu vào; bật context caching ở quy mô thật giúp giảm thêm ~20–30% chi phí token vào.
