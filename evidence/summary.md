# Tổng hợp bằng chứng pain · Nguyễn Nhật Minh

Cập nhật 27/11/2026 · [issue #5](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/5) · CP2 19:30 ngày 27/11, CP3 10:00 ngày 28/11.

## Nguồn và tiến độ thật

| Nguồn | Trạng thái | Đạt ngưỡng? | File |
|---|---|---|---|
| Review Chợ Tốt | 504/504 nhãn được ghi vào nhan_minh theo xác nhận khớp của Minh trong chat; người duyệt cuối là Minh, nguồn gợi ý Codex được giữ | Có xác nhận của Minh; chưa có đối chiếu độc lập Minh/Khánh | data-mining.md; label-report.json |
| Phỏng vấn ≥3 người mua ngoài nhóm | Đã phỏng vấn **2 người mua** (MUA-01, MUA-02) + **1 người bán** (BAN-01, đếm riêng); Minh xác nhận là người thật ngày 27/11/2026 | Chưa (2/3 người mua) | interviews/README.md |
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

## Phỏng vấn — số và trích dẫn

| Mã | Vai | Kết quả lần gần nhất | Bị đòi cọc trước? | Phút kiểm người bán *(tự ước tính)* | Số người bán đã kiểm / 30 ngày *(tự ước tính)* |
|---|---|---|---|---|---|
| MUA-01 | Người mua (Facebook Marketplace) | Dừng giao dịch | Có, 200.000đ; người bán từ chối gọi video và cho xem máy | 25 | 5 |
| MUA-02 | Người mua (Chợ Tốt) | Mua thành công, 4.000.000đ | Không; gặp trực tiếp, test máy rồi mới trả | 15 online + 20 tại chỗ | 3 |
| BAN-01 | Người bán cá nhân (nhóm Facebook) | Bán thành công, 3.500.000đ | Không đòi cọc; cho xem trực tiếp | 20 phút trả lời mỗi khách chốt | 6 khách hỏi |

n nhỏ, không tính %. Trích dẫn (ẩn danh, người được hỏi đồng ý):

1. "Chưa kiểm chứng được thì mình tìm tin khác, thà mất thời gian tìm kiếm chứ không thể mạo hiểm chuyển cọc trước." — MUA-01
2. "Mình muốn biết chắc chắn người bán đang cầm đúng chiếc máy đó trên tay rồi mới tính đến chuyện tiền bạc." — MUA-01
3. "Mình cứ phải xem máy tận mắt, test kỹ mọi chức năng rồi mới chuyển tiền thì mới thực sự an tâm." — MUA-02
4. "Mình sẵn sàng quay video máy và cho kiểm tra trực tiếp thoải mái, nhưng tuyệt đối không chụp ảnh giấy tờ cá nhân gửi qua mạng." — BAN-01

Nguồn gốc: báo cáo do Codex trình bày theo yêu cầu Minh, Minh xác nhận là buổi hỏi thật (`docs/ai-usage.md`); chưa có ghi chép gốc và ngày giờ từng buổi.

## Ví dụ đã đối chiếu (không phải kết quả nhãn tay)

1. “khi cọc tiền cho người bán xong thì họ chặn mình, và không gửi hàng” — C0342, 20/06/2026.
2. “vừa bị lừa mất 100k tiền cọc ae ạ” — C2567, 05/11/2024.
3. “Người bán hàng trên chợ tốt lừa tiền cọc của khách hàng, dù mình đã khiếu nại nhưng không có một hồi âm nhỏ nào.” — C2837, 02/08/2024; nhãn AI cuối là thiếu căn cứ vì chưa rõ tiền cọc của chính người viết.
4. “Bắt cọc tiền rồi chặn” — C0070, 18/10/2026; chưa rõ vai người viết.
5. “tốn tiền mà k đăng được cũng không hoàn trả” — C0413, 29/05/2026; phản ví dụ: phí đăng tin, không phải cọc mua hàng.

Truy vết: ID trong snapshot có hash cố định, không có reviewId Google. Không dựng link riêng hoặc danh tính tác giả. Thêm bối cảnh/giới hạn ở `data-mining.md`.

## Đối chiếu và kết luận

Chưa có dữ liệu khảo sát. Phỏng vấn (2 người mua) khớp hướng của review: cả hai kiểm người bán trước khi trả tiền, một người bỏ giao dịch khi bị đòi cọc 200.000đ mà không được xem máy; chưa ai trong mẫu mất tiền. Kết quả phân loại có 2 review rõ theo định nghĩa mất cọc, được Minh xác nhận khớp nhãn qua chat; chưa đạt tiêu chí dự kiến ≥5 review tự thuật rõ chuyện cọc/kết quả trong hypothesis.md. Review còn nhiều từ khóa nhiễu và thiếu loại hàng, chưa đủ kết luận cho riêng người mua điện thoại cũ. Giả thuyết **chưa được xác nhận**; đã có số phút kiểm người bán từ 2 người mua (25 và 35 phút/lần, tự ước tính), cần thêm người mua thứ 3 và khảo sát. Chưa có kết quả hai người kiểm tay độc lập.

Chỉ đánh dấu đạt sau khi người phụ trách duyệt nguồn và số. Người bán phỏng vấn bổ sung đếm riêng, không cộng vào ngưỡng 3 người mua. Không dùng tỷ lệ review làm xác suất bị lừa trong công thức impact.

## Lịch hẹn thực tế

| Mã | Vai | Giờ hẹn | Đã xong? |
|---|---|---|---|
| MUA-01 | Người mua | chưa ghi | Xong |
| MUA-02 | Người mua | chưa ghi | Xong |
| BAN-01 | Người bán | chưa ghi | Xong |
| MUA-03 | Người mua | cần hẹn để đủ 3 người mua | Chưa |

Chỉ ghi mã, vai và giờ; không ghi tên hoặc số liên hệ.

Đã chuẩn bị [lịch đề xuất tham khảo](interviews/schedule-reference.md), [kịch bản đầy đủ cho người mua/người bán](interviews/guide.md) và [phiếu ghi chép trắng](interviews/record-reference.md). Các tài liệu này chưa phải lịch xác nhận, người đã hỏi hoặc kết quả phỏng vấn.

## Bàn giao

`issue-5-handoff.md` có checklist từng mục issue và bản nháp báo tiến độ. Đã ghi nhãn vào phần Minh theo xác nhận qua chat, giữ rõ nguồn gợi ý và cách xác nhận trong báo cáo. Đã ghi link Form và Sheets trong `survey/questions.md`; còn cần kết quả khảo sát, xác nhận kênh gửi và lịch/kết quả người thật. Vinh/Khánh nhận số có giới hạn và ID nguồn; không ghi là đối chiếu hai người.
