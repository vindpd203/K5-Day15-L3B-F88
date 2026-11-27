# Đào review Chợ Tốt · issue #5

## Nguồn và cách đếm

- File nhóm cung cấp: `evidence/raw-chotot_reviews.csv`; nhận/kiểm ngày 27/11/2026. Không lấy snapshot mới.
- Nguồn khai báo của nhóm: Google Play VN, app `com.chotot.vn`, mọi mức sao, sort NEWEST; script `evidence/scrape_chotot.py`. Không có reviewId Google trong file cũ nên chỉ truy ngược được theo ID cục bộ + hash snapshot, không dựng link review riêng.
- [Trang nguồn](https://play.google.com/store/apps/details?id=com.chotot.vn&hl=vi&gl=VN). Ngày kiểm file: 27/11/2026; trang web chưa xác minh độc lập trong lượt này.
- 5000 dòng, 5000 ID khác nhau, ngày review 29/06/2023–25/11/2026.
- SHA-256: `eec56eb8f707840319b8ef65f7cad1d8e001db2cde2cdf48f4c22ea2138fc18f`.
- Cột: id, date, score, content, labels (từ khóa), nhan_tay (toàn bộ đang trống khi nhận).
- Cách đếm được ghi trước lượt gắn nhãn mới, sau khi đã biết số từ khóa và ví dụ trong đề xuất. Không coi đây là nghiên cứu chưa tiếp xúc dữ liệu.
- Chạy lại thống kê: `python -X utf8 evidence/count.py stats evidence/raw-chotot_reviews.csv`.

## Định nghĩa nhãn và chọn mẫu

Đơn vị: một review. Chuẩn hóa NFC, chữ thường và khoảng trắng; bỏ nội dung rỗng/trùng nội dung, giữ dòng đầu theo thứ tự snapshot. Tập hợp lệ còn **3616** nội dung; loại **1384** dòng. Đây là lựa chọn phân tích, có thể làm thay đổi trọng số các phản ánh lặp lại; không coi mỗi nội dung là một người dùng đã xác minh.

Seed **20261127**: lấy **300** review ngẫu nhiên không hoàn lại từ tập hợp lệ; sau đó lấy tối đa 500 review còn lại có nhãn từ khóa `lua_dao` hoặc `coc_chuyen_tien`. Chỉ có **204** dòng đáp ứng còn lại, nên lấy hết. Tổng mẫu **504** dòng, hai tầng không trùng ID. Không bổ sung dòng khác để đủ con số 500. Mẫu và manifest trong thư mục ignored `evidence/private/`.

| Nhãn cuối | Điều kiện |
|---|---|
| bi_lua_coc | Người viết tự thuật đã chuyển tiền cho người bán rồi bị chặn/không nhận hàng, hoặc tự thuật rõ bị mất tiền cọc. Không cần tự suy đoán ý định người bán; đây là phản ánh chưa xác minh |
| khong_du_bang_chung | Có đề cập nghi lừa, cọc hoặc mất tiền nhưng thiếu vai, thiếu việc đã chuyển/kết quả, chỉ kể chung hoặc đề xuất tính năng; không đủ điều kiện nhãn trên |
| khong_lien_quan | Phí đăng tin/nạp đồng tốt, lỗi app, tuyển dụng, phòng trọ, phản ánh loại khác không liên quan mất cọc của người mua hàng |

Ưu tiên loại khác rõ ràng trước; chỉ dùng nhãn bất định nếu có liên quan nhưng thiếu căn cứ. Review không chỉ rõ điện thoại không chứng minh riêng pain của người mua điện thoại.

Pilot cố định: 15 dòng ngẫu nhiên + 15 dòng từ khóa. Codex đã đọc và gợi ý nhãn cho 504 dòng. Ngày 27/11/2026, **Minh xác nhận trong chat rằng các nhãn khớp với phần nhãn mình làm**, yêu cầu ghi vào phần của Minh. Đã chép đúng 504 giá trị sang `nhan_minh`, ghi `nguoi_duyet = Nguyễn Nhật Minh`, `loai_duyet = human`; căn cứ của Minh ghi rõ đây là xác nhận qua chat với căn cứ tham chiếu từ bản phân loại ban đầu. Giá trị nhãn cuối, ID, tầng và nội dung gốc không thay đổi.

Đây là xác nhận của Minh theo lời Minh cung cấp, chưa có file nhãn độc lập riêng của Minh để đối chiếu bằng máy. `nhan_khanh` vẫn trống; không báo độ đồng thuận Minh/Khánh hoặc nói đã có hai người chấm độc lập. Nguồn gợi ý Codex và cách xác nhận được giữ trong manifest và khai báo dùng AI.

85 đề xuất AI ban đầu được giữ nguyên để lưu lịch sử. Nhãn cuối có thể khác đề xuất sau khi đọc lại theo định nghĩa (ví dụ C2837 thiếu xác nhận tiền cọc là của chính người viết, nên nhãn cuối là `khong_du_bang_chung`). Bản trước sửa và nhật ký từng nhãn + hash nội dung lưu riêng trong `private/sample.before-codex-final.csv`, `private/codex-final-audit.json`.

## Kết quả đếm từ khóa đã kiểm lại

Mẫu số bảng này là **5000 review raw**, không phải 504 dòng được chọn, không phải 3616 nội dung riêng biệt.

| Nhãn từ khóa có sẵn | x/N | % |
|---|---|---|
| lua_dao | 190/5000 | 3,80% |
| coc_chuyen_tien | 58/5000 | 1,16% |
| nguoi_ban_khong_tin | 145/5000 | 2,90% |
| tin_ao_sai_mo_ta | 247/5000 | 4,94% |
| khoa_tai_khoan | 356/5000 | 7,12% |
| Review 1–2 sao | 2166/5000 | 43,32% |

Các nhãn có thể cùng xuất hiện, không cộng thành tổng người. Nhiễu rõ: “mất tiền” thường là phí đăng tin; từ “ảo” có thể khớp trong “đảo”.

| Năm | lua_dao / review năm đó | % |
|---|---|---|
| 2023 | 38/1228 | 3,09% |
| 2024 | 70/1573 | 4,45% |
| 2025 | 36/1429 | 2,52% |
| 2026 | 46/770 | 5,97% |

## Kết quả phân loại — Minh xác nhận trên gợi ý Codex, 27/11/2026

| Tầng | Số dòng đã phân loại | bi_lua_coc | khong_du_bang_chung | khong_lien_quan | Tỷ lệ nhãn bi_lua_coc trong tầng |
|---|---|---|---|---|---|
| Ngẫu nhiên | 300/300 | 0 | 13 | 287 | 0/300 (0,00%) |
| Từ khóa bổ sung | 204/204 | 2 | 86 | 116 | 2/204 (0,98%) |

Đây là thống kê nhãn ban đầu do Codex phân loại, **504 nhãn được ghi vào phần Minh dựa trên xác nhận khớp của Minh trong chat**. Người duyệt cuối ghi Minh; không thay đổi nhãn để đổi số liệu. Pilot có nhãn Minh **30/30**, chưa có nhãn Khánh và số cặp đối chiếu vẫn **0/30**. Không coi đây là xác minh giao dịch thực tế. Không gộp tỷ lệ hai tầng hoặc kết luận không có lừa đảo từ 0/300. Hai dòng mất cọc rõ vẫn là **C0342, C2567**.

Tái lập bảng từ bản nhãn không chứa toàn văn review: `python -X utf8 evidence/count.py count evidence/annotations-codex.csv`. Bản làm việc đầy đủ giữ trong `private/sample.csv`. Báo cáo tổng hợp và hash đầu vào: `evidence/label-report.json`. Chưa đạt tiêu chí giả thuyết ≥5 review tự thuật rõ chuyện cọc/kết quả; không thay ngưỡng để khớp hai trường hợp tìm được.

## Ví dụ đã đối chiếu trực tiếp với file gốc

Các đoạn sau là trích nguyên văn ngắn (≤2 câu/review), không có tên tác giả. Nhận xét bắt đầu từ bản phân loại Codex; Minh đã xác nhận nhãn khớp qua chat. Không coi lời kể trong review là vụ việc đã được xác minh độc lập.

| ID · ngày | Trích ngắn | Nhận xét đề xuất |
|---|---|---|
| C0342 · 20/06/2026 | “khi cọc tiền cho người bán xong thì họ chặn mình, và không gửi hàng” | Đủ mô tả cọc → chặn/không hàng; chưa biết loại món |
| C2567 · 05/11/2024 | “vừa bị lừa mất 100k tiền cọc ae ạ” | Tự thuật mất cọc; chưa xác minh giao dịch |
| C2837 · 02/08/2024 | “Người bán hàng trên chợ tốt lừa tiền cọc của khách hàng, dù mình đã khiếu nại nhưng không có một hồi âm nhỏ nào.” | Có tự thuật khiếu nại tiền cọc; người duyệt cần xác nhận vai |
| C0070 · 18/10/2026 | “Bắt cọc tiền rồi chặn” | Cụm mô tả chiêu; không rõ chính người viết đã chuyển hay không |
| C0413 · 29/05/2026 | “tốn tiền mà k đăng được cũng không hoàn trả” | Phí đăng tin của người bán, không phải mất cọc mua hàng |
| C1360 · 28/07/2025 | “nếu gửi hàng toàn bắt cọc tiền thế là bị lừa” | Cảnh báo chung, chưa đủ tự thuật giao dịch |
| C2073 · 13/02/2025 | “Chotot nên hỗ trợ người bán và người mua nếu bên bán đòi tiền cọc mới ship hàng thì tiền cọc đó nguoi mua chuyển vào chotot giữ cọc dùm” | Đề xuất giữ cọc, không phải bằng chứng một vụ mất cọc |

## Giới hạn

Review là lời kể công khai chưa xác minh, thiên về người chủ động đánh giá; không đo tỷ lệ nạn nhân trong toàn bộ người dùng. Mẫu Google Play không đại diện Facebook/Zalo, nhiều loại hàng và vai người bán. Mẫu từ khóa bỏ sót cách viết khác; tập unique loại các phản ánh lặp. Chưa có bằng chứng riêng cho phạm vi điện thoại hoặc số phút kiểm người bán, cần phỏng vấn/khảo sát đúng đối tượng.
