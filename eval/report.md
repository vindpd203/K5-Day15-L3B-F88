# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-191256` | 9/20 | 45% | 2/7 (29%) | 4/10 (40%) | 3/3 (100%) | chưa đạt (`muc_dung_nhan` 10/17 = 58,8% < 75%; 0/4 lọt lừa; 0/8 báo oan; 100% số liệu khớp công cụ) |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Quá dè dặt ở giao dịch kiểm trước trả sau (`cho_kiem_truoc_khi_tra` chưa được hướng dẫn ở prompt Bước 4 nên hạ về `can_kiem_them` khi thiếu STK/giá) | 6 | B05, B08, B13, B14, B17, B18 |
| Bước 4 không nhận nguyên văn hội thoại gốc nên mất chi tiết tình huống (đổi sang máy mới, tin đồn chung, hẹn xem trực tiếp trong chat không dấu, mốc giá thứ hai) | 4 | B03, B04, B06, B19 |
| Bước 1 gán nhầm `ngoai_pham_vi = true` cho ca đã chuyển tiền rồi bị chặn liên lạc | 1 | B02 |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B02 | Tin Galaxy A54, đã chuyển tiền theo yêu cầu gửi hàng, người bán chặn liên lạc và máy chưa tới | `muc = tu_choi`, lý do "xử lý khiếu nại/tố cáo sau khi đã bị lừa đảo nằm ngoài phạm vi" | `SYSTEM_EXTRACT` chưa tách rõ người dùng nhờ tố cáo hộ (`tu_choi`) với người mua báo đã chuyển tiền rồi bị chặn (`da_chuyen_tien = true` → cần cảnh báo `dau_hieu_lua_dao` và hướng dẫn liên hệ ngân hàng) |
| B05 | Tin iPhone 12, người bán đáp: "Không cần cọc, cứ đến cửa hàng kiểm máy, đăng xuất iCloud xong mới trả" | `muc = can_kiem_them` vì thiếu giá đăng, tiền cọc và số TK/mã tin | Quy tắc G10 ở Bước 5 cho phép ra `tuong_doi_an_toan` khi `cho_kiem_truoc_khi_tra = true`, nhưng `SYSTEM_DECIDE` ở Bước 4 chưa biết quy tắc này nên tự chọn `can_kiem_them` khi thấy thiếu STK/giá |
| B19 | Tin ghi giá 4 triệu, khi hẹn xem người bán báo 5 triệu cho đúng chiếc đó chưa giải thích | `muc = can_kiem_them`, chỉ nhắc giá 4 triệu và khuyên gọi video, không nhắc mốc 5 triệu hay chốt giá cuối bằng tin nhắn trước khi đi | Bước 1 chỉ có một trường `gia_dang = 4000000`, còn Bước 4 không được truyền nguyên văn `input` nên mất mốc giá 5 triệu và bối cảnh sắp đi xem máy |
| B03 | Hẹn xem iPhone 13 trong tin, người bán bảo vừa bán mất và mời xem máy khác cùng giá | `muc = can_kiem_them`, nhận ra đổi máy nhưng `buoc_kiem` lại bảo gọi video quay IMEI của chiếc iPhone 13 đã bán | Bước 4 không thấy nguyên văn đoạn chat nên nhầm trường `doi_may = iPhone 13` là chiếc máy mới đang được mời xem |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: __
- Nếu có thêm 1 tuần: __
