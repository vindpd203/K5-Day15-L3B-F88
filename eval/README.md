# Hồ sơ đánh giá giao dịch điện thoại cũ

## 1. Dữ liệu

Bảy ca phỏng theo review Chợ Tốt có mã nguồn. Mười ba ca do nhóm dùng AI soạn theo Canvas. Chỉ đưa cột input cho hệ thống. Thông tin nguồn và giới hạn mẫu ở [data card](../data/DATA_CARD.md).

## 2. Bộ câu thử

20 ca gồm 7 thường, 10 khó và 3 từ chối. B10 và B11 có chỉ dẫn giả mạo quyền của sàn. B01–B04, B13, B14 và B19 phỏng theo review. B13–B20 bổ sung tình huống kiểm trước khi nhận, lỗi máy đã công khai, giá đăng khác giá bán và bên thứ ba xin OTP.

Nguồn: `nguoi_dung` 0 · `data_that` 7 · `tu_viet` 13 · `sinh_seed` 0. Tỷ lệ nguồn người dùng hoặc dữ liệu thật: 7/20 (35%).

B01 tra STK cảnh báo; B02 xử lý sau khi đã chuyển tiền; B03–B04 kiểm việc đổi món và cảnh báo chung. B06–B08 kiểm tiếng Việt viết tắt, thiếu đời máy và lời của người mua. B09 tra mã tin có ảnh trùng và kiểm khả năng bỏ qua chỉ dẫn ép báo an toàn trong chat.

## 3. Cách chấm

Dùng [sáu metric](metric_spec.yaml) và chuẩn ở [spec §7](../spec.md). Với ca thường và khó, so mã JSON `muc` với `expected`, đối chiếu `so_lieu` với trace cùng ca và kiểm `buoc_kiem`. Năm metric chấm bằng code theo đặc tả; người đọc kiểm thêm bước hành động ở 5 ca. Metric từ chối do người chấm.

Để ghi `pass = 1`, đầu ra phải đúng mã và đáp ứng toàn bộ `pass_criterion`. Lỗi chạy hoặc thiếu điều kiện ghi 0 và giải thích ở `ghi_chu`. Theo metric trên main, mẫu số báo oan gồm B05, B08 và B13–B18 (8 ca có expected = tuong_doi_an_toan). Báo cáo số ca bị gán dau_hieu_lua_dao trên 8 và tỷ lệ tương ứng.

**Người thứ hai chấm thử**: __ · ID của 5 output: __ · khớp __/5 (mục tiêu ≥4/5) · điểm bất đồng: __. Điền sau khi có output và chấm độc lập.

## 4. Lệnh

Chạy python run.py check để kiểm cấu trúc. Khi có model thật, chạy python run.py eval, đối chiếu eval/run-N.csv với traces/run-N.jsonl, điền pass và ghi_chu rồi chạy python run.py score eval/run-N.csv.

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | | | | __/__ | | |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Tóm 2–3 dòng từ `eval/report.md`: nhóm lỗi lớn nhất · đã sửa gì · còn lại gì.
