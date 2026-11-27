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
| 1 | `run-1@20261127-191256` | `google/gemini-3.1-flash-lite` | Workflow 5 bước + 4 công cụ + luật G10 trên `main` (`30f6a39`) | 9/20 | 45% | Chưa (`muc_dung_nhan` 10/17 = 58,8% < 75%; đạt 0/4 lọt lừa, 0/8 báo oan, 17/17 khớp số liệu) |
| 2 | `run-2@20261127-212020` | `google/gemini-3.1-flash-lite` | Truyền `dau_vao_goc` + quy tắc G10 vào Bước 4, làm rõ `ngoai_pham_vi` cho `da_chuyen_tien` ở Bước 1 | 18/20 | 90% | **Đạt** (`muc_dung_nhan` 17/17 = 100% ≥ 75%; 0/4 lọt lừa, 0/8 báo oan, 17/17 khớp số liệu) |
| 3 | `run-3@20261128-001143` | `openai/gpt-4o-mini` (**model chốt của nhóm**) | Chạy lại nguyên bộ trên code `main` hiện tại (`4437fb8`: prompt Lượt 2 + luật đỏ `da_chuyen_bi_chan`), chỉ đổi model | 11/20 | 55% | **Đạt** (`muc_dung_nhan` 17/17 = 100% ≥ 75%; 0/4 lọt lừa, 0/8 báo oan, 17/17 khớp số liệu) |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau Checkpoint 4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Nhóm lỗi lớn nhất ở Lượt 1 là đứt ngữ cảnh giao dịch gốc và thiếu quy tắc G10 giữa Bước 1 → Bước 4 (làm 6/8 ca kiểm trước trả sau bị hạ về `can_kiem_them`, 4 ca mất chi tiết phụ và B02 bị gán nhầm `ngoai_pham_vi`). Sau một lần cải tiến truyền `dau_vao_goc` + quy tắc G10 vào Bước 4 và làm rõ `da_chuyen_tien` ở Bước 1, Lượt 2 đạt **18/20 (90%)** và vượt chuẩn đạt (`17/17` đúng mã mức, `0` câu tệ đi). **Lượt 3 trên model chốt `gpt-4o-mini`:** vẫn đúng mức 17/17 và đạt chuẩn, nhưng chỉ 11/20 câu đạt `pass_criterion` vì `ly_do` ngắn, thiếu ý phụ (B01, B04, B06, B09, B13–B15, B17, B18). Còn lại 2 câu `kho` ở Lượt 2 (`B04`, `B06`) đúng mức `can_kiem_them` nhưng diễn đạt chưa tách bạch tin đồn chung (`B04`) hoặc chưa bắt hết câu viết tắt không dấu mở sẵn phương án hẹn xem trực tiếp (`B06`).

## 7. Demo CP3

- [Video demo CP3 trên Google Drive](https://drive.google.com/file/d/18xsBOwWMGEnzNl0b0dOIJsQ2e0lH7ka-/view?usp=sharing) quay ở phiên bản terminal trước khi tích hợp đầu ra JSON từ `main`.
- Lượt thử `run-try@20261127-223855` chạy B01–B03 với `openai/gpt-4o-mini` trên bản tích hợp. Cả ba câu có token vào và ra, và trường `muc` trùng nhãn mong đợi. Xem [kết quả CSV](run-try.csv) và [trace](../traces/run-try.jsonl).
- Video quay bản cũ: câu B01 bị từ chối nhầm là ngoài phạm vi, công cụ 0 lần. Cần quay lại trên `main` hiện tại (B01, B05 và một câu ngoài phạm vi) rồi thay link. Lượt `run-try` dùng model khác Lượt 1/2 nên chỉ là bằng chứng nối model, không so với hai lượt eval.
