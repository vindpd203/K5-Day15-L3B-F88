# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | | | | |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, phân loại) | Codex | Viết count.py, kiểm snapshot 5000 review, chọn mẫu 504/pilot 30 và gợi ý nhãn; giữ lịch sử gợi ý | Minh xác nhận trong chat rằng nhãn khớp phần mình làm; ghi 504 nhãn vào nhan_minh, người duyệt cuối Nguyễn Nhật Minh. Cách xác nhận và nguồn gợi ý Codex giữ trong manifest; chưa có file nhãn Minh riêng hoặc đối chiếu với Khánh. Kết quả giữ nguyên 0/300 random, 2/204 keyword | Nguyễn Nhật Minh |
| Rà câu hỏi phỏng vấn / khảo sát | Codex | Soạn 7 nhóm câu khảo sát; lịch đề xuất tham khảo, kịch bản người mua/người bán và phiếu ghi chép trắng | Minh đã tạo Form; lịch/câu hỏi phỏng vấn chỉ là tham khảo. Chưa có lịch được xác nhận hoặc câu trả lời người thật trong repo | Nguyễn Nhật Minh |
| Viết câu thử và tiêu chí đánh giá | Codex | Soạn 12 tình huống, gồm 4 ca viết lại từ trích review trong đề xuất, dự thảo cách chấm và chuẩn đạt | Chờ rà nguồn, đáp án và ngưỡng trước CP2 | Khánh; Vinh cùng duyệt chuẩn đạt |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử và tiêu chí đánh giá | Codex | Soạn thêm B13–B20 cho CP3 (3 ca phỏng theo review có mã, 5 ca tự viết). Ở CP2 soạn 12 tình huống, gồm 4 ca viết lại từ trích review trong đề xuất, dự thảo cách chấm và chuẩn đạt | Chờ rà nguồn, đáp án và ngưỡng trước CP2 | Khánh; Vinh cùng duyệt chuẩn đạt |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Trình bày báo cáo phỏng vấn | Codex | Theo yêu cầu Minh, trình bày 3 báo cáo phỏng vấn (2 người mua, 1 người bán), nay ở `evidence/interviews/`. Ban đầu ghi là minh họa; ngày 27/11/2026 Minh xác nhận với nhóm đây là phỏng vấn người thật | Minh xác nhận nội dung khớp buổi hỏi; chưa có ghi chép gốc và ngày giờ từng buổi trong repo | Nguyễn Nhật Minh |
| Chấm cột `pass` bằng LLM (nếu có) | Coding agent + script Python | Đối chiếu tự động `so_lieu` với `traces/run-1.jsonl` và gợi ý nháp cột `pass`, `ghi_chu` theo `pass_criterion` cho Lượt 1 | Khánh kiểm tra thủ công lại 20/20 câu thử trước khi chốt | Khánh |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
