# PLAN · Track D · Kiểm người bán đồ cũ trước khi chuyển cọc

## Kế hoạch của Nguyễn Nhật Minh — kiểm tra ngày 27/11/2026

**Tiến độ triển khai #5 sau kiểm tra:** đã nhận snapshot 5000 review, kiểm hash/số từ khóa, tạo mẫu 504 dòng và pilot 30. Minh xác nhận qua chat rằng nhãn Codex khớp phần mình làm; đã ghi 504 nhãn vào `nhan_minh`, người duyệt cuối Nguyễn Nhật Minh, `loai_duyet=human`. Nguồn gợi ý Codex và cách xác nhận giữ trong manifest; chưa có file nhãn Minh riêng hoặc đối chiếu Minh/Khánh. Kết quả giữ nguyên: random 0/300 mất cọc, keyword 2/204. Form đã có bộ link mới theo log 17:38:36, kết quả bổ sung sau. Xem `evidence/issue-5-handoff.md` cho trạng thái hiện tại; nhận xét “chưa thấy raw” bên dưới là tại lượt kiểm tra ban đầu và đã được xử lý. Chưa xác nhận gửi form hoặc lịch hẹn.

### Kiểm tra issues GitHub

Đã đọc GitHub API ngày 27/11/2026: 9 issue (#2–#10), tất cả đang mở, chưa có comment. Đây là trạng thái issue tại lúc kiểm tra; checkbox chưa tích không tự chứng minh công việc ngoài repo chưa làm.

| Issue | Người được giao | Liên quan đến Minh |
|---|---|---|
| [#5 Bằng chứng](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/5) | NhMinh-2610 | Chủ trì: khảo sát, lịch phỏng vấn, cách đếm và gắn nhãn review |
| [#2 Canvas](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/2), [#3 Spec](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/3) | vindpd203 | Bàn giao số có nguồn, ví dụ và giới hạn cho Vinh |
| [#8 Benchmark](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/8) | dkhanhdev | Bàn giao review đã kiểm, mã nguồn ổn định để Khánh viết câu thử |
| [#4 Chuẩn đạt](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/4) | dkhanhdev, vindpd203 | Góp bằng chứng; người phụ trách chốt trước CP2 |
| [#6 Chợ Mẫu](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/6) | thehung1406, dkhanhdev | Cung cấp tình huống; phân biệt dữ liệu dựng với bằng chứng thật |
| [#7 Workflow](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/7), [#9 Model](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/9) | thehung1406 | Chưa thuộc phạm vi triển khai của Minh |
| [#10 Nộp CP2](https://github.com/vindpd203/K5-Day15-L3B-F88/issues/10) | vindpd203 | Bàn giao tiến độ #5 và đường dẫn tài liệu trước khi Vinh nộp |

### Kiểm tra phần việc của Minh

- `TEAMS.md` xác nhận Minh phụ trách `evidence/`. Nhánh tại lúc kiểm tra: `NguyenNhatMinh`.
- `evidence/hypothesis.md`, `data-mining.md`, `summary.md` còn mẫu; khảo sát và phỏng vấn mới có `TEMPLATE.md`. Chưa thấy kết quả, link form hoặc lịch hẹn đã xác nhận trong các file này.
- Chưa tìm thấy `evidence/raw-chotot_reviews.csv` tại workspace. Số 190/5000 và các trích dẫn trong đề xuất chưa được tái kiểm bằng dữ liệu gốc trong lượt kiểm tra này; chưa đưa thành kết quả gắn nhãn tay.
- Có `evidence/scrape_chotot.py`, nhưng `google_play_scraper` chưa được khai báo trong `requirements.txt`. Chỉ cài/chạy khi cần lấy dữ liệu mới; bản lấy mới không mặc nhiên tái hiện 5000 review và các mã Cxxxx của lần lấy cũ.
- `.gitignore` có `evidence/**/raw-*`, chưa có quy tắc rõ cho file `evidence/raw-chotot_reviews.csv` ở ngay gốc thư mục evidence. Cần thêm quy tắc cụ thể và kiểm bằng `git check-ignore` trước khi tạo file raw.
- `python run.py check` xác nhận 4 thành viên; benchmark mới có 3 câu mẫu và 0 metric hoàn chỉnh. Lệnh này không xác nhận chất lượng bằng chứng; phần benchmark/metric cần Khánh xử lý theo #8/#4.

### Kế hoạch hoàn thành

Các giờ dưới đây là mốc đề xuất theo giờ Việt Nam, không phải lịch hẹn đã xác nhận. Thời lượng gắn nhãn cần điều chỉnh sau pilot 30 dòng.

| Ưu tiên / mốc | Việc cụ thể | Đầu ra và tiêu chí hoàn thành |
|---|---|---|
| P0 · 27/11, 17:00–17:30 | Xác nhận file raw cũ với nhóm; nếu không còn thì lấy snapshot mới. Bổ sung ignore và dependency trước khi chạy scraper | Raw lưu riêng, không stage; ghi ngày lấy, số dòng thực tế, khoảng ngày, SHA-256 và phiên bản công cụ. Giữ snapshot cố định để mã dòng không đổi |
| P0 · 17:00–17:30 | Soạn form và câu hỏi phỏng vấn theo người mua điện thoại cũ; Minh gửi và đặt lịch thực tế | `survey/questions.md`, link form + kênh + giờ gửi; lịch hẹn trong `summary.md`. Mục tiêu tuyển ≥25 để có ≥20 câu trả lời hợp lệ ngoài nhóm; không ghi đã gửi/đã hẹn trước khi thực hiện |
| P0 · 17:30–18:00 | Ghi giả thuyết và định nghĩa nhãn trước lượt gắn nhãn mới; ghi rõ đã đọc đề xuất và ví dụ có sẵn | `hypothesis.md`, `data-mining.md`: tiêu chí vào/ra, mẫu số, nhãn `bi_lua_coc`/`khong_du_bang_chung`/`khong_lien_quan`, cách xử lý spam và trùng. Không ghi lùi thời điểm hoặc nhận là giả thuyết trước mọi dữ liệu |
| P0 · 18:00–18:45 | Tạo mẫu có seed cố định, Minh và Khánh gắn nhãn độc lập cùng 30 dòng, giải quyết bất đồng trước khi làm tiếp | Manifest ID + tầng mẫu lưu riêng; số đồng thuận/30 trước hòa giải và lý do bất đồng. Sau pilot ước lượng lại khối lượng có thể làm xong |
| P0 · 18:45–19:15 | Ghi tiến độ thật và bàn giao cho Vinh/Khánh | `data-mining.md`: số đã gắn nhãn, x/N tạm và giới hạn; `summary.md`: trạng thái form/lịch hẹn. Review bàn giao có ID, ngày, nguồn và trích ngắn đã kiểm. Với ≥10 câu thử ở #8, cần ≥4 câu có nguồn thật/người dùng; Khánh kiểm cách đếm cuối cùng |
| CP2 · trước 19:30 27/11 | Đối chiếu checklist #5, báo Vinh phần xong và phần còn thiếu để tổng hợp #10 | Có cách đếm đã viết, form thực sự đã gửi, lịch thực sự đã hẹn, gắn nhãn đã bắt đầu. Chỉ đánh dấu các mục có bằng chứng thực hiện |
| P1 · tối 27/11 | Hoàn tất gắn nhãn theo năng lực sau pilot; thực hiện phỏng vấn đúng người dùng | `data-mining.md` có script đếm chạy lại được, x/N, ≥5 ví dụ có nguồn. `interviews/P*.md` chỉ tạo kết quả sau buổi hỏi thật; không tự điền câu trả lời |
| P1 · 28/11, 08:00–09:15 | Chốt khảo sát, lọc người trong nhóm/sai đối tượng/trùng, tổng hợp nguồn đạt ngưỡng | Khảo sát chỉ được ghi đạt nếu ≥20 người hợp lệ; phỏng vấn đạt nếu ≥3 người ngoài nhóm đúng vai người dùng. Lưu log đã ẩn danh, phân biệt số tuyển/số hợp lệ |
| P1 · 09:15–09:45 | Viết kết luận và bàn giao trước CP3 10:00 | `summary.md`: ≥1 nguồn đạt ngưỡng, số chính có mẫu số, ≥5 trích dẫn/ví dụ đã kiểm, giới hạn, giả thuyết đúng/sai/phải đổi. Vinh cập nhật spec/canvas; Khánh nhận nguồn benchmark và tần suất dùng thực tế cho chi phí |
| P2 · 28/11, 10:00–13:00 | Nếu bản chạy thử sẵn sàng, mời 2–3 người ngoài nhóm dùng thử | `validation/log.md` có nhiệm vụ, hành vi quan sát và trích dẫn thật; không thay thế bằng chứng pain. Bàn giao lỗi trước demo 14:30 |
| P2 · sau demo, trước 23:59 28/11 | Ghi reflection cá nhân và thay đổi theo góp ý | `reflection/NguyenNhatMinh.md`; phối hợp ghi thay đổi sau CP2 vào `spec.md` §10 |

### Cách đếm cần chốt trước khi làm

1. Ưu tiên lấy 300 review ngẫu nhiên từ snapshot đầy đủ làm mẫu nền; sau đó lấy tối đa 500 review có từ khóa chưa nằm trong mẫu nền để tìm tình huống. Nếu không đủ 500 thì lấy tất cả dòng phù hợp và ghi số thực tế. Chốt seed, điều kiện lọc, thứ tự và ID trước khi gắn nhãn.
2. Báo riêng x/N từng tầng. Không lấy tỷ lệ trên mẫu gộp ưu tiên từ khóa để suy ra tỷ lệ toàn bộ 5000 review hoặc tỷ lệ người dùng bị lừa. Review là đơn vị đếm; nhắc lừa đảo bằng từ khóa không đồng nghĩa đã mất cọc.
3. Nhãn `bi_lua_coc` chỉ nhận khi người viết kể đã chuyển cọc/tiền và sau đó bị chặn hoặc không nhận hàng; cảnh báo chung, chuyện nghe kể mơ hồ hoặc chưa chuyển tiền không được tự gán cùng nhãn. Lưu câu làm căn cứ và lý do bất định.
4. Với phỏng vấn, kế hoạch cũ 2 người mua + 1 người bán chỉ có 2 người cùng vai người dùng chính. Để đạt ngưỡng 3 người đúng vai, tuyển ≥3 người mua điện thoại cũ ngoài nhóm; người bán là nguồn bổ sung và đếm riêng.
5. Khảo sát bổ sung số lần kiểm người bán trong 30 ngày và phút kiểm ở lần gần nhất; phân biệt trải nghiệm bản thân với chuyện người quen. Không dùng tỷ lệ review làm xác suất lừa đảo trong công thức impact. Không đủ mẫu thì báo thiếu, ưu tiên nguồn đào data đạt ngưỡng và giữ giới hạn.

### Điều kiện đóng phần việc

- #5: kiểm được cả 4 mục trong issue; Vinh có tiến độ thực tế trước CP2.
- CP3: có ít nhất một nguồn đạt ngưỡng, kết quả truy được về nguồn, ≥5 ví dụ/trích dẫn và kết luận trong `summary.md`. Không bắt buộc biến cả ba nguồn thành đạt nếu không đủ dữ liệu thật.
- Commit chỉ chứa tài liệu tổng hợp, công cụ và ví dụ ngắn đã ẩn danh; không chứa file raw, thông tin liên hệ, tên người trả lời. Đối chiếu staged diff trước khi push; mọi số chưa có nguồn phải ghi chưa kiểm hoặc tự ước tính đúng loại.

---

> Đề xuất chi tiết: [de-xuat-do-cu.md](de-xuat-do-cu.md). Plan này chia việc theo 4 checkpoint. Giả định nhóm 4 người: **A** (đội trưởng, sản phẩm), **B** (bằng chứng), **C** (code), **D** (eval và chi phí). Nhóm 3 người thì gộp việc của B và D.

**Lát cắt:** *Một người mua điện thoại cũ · dán tin đăng và đoạn chat với người bán · AI quyết định "tương đối an toàn / cần kiểm thêm / có dấu hiệu lừa đảo", kèm lý do và bước kiểm · người mua không chuyển cọc cho người bán giả, không bỏ oan người bán thật.*

## Đã có
- [x] 5000 review Chợ Tốt (`evidence/raw-chotot_reviews.csv`, không commit) và script `evidence/scrape_chotot.py`
- [x] Đếm thô: 190/5000 (3,8%) nhắc lừa đảo · 2026: 46/770 (6,0%) · 5 trích dẫn nguyên văn
- [x] Cảnh báo công khai của công an năm 2026 (link trong đề xuất)
- [x] Thiết kế workflow 5 bước, luật cứng, chuẩn "đạt", 12 tình huống khó

---

## Chặng 1 · Ngay bây giờ → CP1 17:00 Thứ Sáu 27/11 (3đ)

| Việc | Ai | Ra file |
|---|---|---|
| Tạo repo công khai `K5-Day15-L3B-<TenNhom>`, chép nội dung `starter-repo/` vào gốc repo, mời thành viên | A | repo |
| Điền `TEAMS.md` đúng format, đội trưởng ở dòng 1, chạy `python run.py check` | A | `TEAMS.md` |
| Điền `canvas.md` đủ 7 dòng (lấy câu ở §0 đề xuất) | A | `canvas.md` |
| **Gửi khảo sát 7 câu** (Google Form) lên Discord lớp và nhóm bạn, mục tiêu ≥25 người | B | link form |
| Hẹn 3 người phỏng vấn: 2 người hay mua đồ cũ, 1 người hay bán | B | lịch hẹn |
| Hỏi lab coach: hướng này tính Track D được không (giáp Track E) | A | — |

**Nộp CP1:** TEAMS.md · Track D + bài toán 1–2 câu (không chữ AI) · lát cắt 1 câu · canvas · link repo (mở thử bằng cửa sổ ẩn danh).

---

## Chặng 2 · 17:00 → CP2 19:30 Thứ Sáu 27/11 (4đ)

| Việc | Ai | Ra file |
|---|---|---|
| Viết định nghĩa nhãn `bi_lua_coc` và cách chọn mẫu (khoảng 500 review có từ khoá + 300 review ngẫu nhiên) **trước khi đếm** | B | `evidence/data-mining.md` |
| Bắt đầu gắn nhãn tay, cho 2 người cùng chấm 30 dòng để kiểm độ khớp | B, D | cột `nhan_tay` |
| Viết `spec.md` §0–§4, có sơ đồ workflow (Mermaid) | A | `spec.md` |
| Dựng data "Chợ Mẫu" có seed: giá tham chiếu, tin đăng, người bán, TK cảnh báo, ~30 đoạn chat | C | `data/*.csv`, `data/chat/` |
| Viết 4 công cụ + luồng 5 bước, chạy được với AI giả | C | `codebase/tools.py`, `agent.py` |
| Viết ≥10 câu thử đầu tiên (có ≥3 câu lấy từ review, `source = data_that: chotot Cxxxx`) | D | `eval/benchmark.csv` |
| Viết `metric_spec.yaml` (6 metric trong đề xuất §5) và `DATA_CARD.md` bản đầu | D | `eval/`, `data/` |
| **Chốt chuẩn "đạt"** trong `spec.md` §7 (từ đây không được sửa) | A + D | `spec.md` §7 |

**Chuẩn "đạt" đề xuất chốt:** *Đạt khi ≥75% câu đúng mức, **và** 0 ca lừa bị báo "tương đối an toàn", **và** ≤1/8 ca người bán thật bị báo lừa, **và** 100% số liệu trong lý do khớp công cụ.*

**Nộp CP2:** canvas cập nhật + dòng "đã đổi gì" · tiến độ bằng chứng · link `spec.md` có sơ đồ · link benchmark ≥10 câu · metric_spec + DATA_CARD · chuẩn "đạt" · `python run.py` chạy hết luồng với AI giả.

---

## Chặng 3 · Tối Thứ Sáu → CP3 10:00 Thứ Bảy 28/11 (4đ)

| Việc | Ai | Ra file |
|---|---|---|
| Nối model thật (`.env` + `codebase/ai.py`), `python run.py eval --try` thấy token > 0. **Nên xong trước khi ngủ** | C | `codebase/ai.py` |
| Gắn nhãn tay xong, đếm x/N và %, chọn ≥5 trích dẫn | B | `evidence/data-mining.md` |
| Đóng khảo sát (≥20 người ngoài nhóm), tổng hợp số. Ghi 3 file phỏng vấn | B | `evidence/survey/`, `evidence/interviews/P1–P3.md` |
| Viết `evidence/summary.md`: số chính + kết luận giả thuyết đúng, sai hay phải đổi | B | `evidence/summary.md` |
| Đủ **20–30 câu thử**: ≥5 `kho`, ≥2 `tu_choi`, ≥1/3 `data_that` hoặc `nguoi_dung` | D | `eval/benchmark.csv` |
| Chạy **lượt 1** (`python run.py eval`), chấm cột `pass` theo metric, `python run.py score` | D | `eval/run-1.csv` |
| Thử mô phỏng chi phí 10 phiên (`python run.py simulate --try`) | D | `cost/simulate-try.csv` |
| Quay **video 30 giây** bản chạy thử gọi AI thật, đưa lên YouTube "Không công khai" | C | link video |
| Hoàn thiện `spec.md` §0–§7, điền bảng impact §2 (có hướng người bán bị loại, số từ cùng bộ review) | A | `spec.md` |

**Nộp CP3:** bằng chứng đạt ngưỡng + ≥5 trích dẫn · bộ câu thử 20–30 câu · video 30 giây · kết quả lượt 1 (x/N) + run ID · `spec.md` §0–§7.

---

## Chặng 4 · 10:00 → CP4 14:30 Thứ Bảy 28/11 (4đ)

| Việc | Ai | Ra file |
|---|---|---|
| Đọc trace các câu trượt ở lượt 1, sửa prompt hoặc luật. **Ghi mỗi thay đổi vào `spec.md` §10** | C | `codebase/`, `spec.md` §10 |
| Chạy **lượt 2**, chấm, so sánh lượt 1 → lượt 2 | D | `eval/run-2.csv`, `eval/report.md` |
| Điền `cost/personas.yaml` (số lần dùng/tháng từ khảo sát, giá 2 model từ `further-reading/model-prices.csv`), chạy `python run.py simulate` (≥50 phiên) | D | `cost/simulate-N.csv`, `cost/cost-estimate.md` |
| *Bonus:* 2–3 người ngoài nhóm dùng thử, ghi log | B | `validation/log.md` |
| Làm slide → `demo-slides.pdf` ở gốc repo: có trang "Đánh giá thế nào" và "Chi phí khi dùng thật". Quay video demo dự phòng | A | `demo-slides.pdf` |

**Nộp CP4:** phòng demo + repo · tích 7 hạng mục · lượt 1 → lượt 2 · chi phí / task thành công + tên model · slide PDF + video dự phòng.

---

## Sau demo → 23:59 Thứ Bảy 28/11
- Sửa theo góp ý, ghi mọi thay đổi vào `spec.md` §10. **Không** sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy.
- Mỗi người một file `reflection/<ten>.md`.

---

## Luật phải nhớ
- **Không commit:** `.env`, API key, `evidence/raw-*.csv` (toàn văn review). Repo chỉ chứa bảng đếm và trích dẫn ≤2 câu mỗi review, không tên người viết.
- Data chạy thử dùng tên và số dựng. Không dùng chat, số tài khoản, số điện thoại thật.
- Người trong nhóm không tính là bằng chứng.
- Kết quả thấp mà trung thực vẫn được đủ điểm. Sửa số hoặc đổi chuẩn "đạt" sau CP2 thì phần đó 0 điểm.

## Rủi ro và phương án dự phòng
| Rủi ro | Dự phòng |
|---|---|
| Khảo sát không đủ 20 người trước CP3 | Bằng chứng chính chuyển sang đào review (gắn nhãn tay đạt ngưỡng x/N). Phỏng vấn 3 người làm nguồn kiểm lại |
| Lab coach nói hướng này thuộc Track E | Báo đổi track trước CP2 (luật cho phép), giữ nguyên thiết kế |
| Gói model miễn phí hết lượt | Thêm `--wait 4` khi chạy eval và simulate, hoặc đổi model rẻ hơn, ghi vào §10 |
| AI báo oan nhiều ca người bán thật | Thêm câu thử "rẻ vì máy xấu" vào lượt 2, chỉnh luật vàng/đỏ, ghi §10 |
