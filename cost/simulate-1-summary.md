# Tóm tắt mô phỏng simulate-1@20261127-212619

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| mua_thinh_thoang | 26 | 1 | 1995 | 573 | 2.0 | 4.0 |
| san_mot_mon | 21 | 2 | 3902 | 1151 | 4.0 | 8.0 |
| mua_di_ban_lai | 3 | 2 | 3879 | 1153 | 4.0 | 8.0 |

Tỉ lệ đạt dùng để tính: 18/20 (90%) — lượt run-2@20261127-212020

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10.000 người) | Chi phí / tháng — cơ sở (100.000 người) | Chi phí / tháng — cao (500.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0020 (≈ 51 ₫) | $0.0022 (≈ 57 ₫) | $0.0015 (≈ 38 ₫) | $85.08 (≈ 2.160.933 ₫) | $850.76 (≈ 21.609.330 ₫) | $4,253.81 (≈ 108.046.649 ₫) | $0.0085 (≈ 216 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0107 (≈ 273 ₫) | $0.0119 (≈ 303 ₫) | $0.0081 (≈ 205 ₫) | $456.04 (≈ 11.583.433 ₫) | $4,560.41 (≈ 115.834.331 ₫) | $22,802.03 (≈ 579.171.655 ₫) | $0.0456 (≈ 1.158 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.5) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: google/gemini-3.1-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ ((tự ước tính) tỷ giá tham khảo USD/VNĐ ngày 27/11/2026).
