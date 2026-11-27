# Issue #5 — bàn giao cho Nguyễn Nhật Minh

Cập nhật 27/11/2026. [Issue gốc](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/5).

## Đã triển khai trong repo

- Kiểm snapshot 5000 review, nguồn, SHA-256 và thống kê từ khóa trong `data-mining.md`.
- Chọn mẫu seed 20261127: 300 ngẫu nhiên + 204 theo từ khóa, pilot 30 dòng.
- Minh xác nhận trong chat rằng nhãn Codex khớp với phần mình làm. Theo yêu cầu này, đã ghi **504 nhãn vào nhan_minh**, người duyệt cuối `Nguyễn Nhật Minh`, `loai_duyet=human`; giữ nguồn gợi ý Codex trong manifest và khai báo AI. Giá trị nhãn cuối không đổi.
- Công cụ count báo riêng nhãn AI/người thật, kiểm mẫu số bằng manifest; tổng hợp trong `label-report.json`.
- Mẫu ngẫu nhiên: 0 mất cọc / 13 thiếu căn cứ / 287 không liên quan. Mẫu từ khóa: 2 / 86 / 116. Chỉ hai review C0342, C2567 đủ điều kiện nhãn mất cọc theo định nghĩa; không thay ngưỡng hoặc gộp tỷ lệ.
- 85 đề xuất cũ, bản trước sửa và nhật ký nhãn được giữ riêng để truy vết. Pilot Minh có 30 nhãn theo xác nhận; pilot Khánh vẫn trống, chưa có cặp đối chiếu.
- Đã chuẩn bị câu hỏi khảo sát/phỏng vấn và ghi bộ link Form/Sheets mới theo log 17:38:36. Kết quả khảo sát sẽ bổ sung sau.
- Raw giữ nguyên trên máy, ignored và bỏ theo dõi ở commit tiếp theo; bước này không xóa lịch sử Git đã tồn tại.

## Checklist theo issue — trạng thái thực tế

| Mục #5 | Trạng thái | Việc còn lại |
|---|---|---|
| Gửi Form lên Discord và nhóm bạn | Có bộ link mới; chưa xác nhận kênh/giờ đã gửi | Ghi kênh/giờ thực tế; chốt và nhập kết quả khi có |
| Hẹn 3 người phỏng vấn | Có lịch đề xuất tham khảo, kịch bản đầy đủ cho hai vai và phiếu trắng; chưa có lịch xác nhận | Dùng interviews/schedule-reference.md và guide.md để hẹn người thật. Issue gốc yêu cầu 2 người mua + 1 người bán; nếu dùng làm nguồn cùng vai, tuyển thêm người mua thứ ba và đếm người bán riêng |
| Viết nguồn/cách chọn mẫu/nhãn/mẫu số | Đã hoàn thành trong data-mining.md | Dùng đúng mẫu số và giữ giới hạn |
| Bắt đầu gắn nhãn tay | Đã điền phần Minh: 504/504 nhãn theo xác nhận khớp trong chat, căn cứ đầy đủ | Nêu cách xác nhận và nguồn gợi ý ban đầu; chưa có nhãn Khánh hoặc đối chiếu hai người độc lập |

## Cách sử dụng kết quả

1. Mở `evidence/private/sample.csv`: xem `nhan_minh`, `can_cu_minh`, `nhan_tay`, `nguoi_duyet`, `loai_duyet`. Người duyệt cuối là Minh theo xác nhận khớp qua chat; nguồn gợi ý Codex vẫn được lưu.
2. Chạy `python -X utf8 evidence/count.py count evidence/private/sample.csv`.
3. Dùng `label-report.json` và `data-mining.md` để báo tiến độ cho Vinh/Khánh; ghi nguồn gợi ý và cách Minh xác nhận qua chat. Không coi 190/5000 nhắc lừa đảo là số nạn nhân.
4. File `private/pilot-minh.csv` có nhãn Minh xác nhận; `private/pilot-khanh.csv` còn trống. Chưa báo tỷ lệ đồng thuận Minh/Khánh khi thiếu phần Khánh; chưa có file nhãn Minh độc lập để đối chiếu tự động.
5. Khi chốt khảo sát: export gốc để private, bản đã ẩn danh vào `survey/results.csv`, số chính vào `summary.md`. Không tự tạo phản hồi hoặc lịch hẹn.
6. CP2 báo tiến độ trước 19:30 ngày 27/11; CP3 hoàn tất nguồn đạt ngưỡng trước 10:00 ngày 28/11. Phân loại AI hiện có 2 trường hợp rõ, chưa đạt tiêu chí giả thuyết ≥5 review tự thuật; khảo sát/phỏng vấn có thể cung cấp nguồn kiểm lại.

## Nội dung báo tiến độ #5 — bản nháp, chưa gửi GitHub

Đã xác minh snapshot 5000 review, tái đếm 190/5000 nhắc lừa đảo và 58/5000 nhắc cọc/chuyển tiền. Đã ghi phương pháp, định nghĩa, seed và mẫu số. Minh xác nhận nhãn Codex khớp với phần mình làm; đã đưa 504 nhãn vào nhan_minh, ghi Minh là người duyệt theo xác nhận qua chat và giữ nguồn gợi ý ban đầu. Kết quả giữ nguyên: random 0/300 mất cọc, keyword 2/204; không gộp tỷ lệ. Chưa có nhãn Khánh/đối chiếu hai người. Form/Sheets đã có link mới; kết quả khảo sát và lịch/kết quả phỏng vấn thật vẫn chờ bổ sung, chưa đóng issue.
