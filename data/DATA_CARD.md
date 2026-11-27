# Dữ liệu đánh giá giao dịch điện thoại cũ

Bản cập nhật benchmark CP3, ngày 27/11/2026.

| Nguồn | Cách dùng và giới hạn |
|---|---|
| Trích review Chợ Tốt trong [đề xuất §1](../docs/de-xuat-do-cu.md) | Đề xuất mô tả 5.000 review Google Play thu ngày 27/11. Bản này sử dụng bốn trích đoạn đã bỏ tên có mã C0070, C0342, C0005, C0124. Review là lời kể của người viết. Không suy rộng tỷ lệ mất cọc từ số lượt khớp từ khóa. |
| [Benchmark CP2](../eval/benchmark.csv) | 12 ca tiếng Việt. B01–B04 phỏng theo bốn review tương ứng ở trên. Điện thoại, điều kiện giao dịch và hội thoại được dựng cho bài đánh giá; C0005 gốc nói về xe, C0124 là nhận xét chung. B05–B12 do AI soạn theo Canvas và đề xuất để Khánh duyệt. Toàn bộ đầu vào là tình huống viết lại, không chứa danh tính người bán. Soạn trực tiếp, không dùng lấy mẫu ngẫu nhiên hay seed. Số ca đã được thành viên nhóm rà tay chưa ghi nhận. |
| [Tin đăng Chợ Tốt](../evidence/raw-chotot_listings.csv) · thật | Cào ngày 27/11/2026 từ API công khai `gateway.chotot.com/v1/public/ad-listing` bằng [script](../evidence/scrape_chotot_listings.py): 1.500 tin mới nhất (500 điện thoại, 500 laptop, 500 xe máy), `body` cắt 300 ký tự. Công cụ `tra_gia_thi_truong` gom giá điện thoại đã dùng theo `mobile_model` (bỏ "Dòng khác", bỏ tin mới `condition=1`, cần ≥3 tin) → 37 đời máy, khoảng giá = tứ phân vị 25–75%. `kiem_tin_dang` tra được mã tin Chợ Tốt (số trong link). Giới hạn: một lần cào, giá đăng chứ không phải giá bán, lẫn tin shop/trả góp; nhiều đời chỉ 3–10 tin (iPhone 13: 7 tin); laptop và xe máy không có trường đời máy nên chưa dùng cho giá; không có mã ảnh nên không kiểm được trùng ảnh. |
| [Người bán Chợ Tốt](../evidence/raw-chotot_sellers.csv) · thật | Cào cùng ngày từ API `profile/{account_oid}` bằng [script](../evidence/scrape_chotot_sellers.py): 816 hồ sơ của người bán trong tập tin đăng. `kiem_tin_dang` lấy tuổi tài khoản (`account_age_days`, tính tại ngày cào) và điểm đánh giá (`seller_rating` của tin). API không trả số lượt đánh giá và số tin đã đăng nên hai trường này để trống, luật "chưa có đánh giá" không áp dụng cho người bán Chợ Tốt. Chưa ẩn danh: có tên hiển thị và địa chỉ thật của người bán. |
| Giá tham chiếu · synthetic | Dự kiến khoảng 40 mục theo đời và tình trạng, giá ước tính để kiểm phép so giá. |
| Tin đăng · synthetic | Dự kiến khoảng 60 tin để tra mã tin và trùng ảnh trong Chợ Mẫu. |
| Người bán · synthetic | Dự kiến khoảng 40 hồ sơ để tra tuổi tài khoản, số tin và đánh giá. |
| Tài khoản cảnh báo · synthetic | Dự kiến khoảng 15 mã giả để kiểm luật chặn. Chỉ có ý nghĩa trong Chợ Mẫu. |
| Chat · synthetic | Dự kiến khoảng 30 đoạn hội thoại lừa, thật và mơ hồ. Dùng mã và hội thoại hư cấu. |

### Đối chiếu B01 và B09 sau PR #17

Ngày 27/11/2026, chạy nguyên đầu vào B01 và B09 của benchmark qua `answer()` với `MODEL_PROVIDER=fake`, dùng code trên `main` tại `5d201c2`. Cả hai đầu ra đều là JSON, có `muc = dau_hieu_lua_dao`, khớp nhãn kỳ vọng. Bảng dưới đối chiếu `so_lieu` và mã trong `tin_hieu` với trace công cụ của từng ca.

| Ca | Giá và tiền cọc | Tra tài khoản, tin và ảnh | Mã luật trong đầu ra |
|---|---|---|---|
| B01 · iPhone 12 | Giá đăng 5.000.000 đ, cao hơn 9,3% so với giá tham chiếu 4.575.000 đ từ tin đăng Chợ Tốt. Cọc 500.000 đ bằng 10% giá đăng. | STK trong bộ dự phòng có 5 lượt báo cáo, kích hoạt cảnh báo đỏ. Đầu vào thiếu mã tin để kiểm ảnh. | Đỏ: `tk_canh_bao`. Vàng: `thuc_ep`. |
| B09 · TD002 | Giá đăng 6.500.000 đ, thấp hơn 36,6% so với giá tham chiếu 10.250.000 đ của bộ dự phòng. Tỷ lệ cọc là `null` vì thiếu số tiền cọc. | TD002 dùng trùng ảnh với TD001 của người bán khác trong bộ dự phòng. Đầu vào thiếu STK và SĐT để tra cảnh báo tài khoản. | Đỏ: `gia_thap_30`, `anh_trung`. Vàng: `tai_khoan_moi`, `chua_danh_gia`, `thuc_ep`. |

Nguồn giá B01 là `evidence/raw-chotot_listings.csv`. Trace ghi `du_lieu_mau_tam` cho danh sách STK ở B01, giá và dữ liệu tin ở B09. Khi issue #6 có CSV Chợ Mẫu chính thức, chạy lại hai ca và đối chiếu nguồn trong trace. Lượt thử này dùng để kiểm luồng và hợp đồng JSON; kết quả đánh giá CP3 cần lượt chạy với model thật.

### Nguồn cho B13–B20

Đối chiếu cột id của [CSV review](../evidence/raw-chotot_reviews.csv). Các trường hợp dưới đây chuyển ý từ review thành tình huống giả định. Mức kỳ vọng dùng để chấm tình huống đã viết.

| Ca | Review | Chi tiết gốc dùng để dựng ca |
|---|---|---|
| B13 | C3257 · 24/04/2024 | Người viết khuyên gặp nhau kiểm hàng, trả sau khi kiểm. |
| B14 | C3729 · 08/01/2024 | Người mua kể được đồng kiểm hàng. Điều kiện trả sau, từ chối nhận và loại máy do nhóm thêm. |
| B19 | C3504 · 02/03/2024 | Người viết kể giá đăng xe khác giá bán. Nhóm đổi mặt hàng và dựng hai mức giá. |

B15–B18 và B20 do AI soạn theo Canvas. Với 12 ca CP2, bộ CP3 có tổng cộng 20 ca, gồm 7 ca phỏng theo review và 13 ca tự viết.

**Phạm vi nhãn.** Mức kỳ vọng áp dụng cho thông tin người mua có tại thời điểm hỏi. Một review kể về mất cọc có thể gợi ý cách viết ca thử nhưng không xác minh danh tính của người bán trong hội thoại dựng lại. Metric trên main dùng mã expected để xác định nhóm ca lừa và ca người bán thật trong benchmark. Khi chạy, hệ thống chỉ nhận cột `input`; đáp án, tiêu chí và mã nguồn dùng cho người chấm.
