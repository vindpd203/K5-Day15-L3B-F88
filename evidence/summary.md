# Tổng hợp bằng chứng pain · Nguyễn Nhật Minh

Cập nhật 27/11/2026 · [issue #19](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/19), nối tiếp [issue #5](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/5).

## §1. Nguồn và ngưỡng bằng chứng

- [x] **Đào data:** đã có cách chọn mẫu, định nghĩa nhãn, số x/N và %, lệnh đếm lại và ≥5 ví dụ cụ thể. Hồ sơ đạt ngưỡng đào data; kết quả chưa xác nhận giả thuyết riêng về điện thoại cũ.
- [ ] **Phỏng vấn ≥3 người mua ngoài nhóm:** có 2 người mua và 1 người bán; người bán đếm riêng, còn thiếu 1 người mua đúng vai.
- [ ] **Khảo sát ≥20 người đúng đối tượng ngoài nhóm:** có 20 phản hồi người thật ngoài nhóm theo xác nhận đã ghi của Minh; cả 20 còn chờ xác nhận từng tìm mua điện thoại cũ online trong 12 tháng.

| Nguồn | Phạm vi và ngày đối chiếu | Hồ sơ |
|---|---|---|
| Review Chợ Tốt | Snapshot nhóm cung cấp: 5000 review ngày 29/06/2023–25/11/2026; kiểm lại ngày 27/11/2026 | [Nguồn, chọn mẫu và định nghĩa nhãn](data-mining.md), [báo cáo nhãn](label-report.json) |
| Phỏng vấn | MUA-01, MUA-02 và BAN-01; báo cáo ghi Minh xác nhận người thật ngoài nhóm ngày 27/11/2026; chưa ghi ngày giờ từng buổi | [Danh sách phiên](interviews/README.md) |
| Khảo sát | Bản xuất ngày 27/11/2026 từ tab “Câu trả lời biểu mẫu 1”; chưa xác nhận Form đã đóng | [Báo cáo](survey/results-report.md), [đối chiếu bản xuất](survey/import-report.json) |

Nguồn công khai của review: [Google Play VN — Chợ Tốt](https://play.google.com/store/apps/details?id=com.chotot.vn&hl=vi&gl=VN). Ngày 27/11/2026 là ngày kiểm snapshot, không phải ngày xác minh từng giao dịch. File cũ thiếu reviewId Google; truy vết bằng ID cục bộ và SHA-256 trong `data-mining.md`.

## §2. Đếm gì, mẫu số và kết quả

Snapshot có 5000 ID khác nhau. Sau chuẩn hóa NFC, chữ thường và khoảng trắng, loại 1384 nội dung rỗng hoặc trùng, còn 3616 nội dung. Seed **20261127** chọn **300 ngẫu nhiên**, rồi chọn tối đa 500 dòng còn lại có từ khóa; chỉ còn **204** dòng phù hợp nên lấy hết. Hai tầng không trùng ID, tổng **504** dòng; không gộp tỷ lệ hai tầng.

| Đếm gì | x / N | % |
|---|---|---|
| Có nhãn từ khóa `lua_dao` trong snapshot | 190/5000 | 3,80% |
| Có nhãn từ khóa `coc_chuyen_tien` trong snapshot | 58/5000 | 1,16% |
| Đã có nhãn cuối trong mẫu ngẫu nhiên | 300/300 | 100,00% |
| Tự thuật mất cọc trong mẫu ngẫu nhiên | 0/300 | 0,00% |
| Thiếu căn cứ trong mẫu ngẫu nhiên | 13/300 | 4,33% |
| Không liên quan trong mẫu ngẫu nhiên | 287/300 | 95,67% |
| Đã có nhãn cuối trong mẫu từ khóa | 204/204 | 100,00% |
| Tự thuật mất cọc trong mẫu từ khóa | 2/204 | 0,98% |
| Thiếu căn cứ trong mẫu từ khóa | 86/204 | 42,16% |
| Không liên quan trong mẫu từ khóa | 116/204 | 56,86% |

Các nhãn từ khóa có thể chồng lặp; không cộng thành tổng người. Hai review tự thuật mất cọc rõ là **C0342** và **C2567**. Nhãn `nhan_tay` và căn cứ đã có trong mẫu phân tích; snapshot gốc giữ nguyên để bảo toàn hash. Không coi 5000 dòng là đã được đọc và gắn nhãn cuối.

Minh đã xác nhận qua chat rằng 504 nhãn khớp phần mình làm. Nguồn gợi ý ban đầu và cách xác nhận giữ nguyên trong `label-report.json` và manifest của mẫu. Chưa có file nhãn độc lập của Minh để đối chiếu; Khánh chưa gắn nhãn, pilot có **0/30 cặp** đối chiếu. Không báo tỷ lệ đồng thuận hai người hoặc coi đây là xác minh giao dịch.

Đếm lại trên bản làm việc riêng, không ghi đè dữ liệu:

```powershell
python -X utf8 evidence/count.py stats evidence/raw-chotot_reviews.csv
python -X utf8 evidence/count.py count evidence/private/sample.csv
```

Bản nhãn công khai và lệnh đếm tương ứng nằm trong [hướng dẫn dữ liệu](README.md). File gốc và mẫu đầy đủ không đưa vào Git.

Khảo sát: **20** phản hồi có nội dung, **1** dòng chỉ có lỗi công thức được bỏ khỏi số phản hồi; **5** chọn “Điện thoại, máy tính bảng”, **9** chọn món khác, **6** không trả lời món gần nhất. Về yêu cầu chuyển trước: **5 Có · 6 Không · 3 Không nhớ · 6 không trả lời**. Có **12** phản hồi mang lựa chọn cần hỏi lại. Chưa có người được xác nhận đủ tiêu chí lát cắt; không dùng 20 phản hồi để báo đạt ngưỡng khảo sát đúng đối tượng. Chi tiết ánh xạ và dữ liệu thiếu ở [báo cáo khảo sát](survey/results-report.md). Bản xuất từng phản hồi giữ tại máy người phụ trách, không kèm PR này.

## §3. Trích dẫn và ví dụ nguyên văn

### Review

Năm đoạn dưới đã đối chiếu trực tiếp với snapshot ngày 27/11/2026. Mỗi đoạn ≤2 câu, bỏ tên người viết; ID và ngày nối với nguồn Google Play nêu ở §1. Các ví dụ gồm cả trường hợp thiếu căn cứ và phản ví dụ, không phải 5 vụ mất cọc đã xác minh.

| ID · ngày review | Trích nguyên văn | Diễn giải theo định nghĩa nhãn |
|---|---|---|
| C0342 · 20/06/2026 | “khi cọc tiền cho người bán xong thì họ chặn mình, và không gửi hàng” | Tự thuật chuyển cọc rồi bị chặn/không hàng; chưa biết loại món |
| C2567 · 05/11/2024 | “vừa bị lừa mất 100k tiền cọc ae ạ” | Tự thuật mất cọc; chưa xác minh giao dịch |
| C2837 · 02/08/2024 | “Người bán hàng trên chợ tốt lừa tiền cọc của khách hàng, dù mình đã khiếu nại nhưng không có một hồi âm nhỏ nào.” | Thiếu căn cứ tiền cọc là của chính người viết |
| C0070 · 18/10/2026 | “Bắt cọc tiền rồi chặn” | Chưa rõ vai người viết và giao dịch cụ thể |
| C0413 · 29/05/2026 | “tốn tiền mà k đăng được cũng không hoàn trả” | Phản ví dụ: phí đăng tin, không phải mất cọc mua hàng |

### Phỏng vấn

| Mã và nguồn | Kết quả được kể | Thời gian kiểm *(tự ước tính)* |
|---|---|---|
| [MUA-01](interviews/MUA-01.md) | Bỏ giao dịch khi bị đòi cọc 200.000đ và không được xem máy; chưa chuyển tiền | 25 phút; 5 người bán đã kiểm trong 30 ngày |
| [MUA-02](interviews/MUA-02.md) | Mua 4.000.000đ, xem và thử máy trước khi trả; không bị đòi cọc | 15 phút online + 20 phút tại chỗ; 3 người bán đã kiểm trong 30 ngày |
| [BAN-01](interviews/BAN-01.md) | Bán 3.500.000đ, không đòi cọc; là góc nhìn người bán, đếm riêng | 20 phút trả lời mỗi khách chốt; 6 khách hỏi |

Các báo cáo ghi đồng ý trích dẫn ẩn danh:

- “Chưa kiểm chứng được thì mình tìm tin khác, thà mất thời gian tìm kiếm chứ không thể mạo hiểm chuyển cọc trước.” — [MUA-01, §4](interviews/MUA-01.md#4-trích-dẫn-nguyên-văn).
- “Mình muốn biết chắc chắn người bán đang cầm đúng chiếc máy đó trên tay rồi mới tính đến chuyện tiền bạc.” — [MUA-01, §4](interviews/MUA-01.md#4-trích-dẫn-nguyên-văn).
- “Mình cứ phải xem máy tận mắt, test kỹ mọi chức năng rồi mới chuyển tiền thì mới thực sự an tâm.” — [MUA-02, §4](interviews/MUA-02.md#4-trích-dẫn-nguyên-văn).
- “Mình sẵn sàng quay video máy và cho kiểm tra trực tiếp thoải mái, nhưng tuyệt đối không chụp ảnh giấy tờ cá nhân gửi qua mạng.” — [BAN-01, §4](interviews/BAN-01.md#4-trích-dẫn-nguyên-văn).

Mẫu phỏng vấn nhỏ, không tính %. Chưa có ghi chép gốc và ngày giờ từng buổi trong repo.

## §4. Kết luận giả thuyết và giới hạn

**Phải đổi mức khẳng định:** hiện chỉ có bằng chứng ban đầu rằng người mua cần kiểm chứng người bán trước khi chuyển tiền và có thể bỏ giao dịch khi thiếu căn cứ. Chưa xác nhận mức phổ biến hoặc thiệt hại riêng cho người mua điện thoại cũ. Giữ nguyên các ngưỡng đã ghi trong [giả thuyết](hypothesis.md).

Hai review tự thuật mất cọc rõ chưa đạt tiêu chí dự kiến ≥5; hai người mua được phỏng vấn chưa đủ mẫu ≥3; khảo sát chưa sàng lọc đủ đối tượng. Không kết luận giả thuyết “đúng” hoặc “sai” từ các số này. Đủ hồ sơ đào data không đồng nghĩa đủ bằng chứng để suy rộng giả thuyết.

Review là lời kể chưa xác minh, thiên về người chủ động đánh giá, gồm nhiều vai và loại hàng. Mẫu từ khóa có nhiễu, loại trùng làm thay đổi trọng số. Tỷ lệ trong review không phải xác suất một người mua bị lừa; **0/300 không chứng minh không có lừa đảo**. Không dùng tỷ lệ review cho công thức impact hoặc coi tiền được yêu cầu chuyển trước là tiền đã mất.

## §5. Bàn giao CP3 và việc còn thiếu

Link hồ sơ để người phụ trách nộp CP3: [evidence/summary.md](https://github.com/vindpd203/K5-Day15-L3B-F88/blob/main/evidence/summary.md) (bản trên `main`, PR #33 đã hợp nhất). Chưa có link form CP3 hoặc xác nhận đã nộp form.

- Bổ sung ngày giờ và ghi chép gốc của các buổi phỏng vấn; hỏi thêm ít nhất 1 người mua đúng tiêu chí.
- Xác nhận loại hàng và thời điểm tìm mua của 20 người khảo sát; hỏi lại 12 phản hồi có lựa chọn cần làm rõ, tuyển thêm nếu chưa đủ người phù hợp.
- Người phụ trách nộp link hồ sơ trong form CP3; mục này chưa hoàn tất.
- [Issue #29](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/29) cần phiên dùng thử sản phẩm riêng; không dùng phỏng vấn pain làm kết quả dùng thử.
