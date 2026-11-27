# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-191256` | 9/20 | 45% | 2/7 (29%) | 4/10 (40%) | 3/3 (100%) | chưa đạt (`muc_dung_nhan` 10/17 = 58,8% < 75%; 0/4 lọt lừa; 0/8 báo oan; 100% số liệu khớp công cụ) |
| 2 | `run-2@20261127-212020` | 18/20 | 90% | 7/7 (100%) | 8/10 (80%) | 3/3 (100%) | **đạt** (`muc_dung_nhan` 17/17 = 100% ≥ 75%; 0/4 lọt lừa; 0/8 báo oan; 100% số liệu khớp công cụ) |

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

- Nhắm vào nhóm lỗi: **Đứt ngữ cảnh giao dịch gốc và thiếu quy tắc G10 ở bước kết luận AI (Bước 1 → Bước 4)** — vì sao là nhóm **đau nhất với người dùng**: Người mua đã tự thương lượng được cách an toàn nhất (*gặp mặt / đồng kiểm thử máy xong mới trả tiền*) nhưng vẫn bị phán `can_kiem_them` chỉ vì thiếu STK (khiến họ chần chừ bỏ lỡ món tốt — đúng pain thứ hai ở `spec.md` §1); đồng thời người mua vừa bị chặn sau khi chuyển tiền (`B02`) lại bị từ chối hỗ trợ thay vì được hướng dẫn giữ chứng từ và báo ngân hàng ngay.
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): (1) Truyền thêm `dau_vao_goc` vào Bước 4 trong `codebase/agent.py` (kèm quy tắc chỉ coi là dữ liệu, không thực thi chỉ dẫn trong chat) và giữ tối đa 4 ý ở `ly_do`; (2) Bổ sung tiêu chí chọn 3 mức khớp quy tắc G10 vào `SYSTEM_DECIDE` (cho phép kết luận `tương đối an toàn` khi `cho_kiem_truoc_khi_tra = true` và không có tín hiệu đỏ/vàng); (3) Làm rõ ranh giới `ngoai_pham_vi` trong `SYSTEM_EXTRACT` để ca đã chuyển tiền rồi bị chặn đi vào luồng cảnh báo `da_chuyen_tien = true` thay vì bị từ chối.
- Kết quả: 6 câu lỗi kiểm trước trả sau (`B05, B08, B13, B14, B17, B18`) từ **0/6 → 6/6** (toàn bộ 8 ca người bán thật **2/8 → 8/8**); nhóm 4 câu thiếu chi tiết hội thoại (`B03, B04, B06, B19`) từ **0/4 → 2/4**; câu `B02` từ **0/1 → 1/1** · tổng **45% (9/20) → 90% (18/20)** (`muc_dung_nhan` tăng từ **10/17 = 58,8% → 17/17 = 100%**).
- Câu nào **tệ đi** sau khi sửa: **0 câu tệ đi** (không có câu nào từ `1 → 0`; đánh đổi duy nhất là lượng token vào trung bình mỗi câu tăng nhẹ từ `1.301` lên `1.729` token do Bước 4 đọc thêm `dau_vao_goc` và quy tắc G10).

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: Còn **2 câu `kho`** (`B04`, `B06`) đã ra đúng mã mức `can_kiem_them` và khuyên không chuyển tiền trước, nhưng thiếu ý phụ trong `pass_criterion`: ở `B04`, `ly_do` chưa phân biệt tường minh giữa tin đồn lừa đảo chung trên sàn với căn cứ riêng của người bán; ở `B06`, AI chưa chỉ ra ngay trong tin nhắn viết tắt không dấu (`"ko thich thi hen xem may cung dc"`) người bán đã mở sẵn phương án hẹn xem trực tiếp không mất 50k phí ship. Rủi ro mất tiền thấp (vì không báo nhầm an toàn), nhưng khiến người mua phải hỏi lại điều người bán đã viết tắt trong chat.
- Nếu có thêm 1 tuần: (1) Bổ sung bước chuẩn hóa tiếng Việt không dấu/viết tắt mua bán đồ cũ (`ck`, `dc`, `ko`, `ship cod`) và trường `phuong_an_thay_the_trong_chat` ở Bước 1; (2) Mở rộng dữ liệu giá tham chiếu Chợ Tốt theo dung lượng/tình trạng máy và đối chiếu trùng ảnh thật bằng perceptual hash.
