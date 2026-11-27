# Dữ liệu đánh giá giao dịch điện thoại cũ

Bản cập nhật benchmark CP3, ngày 27/11/2026.

| Nguồn | Cách dùng và giới hạn |
|---|---|
| Trích review Chợ Tốt trong [đề xuất §1](../docs/de-xuat-do-cu.md) | Đề xuất mô tả 5.000 review Google Play thu ngày 27/11. Bản này sử dụng bốn trích đoạn đã bỏ tên có mã C0070, C0342, C0005, C0124. Review là lời kể của người viết. Không suy rộng tỷ lệ mất cọc từ số lượt khớp từ khóa. |
| [Benchmark CP2](../eval/benchmark.csv) | 12 ca tiếng Việt. B01–B04 phỏng theo bốn review tương ứng ở trên. Điện thoại, điều kiện giao dịch và hội thoại được dựng cho bài đánh giá; C0005 gốc nói về xe, C0124 là nhận xét chung. B05–B12 do AI soạn theo Canvas và đề xuất để Khánh duyệt. Toàn bộ đầu vào là tình huống viết lại, không chứa danh tính người bán. Soạn trực tiếp, không dùng lấy mẫu ngẫu nhiên hay seed. Số ca đã được thành viên nhóm rà tay chưa ghi nhận. |
| Giá tham chiếu · synthetic | Dự kiến khoảng 40 mục theo đời và tình trạng, giá ước tính để kiểm phép so giá. |
| Tin đăng · synthetic | Dự kiến khoảng 60 tin để tra mã tin và trùng ảnh trong Chợ Mẫu. |
| Người bán · synthetic | Dự kiến khoảng 40 hồ sơ để tra tuổi tài khoản, số tin và đánh giá. |
| Tài khoản cảnh báo · synthetic | Dự kiến khoảng 15 mã giả để kiểm luật chặn. Chỉ có ý nghĩa trong Chợ Mẫu. |
| Chat · synthetic | Dự kiến khoảng 30 đoạn hội thoại lừa, thật và mơ hồ. Dùng mã và hội thoại hư cấu. |

Năm tập Chợ Mẫu đang chờ bản dữ liệu từ Hùng. Seed thực tế, số dòng, phiên bản và số dòng đã kiểm tay chưa xác định. B01 dùng STK cảnh báo dựng sẵn và B09 dùng TD002 (trùng mã ảnh IMG-001 với TD001 của người bán khác) từ bộ dự phòng trong codebase/tools.py tại commit 1444053 của PR #13. Kiểm lại hai ca khi issue #6 có bộ CSV chính thức. Khi có dữ liệu, đối chiếu đời máy, tình trạng, mã tin và mã tài khoản cảnh báo với benchmark trước lượt chạy.

### Kiểm tra B01 và B09 cho CP2

Ngày 27/11, chạy hai input của benchmark qua `answer()` với model giả trên commit `3cddf2f`. B01 gọi `kiem_tai_khoan`, trả `canh_bao=True` và 5 lượt báo cáo. B09 gọi `kiem_tin_dang(TD002)`, trả ảnh trùng tin TD001 của người bán khác. Cả hai trace đều ghi nguồn `du_lieu_mau_tam`. Tại thời điểm kiểm tra, cả 5 nhánh của origin đều chưa có CSV Chợ Mẫu trong data/. Các tệp raw trong evidence/ là dữ liệu nghiên cứu riêng. Đối chiếu chính thức còn chờ CSV từ issue #6; khi có, chạy lại hai input và xác nhận cả nguồn CSV lẫn tín hiệu trong trace.

### Nguồn cho B13–B20

Đối chiếu cột id của [CSV review](../evidence/raw-chotot_reviews.csv). Các trường hợp dưới đây chuyển ý từ review thành tình huống giả định. Mức kỳ vọng dùng để chấm tình huống đã viết.

| Ca | Review | Chi tiết gốc dùng để dựng ca |
|---|---|---|
| B13 | C3257 · 24/04/2024 | Người viết khuyên gặp nhau kiểm hàng, trả sau khi kiểm. |
| B14 | C3729 · 08/01/2024 | Người mua kể được đồng kiểm hàng. Điều kiện trả sau, từ chối nhận và loại máy do nhóm thêm. |
| B19 | C3504 · 02/03/2024 | Người viết kể giá đăng xe khác giá bán. Nhóm đổi mặt hàng và dựng hai mức giá. |

B15–B18 và B20 do AI soạn theo Canvas. Với 12 ca CP2, bộ CP3 có tổng cộng 20 ca, gồm 7 ca phỏng theo review và 13 ca tự viết.

**Phạm vi nhãn.** Mức kỳ vọng áp dụng cho thông tin người mua có tại thời điểm hỏi. Một review kể về mất cọc có thể gợi ý cách viết ca thử nhưng không xác minh danh tính của người bán trong hội thoại dựng lại. Metric trên main dùng mã expected để xác định nhóm ca lừa và ca người bán thật trong benchmark. Khi chạy, hệ thống chỉ nhận cột `input`; đáp án, tiêu chí và mã nguồn dùng cho người chấm.
