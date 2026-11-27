# Khảo sát hành vi mua điện thoại cũ online

Phụ trách: Nguyễn Nhật Minh · issue #5 · soạn 27/11/2026.

**Trạng thái:** đã có Form và bảng kết quả theo liên kết Minh cung cấp; chưa xác nhận đã gửi lên các kênh hoặc số phản hồi. Chưa đối chiếu nội dung Form với bộ câu hỏi chuẩn bị bên dưới.

## Liên kết và nhật ký phát hành

| Loại | Liên kết | Mục đích |
|---|---|---|
| Gửi khảo sát | [Mở Form cho người trả lời](https://docs.google.com/forms/d/e/1FAIpQLSfasj5d9ard8NNH1zDJIE7FzxJzZOSE6_3ZUdZd_gYi1RgEBA/viewform) | Dùng link này khi mời tham gia |
| Chỉnh sửa | [Chỉnh sửa Google Form](https://docs.google.com/forms/d/1wUTqO5wVRb20c4E-wD6HE7bVNW2pjNc5vnhAQea63j8/edit) | Dành cho người quản lý có quyền truy cập |
| Kết quả | [Google Sheets nhận phản hồi](https://docs.google.com/spreadsheets/d/1oYM1CZ6PHnJHpb41z17OETy3S-hiqApnwzhBxwcWu2o/edit) | Xem và xuất kết quả; CSV đã ẩn danh mới đưa vào repo |

- Bộ liên kết mới thay bộ cũ; log Minh cung cấp: **17:38:36**, chưa có ngày trong log. Đây là mốc ghi log liên kết, không tự coi là giờ gửi hoặc giờ mở nhận phản hồi.
- Kênh dự kiến: Discord lớp và nhóm bạn. Kênh đã gửi, giờ gửi/mở/chốt thực tế: chưa được xác nhận.
- Số phản hồi/số hợp lệ: **bổ sung sau khi chốt khảo sát** theo yêu cầu của Minh; chưa kiểm tra, không mặc định bằng 0. Khi có kết quả, lưu bản đã ẩn danh vào `evidence/survey/results.csv` và cập nhật `evidence/summary.md`.
- Mục tiêu tuyển ≥25 để có ≥20 câu hợp lệ ngoài nhóm trước CP3 10:00 ngày 28/11/2026.

Lời mở: “Nhóm F88 tìm hiểu lần mua điện thoại cũ online gần nhất. Khảo sát khoảng 3–5 phút, tự nguyện; bạn có thể bỏ qua câu nhạy cảm. Không nhập tên, email, số điện thoại, tài khoản ngân hàng hay thông tin người bán. Không cần kể thông tin nhận diện. Kết quả được tổng hợp cho bài hackathon.”

Không bật thu email, không yêu cầu đăng nhập, không thu liên hệ trong form này. Nếu muốn phỏng vấn, người tham gia chủ động nhắn Minh riêng; không đưa liên hệ vào repo.

## 7 câu chính

| # | Nguyên câu hỏi | Kiểu / nhánh |
|---|---|---|
| 1 | Bạn có phải thành viên nhóm F88 không? Trong 12 tháng qua, bạn có trực tiếp tìm mua điện thoại cũ qua tin đăng hoặc chat online không? | Hai lựa chọn sàng lọc trong một phần: thành viên F88 → kết thúc, không từng tìm mua → kết thúc |
| 2 | Lần gần nhất đó là tháng/năm nào, qua kênh nào, và kết quả là gì? | Tháng/năm; Chợ Tốt/Facebook/Zalo/khác; đã mua/chưa mua/bỏ giao dịch. Không cần tên shop |
| 3 | Trong 30 ngày qua, bạn đã kiểm tra bao nhiêu người bán điện thoại cũ khác nhau trước khi quyết định mua? | Số nguyên ≥0; thêm “không nhớ”. Phân biệt kiểm nhiều người bán với số máy đã mua |
| 4 | Ở lần gần nhất, người bán yêu cầu thanh toán lúc nào? Bạn đã thực sự chuyển khoản/cọc chưa, khoảng bao nhiêu? | Không đòi trước/đòi cọc/đòi toàn bộ/không nhớ; chưa chuyển/đã chuyển/không muốn trả lời; số tiền hoặc khoảng tiền tùy chọn. Không hỏi số tài khoản |
| 5 | Trước khi quyết định, bạn đã làm gì để kiểm tin đăng/người bán? Lần đó mất khoảng bao nhiêu phút và khó nhất ở bước nào? | Chọn nhiều: xem lịch sử/đánh giá, so giá, hỏi ảnh/video, gặp trực tiếp, hỏi người quen, không kiểm, khác; số phút hoặc “không nhớ”; đoạn ngắn |
| 6 | Giao dịch gần nhất kết thúc ra sao? Nếu đã chuyển tiền, bạn nhận hàng hoặc nhận hoàn tiền chưa? Trong 12 tháng qua chính bạn có lần nào chuyển tiền rồi không nhận hàng/không được hoàn không? | Kết quả lần gần nhất + Có/Không/Không rõ/Không muốn trả lời; nếu có, kể một lần và khoảng tiền tùy chọn. Chỉ hỏi bản thân, không cộng chuyện người quen |
| 7 | Có lần nào bạn quyết định không mua vì chưa kiểm được người bán không? Kể lần gần nhất: bạn chưa kiểm được điều gì và đã làm gì tiếp? | Có/Không/Không nhớ; kể ngắn nếu có. Không hỏi “có thích AI không” |

Câu 1–7 là 7 nhóm câu, có trường phụ để tách số khi nhập Form. Ghi nguyên văn cả câu hỏi và các lựa chọn thực sự phát hành nếu có chỉnh sửa.

## Quy tắc hợp lệ và lưu kết quả

- Ngoài nhóm F88; trực tiếp tìm mua điện thoại cũ online trong 12 tháng; đồng ý trả lời; đủ thông tin sàng lọc. “Không nhớ” vẫn hợp lệ, loại khỏi mẫu số của chỉ số không có giá trị, công bố n thiếu.
- Không ép mua thành công, không chỉ tuyển người từng mất tiền. Không tự coi câu trả lời giống nhau là cùng một người; chỉ loại bản gửi trùng khi có căn cứ và ghi lý do.
- Export gốc để `evidence/private/raw-survey.csv`. Không commit bản gốc chứa thông tin nhận diện.
- Bản đã rà/ẩn danh để `results.csv`: response_id (S001…), eligible, exclusion_reason, channel, last_purchase_month, result, sellers_checked_30d, upfront_request, paid, amount_vnd, check_minutes, check_method, difficulty, own_loss_12m, last_loss_description, abandoned_description. Không điền kết quả mẫu giả.
- Công bố số nhận, số hợp lệ, số thiếu theo từng câu; n nhỏ chỉ ghi x/n. Đủ ≥20 hợp lệ mới đánh dấu nguồn khảo sát đạt ngưỡng. Nêu cách tuyển thuận tiện, không suy rộng ra toàn bộ người dùng.
