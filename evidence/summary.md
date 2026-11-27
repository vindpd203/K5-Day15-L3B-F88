# Tổng hợp bằng chứng pain · Nguyễn Nhật Minh

Cập nhật 27/11/2026 · [issue #5](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/5) · CP2 19:30 ngày 27/11, CP3 10:00 ngày 28/11.

## Nguồn và tiến độ thật

| Nguồn | Trạng thái | Đạt ngưỡng? | File |
|---|---|---|---|
| Review Chợ Tốt | 504/504 nhãn được ghi vào nhan_minh theo xác nhận khớp của Minh trong chat; người duyệt cuối là Minh, nguồn gợi ý Codex được giữ | Có xác nhận của Minh; chưa có đối chiếu độc lập Minh/Khánh | data-mining.md; label-report.json |
| Phỏng vấn ≥3 người mua ngoài nhóm | Có câu hỏi/tin hẹn; chưa có lịch hoặc kết quả thật trong repo | Chưa | interviews/guide.md |
| Khảo sát ≥20 người hợp lệ ngoài nhóm | Đã cập nhật bộ link mới theo log 17:38:36; kết quả sẽ bổ sung sau khi chốt khảo sát theo yêu cầu của Minh | Chưa xác nhận | survey/questions.md |

## Số đã kiểm lại

- Snapshot: **5000** review, 29/06/2023–25/11/2026, SHA-256 trong `data-mining.md`.
- Nhãn từ khóa `lua_dao`: **190/5000 (3,80%)**. Năm 2026: **46/770 (5,97%)**. Chưa phải tỷ lệ nạn nhân.
- Nhãn từ khóa `coc_chuyen_tien`: **58/5000 (1,16%)**; nhiều dòng là phí đăng tin/nạp đồng tốt.
- Loại rỗng/trùng nội dung chuẩn hóa: **1384** dòng; còn **3616** nội dung khác nhau.
- Mẫu seed 20261127: **300 random + 204 keyword = 504**. Pilot **30** (15/tầng).
- **504/504 nhãn trong nhan_minh**: Minh xác nhận qua chat rằng nhãn Codex khớp phần mình làm và yêu cầu ghi vào phần của mình. Người duyệt cuối `Nguyễn Nhật Minh`, `loai_duyet=human`. Nguồn gợi ý Codex và 85 đề xuất ban đầu vẫn giữ để truy vết; không đổi giá trị nhãn hoặc kết quả.
- Tầng ngẫu nhiên: **0/300** nhãn `bi_lua_coc`, 13 thiếu căn cứ, 287 không liên quan. Tầng từ khóa: **2/204 (0,98%)** nhãn `bi_lua_coc`, 86 thiếu căn cứ, 116 không liên quan. Hai dòng rõ: C0342, C2567. Không gộp tỷ lệ hai tầng.
- Nhãn Minh: **504**; pilot có nhãn Minh **30/30**. Nhãn Khánh: **0**, số cặp pilot Minh/Khánh **0/30**; không có tỷ lệ đồng thuận hai người. Việc xác nhận dựa trên lời Minh trong chat, chưa có file nhãn riêng của Minh để đối chiếu tự động. Chi tiết: `label-report.json`.

Tái lập: `python -X utf8 evidence/count.py stats evidence/raw-chotot_reviews.csv` và `python -X utf8 evidence/count.py count evidence/private/sample.csv`.

## Ví dụ đã đối chiếu (không phải kết quả nhãn tay)

1. “khi cọc tiền cho người bán xong thì họ chặn mình, và không gửi hàng” — C0342, 20/06/2026.
2. “vừa bị lừa mất 100k tiền cọc ae ạ” — C2567, 05/11/2024.
3. “Người bán hàng trên chợ tốt lừa tiền cọc của khách hàng, dù mình đã khiếu nại nhưng không có một hồi âm nhỏ nào.” — C2837, 02/08/2024; nhãn AI cuối là thiếu căn cứ vì chưa rõ tiền cọc của chính người viết.
4. “Bắt cọc tiền rồi chặn” — C0070, 18/10/2026; chưa rõ vai người viết.
5. “tốn tiền mà k đăng được cũng không hoàn trả” — C0413, 29/05/2026; phản ví dụ: phí đăng tin, không phải cọc mua hàng.

Truy vết: ID trong snapshot có hash cố định, không có reviewId Google. Không dựng link riêng hoặc danh tính tác giả. Thêm bối cảnh/giới hạn ở `data-mining.md`.

## Đối chiếu và kết luận

Chưa có dữ liệu khảo sát/phỏng vấn để đối chiếu. Kết quả phân loại có 2 review rõ theo định nghĩa mất cọc, được Minh xác nhận khớp nhãn qua chat; chưa đạt tiêu chí dự kiến ≥5 review tự thuật rõ chuyện cọc/kết quả trong hypothesis.md. Review còn nhiều từ khóa nhiễu và thiếu loại hàng, chưa đủ kết luận cho riêng người mua điện thoại cũ. Giả thuyết **chưa được xác nhận**; còn thiếu số lần kiểm người bán và phút/lần từ đúng người dùng. Chưa có kết quả hai người kiểm tay độc lập.

Chỉ đánh dấu đạt sau khi người phụ trách duyệt nguồn và số. Người bán phỏng vấn bổ sung đếm riêng, không cộng vào ngưỡng 3 người mua. Không dùng tỷ lệ review làm xác suất bị lừa trong công thức impact.

## Lịch hẹn thực tế

Chưa có lịch được xác nhận. Khi có, chỉ ghi mã P_, vai và giờ; không ghi tên hoặc số liên hệ. Không tự điền lịch dự kiến thành lịch đã hẹn.

Đã chuẩn bị [lịch đề xuất tham khảo](interviews/schedule-reference.md), [kịch bản đầy đủ cho người mua/người bán](interviews/guide.md) và [phiếu ghi chép trắng](interviews/record-reference.md). Các tài liệu này chưa phải lịch xác nhận, người đã hỏi hoặc kết quả phỏng vấn.

## Bàn giao

`issue-5-handoff.md` có checklist từng mục issue và bản nháp báo tiến độ. Đã ghi nhãn vào phần Minh theo xác nhận qua chat, giữ rõ nguồn gợi ý và cách xác nhận trong báo cáo. Đã ghi link Form và Sheets trong `survey/questions.md`; còn cần kết quả khảo sát, xác nhận kênh gửi và lịch/kết quả người thật. Vinh/Khánh nhận số có giới hạn và ID nguồn; không ghi là đối chiếu hai người.
