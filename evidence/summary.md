# Tổng hợp bằng chứng pain · Nguyễn Nhật Minh

Cập nhật 27/11/2026 · [issue #5](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/5) · CP2 19:30 ngày 27/11, CP3 10:00 ngày 28/11.

## Nguồn và tiến độ thật

| Nguồn | Trạng thái | Đạt ngưỡng? | File |
|---|---|---|---|
| Review Chợ Tốt | Codex đã phân loại 504/504 dòng, căn cứ đầy đủ và loai_duyet=ai; chưa có kiểm tay của người thật | Hoàn thành phân loại AI; chưa xác nhận đạt yêu cầu gắn nhãn tay | data-mining.md; label-report.json |
| Phỏng vấn ≥3 người mua ngoài nhóm | Có câu hỏi/tin hẹn; chưa có lịch hoặc kết quả thật trong repo | Chưa | interviews/guide.md |
| Khảo sát ≥20 người hợp lệ ngoài nhóm | Đã cập nhật bộ link mới theo log 17:38:36; kết quả sẽ bổ sung sau khi chốt khảo sát theo yêu cầu của Minh | Chưa xác nhận | survey/questions.md |

## Số đã kiểm lại

- Snapshot: **5000** review, 29/06/2023–25/11/2026, SHA-256 trong `data-mining.md`.
- Nhãn từ khóa `lua_dao`: **190/5000 (3,80%)**. Năm 2026: **46/770 (5,97%)**. Chưa phải tỷ lệ nạn nhân.
- Nhãn từ khóa `coc_chuyen_tien`: **58/5000 (1,16%)**; nhiều dòng là phí đăng tin/nạp đồng tốt.
- Loại rỗng/trùng nội dung chuẩn hóa: **1384** dòng; còn **3616** nội dung khác nhau.
- Mẫu seed 20261127: **300 random + 204 keyword = 504**. Pilot **30** (15/tầng).
- **504/504 nhãn cuối do Codex (AI)** theo yêu cầu Minh; `nguoi_duyet=Codex`, `loai_duyet=ai`. 85 đề xuất ban đầu giữ làm lịch sử. Không khai là Minh/Khánh đã chấm.
- Tầng ngẫu nhiên: **0/300** nhãn `bi_lua_coc`, 13 thiếu căn cứ, 287 không liên quan. Tầng từ khóa: **2/204 (0,98%)** nhãn `bi_lua_coc`, 86 thiếu căn cứ, 116 không liên quan. Hai dòng rõ: C0342, C2567. Không gộp tỷ lệ hai tầng.
- **0 nhãn của người thật**, chưa có cặp pilot Minh/Khánh; không có số đồng thuận giữa hai người. Chi tiết tổng hợp: `label-report.json`.

Tái lập: `python -X utf8 evidence/count.py stats evidence/raw-chotot_reviews.csv` và `python -X utf8 evidence/count.py count evidence/private/sample.csv`.

## Ví dụ đã đối chiếu (không phải kết quả nhãn tay)

1. “khi cọc tiền cho người bán xong thì họ chặn mình, và không gửi hàng” — C0342, 20/06/2026.
2. “vừa bị lừa mất 100k tiền cọc ae ạ” — C2567, 05/11/2024.
3. “Người bán hàng trên chợ tốt lừa tiền cọc của khách hàng, dù mình đã khiếu nại nhưng không có một hồi âm nhỏ nào.” — C2837, 02/08/2024; nhãn AI cuối là thiếu căn cứ vì chưa rõ tiền cọc của chính người viết.
4. “Bắt cọc tiền rồi chặn” — C0070, 18/10/2026; chưa rõ vai người viết.
5. “tốn tiền mà k đăng được cũng không hoàn trả” — C0413, 29/05/2026; phản ví dụ: phí đăng tin, không phải cọc mua hàng.

Truy vết: ID trong snapshot có hash cố định, không có reviewId Google. Không dựng link riêng hoặc danh tính tác giả. Thêm bối cảnh/giới hạn ở `data-mining.md`.

## Đối chiếu và kết luận

Chưa có dữ liệu khảo sát/phỏng vấn để đối chiếu. AI tìm thấy 2 review rõ theo định nghĩa mất cọc, chưa đạt tiêu chí dự kiến ≥5 review tự thuật rõ chuyện cọc/kết quả trong hypothesis.md. Review còn nhiều từ khóa nhiễu và thiếu loại hàng, chưa đủ kết luận cho riêng người mua điện thoại cũ. Giả thuyết **chưa được xác nhận**; còn thiếu số lần kiểm người bán và phút/lần từ đúng người dùng. Không coi phân loại AI là kết quả hai người kiểm tay.

Chỉ đánh dấu đạt sau khi người phụ trách duyệt nguồn và số. Người bán phỏng vấn bổ sung đếm riêng, không cộng vào ngưỡng 3 người mua. Không dùng tỷ lệ review làm xác suất bị lừa trong công thức impact.

## Lịch hẹn thực tế

Chưa có lịch được xác nhận. Khi có, chỉ ghi mã P_, vai và giờ; không ghi tên hoặc số liên hệ. Không tự điền lịch dự kiến thành lịch đã hẹn.

Đã chuẩn bị [lịch đề xuất tham khảo](interviews/schedule-reference.md), [kịch bản đầy đủ cho người mua/người bán](interviews/guide.md) và [phiếu ghi chép trắng](interviews/record-reference.md). Các tài liệu này chưa phải lịch xác nhận, người đã hỏi hoặc kết quả phỏng vấn.

## Bàn giao

`issue-5-handoff.md` có checklist từng mục issue và bản nháp báo tiến độ. Đã hoàn thành phần điền nhãn bởi Codex theo yêu cầu Minh; giữ rõ nguồn AI trong báo cáo. Đã ghi link Form và Sheets trong `survey/questions.md`; còn cần kết quả khảo sát, xác nhận kênh gửi và lịch/kết quả người thật. Vinh/Khánh nhận số có giới hạn và ID nguồn, không ghi là kết quả kiểm tay.
