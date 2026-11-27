# Kết quả khảo sát — bản xuất ngày 27/11/2026

## Nguồn và phạm vi

- Nguồn: [Google Sheets nhận phản hồi](https://docs.google.com/spreadsheets/d/1oYM1CZ6PHnJHpb41z17OETy3S-hiqApnwzhBxwcWu2o/edit?gid=1944901882), tab **Câu trả lời biểu mẫu 1**, gid `1944901882`.
- Xuất và xử lý ngày 27/11/2026. Đây là snapshot, không khẳng định Form đã đóng nhận phản hồi.
- Minh xác nhận trong chat ngày 27/11/2026 rằng 20 phản hồi đều do người thật ngoài nhóm tự điền. Chưa có xác nhận riêng về việc từng tìm mua điện thoại cũ online trong 12 tháng cho từng người.
- Bản gốc: `evidence/private/raw-survey.csv`, được Git bỏ qua; SHA-256 `a054d6b8fa979529c3ca6733fecef7182cf14b29296d8c9aa1505c43d657c21a`.
- Bản ẩn danh `results.csv` được giữ tại máy người phụ trách, không kèm PR này. Bỏ dấu thời gian, dùng mã S001–S020; lọc email, liên kết và số liên hệ trong ô văn bản. Báo cáo công khai chỉ chứa số tổng hợp, quy tắc xử lý và câu hỏi, không có từng phản hồi.
- [import-report.json](import-report.json) ghi số dòng, chất lượng dữ liệu và hash để đối chiếu bản xuất.

## Số phản hồi và điều kiện hợp lệ

| Chỉ số | Số lượng | Diễn giải |
|---|---|---|
| Phản hồi có nội dung | 20 | Dòng 2–21 trên Sheets |
| Dòng không phải phản hồi | 1 | Dòng 22 chỉ có lỗi công thức ở cột tính thêm; không tính vào 20 |
| Người thật ngoài nhóm | 20 | Theo xác nhận của Minh trong chat |
| Chọn món gần nhất là “Điện thoại, máy tính bảng” | 5 | Hai loại hàng chung một lựa chọn, chưa tách được điện thoại |
| Chọn loại hàng khác | 9 | Không chứng minh chưa từng tìm điện thoại; cần hỏi thêm |
| Không trả lời món gần nhất | 6 | Không tự bổ sung loại hàng |
| Đã xác nhận đủ tiêu chí lát cắt điện thoại cũ | 0 | Thiếu xác nhận đúng loại hàng và trong 12 tháng |
| Chờ xác minh tiêu chí lát cắt | 20 | `eligible=pending`; chưa dùng để báo đạt ≥20 người phù hợp |
| Phản hồi có lựa chọn cần hỏi lại | 12 | Giữ nguyên, không loại tự động |

Trong câu về yêu cầu cọc/trả trước: 5 chọn “Có”, 6 chọn “Không”, 3 chọn “Không nhớ”, 6 không trả lời. Đây là số của mẫu đồ cũ nói chung. Không suy thành số người đã chuyển tiền hoặc mất cọc.

## Chất lượng dữ liệu

- 8 phản hồi chọn “Không kiểm tra gì” đồng thời với phương pháp kiểm khác.
- 7 phản hồi chọn “Chưa từng nghi ngờ” đồng thời với dấu hiệu nghi ngờ.
- 11 phản hồi chọn “Chưa từng mua đồ cũ online” đồng thời với kênh liên lạc khác.
- Các nhóm trên chồng lặp, tổng có 12 phản hồi được gắn cờ. Câu hỏi có thể được người trả lời hiểu theo các thời điểm khác nhau; cần hỏi lại thay vì tự sửa hoặc loại.
- Cột tính thêm “Tỷ lệ tiền cọc (%)” có `#ERROR!` ở cả 21 dòng dữ liệu của bản xuất. Không đưa cột lỗi vào CSV ẩn danh hoặc sử dụng làm kết quả nghiên cứu.
- Không có căn cứ xác định gửi trùng, nên không xóa phản hồi dựa trên nội dung giống nhau.

## Câu hỏi thực sự có trong bản xuất

Bộ câu hỏi phát hành khác với 7 nhóm câu chuẩn bị trong `questions.md`. Các nhãn cột nguồn:

| Mã nguồn | Nguyên câu hỏi / nhãn cột |
|---|---|
| 1 | Trong 12 tháng qua, bạn mua đồ cũ online bao nhiêu lần? |
| 1.1 | Bạn đã mua đồ cũ qua nền tảng nào? |
| 2 | Lần mua đồ cũ online gần nhất, bạn mua món gì? |
| 2.1 | Giá món hàng (VNĐ) |
| 2.2 | Người bán có yêu cầu đặt cọc hoặc chuyển tiền trước không? |
| 2.3 | Số tiền người bán yêu cầu chuyển trước (VNĐ) |
| 3 | Trước khi chuyển tiền, bạn đã kiểm tra những gì? |
| 3.1 | Bạn mất khoảng bao lâu để kiểm tra? |
| 4 | Những dấu hiệu nào từng khiến bạn nghi ngờ người bán đồ cũ là lừa đảo? |
| 4.1 | Mô tả ngắn gọn lần gần nhất (nếu có) |
| 5 | Bạn hoặc người quen có từng mất tiền khi mua đồ cũ online không? |
| 5.1 | Số tiền bị mất trong vụ gần nhất (VNĐ) |
| 5.2 | Số tiền bị mất có lấy lại được không? |
| 6 | Bạn có từng bỏ mua một món đồ vì sợ bị lừa không? |
| 7 | Bạn có từng bán đồ cũ và bị người mua nghi ngờ là lừa đảo không? |
| 8 | Bạn có biết tính năng "Thanh toán đảm bảo" trên Chợ Tốt không? |
| 9 | Khi mua đồ cũ online, bạn thường liên lạc với người bán qua đâu? |

Các lựa chọn đã được trả lời được giữ nguyên trong CSV ẩn danh; bản CSV không cho biết toàn bộ lựa chọn chưa có lượt chọn hoặc cấu hình nhánh của Form.

## Quy tắc ánh xạ

- Các cột của hợp đồng `questions.md` vẫn có trong `results.csv`; trường không được hỏi để trống, không ghi 0 thay cho thiếu dữ liệu.
- `channel` là nền tảng mua hàng, không phải kênh mời trả lời khảo sát.
- `check_minutes` chỉ có 0 khi chọn rõ “Không kiểm tra”. Những khoảng thời gian khác giữ nguyên trong `check_time_category`, không quy đổi thành điểm giữa.
- `amount_vnd` và `paid` để trống: số được hỏi là yêu cầu chuyển trước (`requested_upfront_amount_vnd`), không phải số thực sự đã chuyển.
- `own_loss_12m` để trống: câu nguồn gộp bản thân/người quen và không giới hạn thời gian 12 tháng. Giữ nguyên ở `loss_experience_scope`, số tiền ở `reported_loss_amount_vnd`; không tự gán khoản tiền cho bản thân người trả lời.
- `last_purchase_month`, `result`, `sellers_checked_30d`, `difficulty`, `last_loss_description`, `abandoned_description` để trống khi câu nguồn không có dữ liệu tương ứng. Mô tả nghi ngờ nằm ở `suspicion_description`.
- Chuẩn hóa `300.000` thành `300000` ở cột tiền, giữ nguyên số tiền theo đơn vị VNĐ.
- `source_row` nối mã ẩn danh với dòng trong bản gốc riêng. `data_quality_notes` ghi điểm cần hỏi lại; `exclusion_reason` để trống khi chưa có kết luận loại.

## Tái lập và việc còn thiếu

Công cụ nhập `import_results.py`, bản gốc và bản ẩn danh từng phản hồi được giữ tại máy người phụ trách. Khi đối chiếu nội bộ, dùng SHA-256 trong `import-report.json` để xác nhận đúng bản xuất. Chỉ xác nhận người thật ngoài nhóm khi có xác nhận thực tế của Minh; không suy ra từ việc có sẵn file CSV. Chưa công bố từng phản hồi.

Cần hỏi bổ sung loại hàng điện thoại riêng và thời điểm trực tiếp tìm mua trong 12 tháng, xác minh các lựa chọn cần hỏi lại, và tuyển thêm nếu chưa đủ ≥20 người phù hợp. Chưa dùng snapshot này để kết luận giả thuyết cho riêng điện thoại cũ hoặc tính tần suất kiểm người bán/phút kiểm chính xác.
