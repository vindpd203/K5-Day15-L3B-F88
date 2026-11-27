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
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Minh họa cách điền báo cáo phỏng vấn | Codex | Theo yêu cầu Minh, viết 3 tình huống AI giả lập trong `docs/examples/interviews/`, gồm 2 vai mua và 1 vai bán; câu trả lời, lời thoại và số tự ước tính đều ghi rõ là minh họa | Chưa có ghi nhận người thật rà soát; không có phiên phỏng vấn, không đưa vào bằng chứng hoặc kết quả khảo sát | Nguyễn Nhật Minh |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
