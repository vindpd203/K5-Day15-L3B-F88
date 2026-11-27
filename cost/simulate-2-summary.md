# Tóm tắt mô phỏng simulate-2@20261128-001559

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| mua_thinh_thoang | 26 | 1 | 1944 | 386 | 2.0 | 4.0 |
| san_mot_mon | 21 | 2 | 3748 | 759 | 4.0 | 7.8 |
| mua_di_ban_lai | 3 | 2 | 3735 | 766 | 4.0 | 8.0 |

Tỉ lệ đạt dùng để tính: 11/20 (55%) — lượt run-3@20261128-001143

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-3.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10.000 người) | Chi phí / tháng — cơ sở (100.000 người) | Chi phí / tháng — cao (500.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.00076 (≈ 19 ₫) | $0.0014 (≈ 35 ₫) | $0.00093 (≈ 24 ₫) | $32.14 (≈ 816.378 ₫) | $321.41 (≈ 8.163.780 ₫) | $1,607.04 (≈ 40.818.901 ₫) | $0.0032 (≈ 82 ₫) |
| gpt-6.2-sol (vào 2.0 · ra 10.0 $/1M) | $0.0113 (≈ 286 ₫) | $0.0205 (≈ 521 ₫) | $0.0139 (≈ 352 ₫) | $476.66 (≈ 12.107.239 ₫) | $4,766.63 (≈ 121.072.394 ₫) | $23,833.15 (≈ 605.361.968 ₫) | $0.0477 (≈ 1.211 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.5) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: openai/gpt-4o-mini. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ ((tự ước tính) tỷ giá tham khảo USD/VNĐ ngày 27/11/2026).
