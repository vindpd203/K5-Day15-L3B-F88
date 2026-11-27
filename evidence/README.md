# Bộ bằng chứng của Minh · issue #5

Công cụ chỉ dùng thư viện chuẩn khi phân tích file có sẵn; không cần API key.

## Chạy lại

Tại gốc repo:

```powershell
python -X utf8 evidence/count.py count evidence/annotations-codex.csv
python -X utf8 evidence/test_count.py
```

`annotations-codex.csv` chứa 504 mã review, tầng mẫu, nhãn, căn cứ phân loại và nguồn AI, không chứa toàn văn review, ngày, điểm sao hoặc thông tin tác giả. Manifest cùng tên kiểm đủ ID/tầng mẫu. Người review PR có thể tái lập bảng đếm mà không cần file raw. `label-report.json` có hash của bản nhãn công khai và mẫu gốc.

Các lệnh dưới đây dùng khi có snapshot và file làm việc riêng tại máy:

```powershell
python -X utf8 evidence/count.py stats evidence/raw-chotot_reviews.csv
python -X utf8 evidence/count.py sample evidence/raw-chotot_reviews.csv
python -X utf8 evidence/count.py count evidence/private/sample.csv
python -X utf8 evidence/test_count.py
```

Lệnh sample từ chối ghi đè để bảo toàn nhãn đang làm. Muốn kiểm tính tái lập, dùng `--name sample-check` và cùng seed. Mặc định seed 20261127, random 300, keyword tối đa 500; dữ liệu hiện tại chỉ đủ 204 keyword còn lại.

Raw giữ nguyên. `private/sample.json` chứa hash, seed và ID mẫu; `sample.csv` là bản làm việc chính, `sample.pilot.csv` là 30 dòng xuất ban đầu cho chấm độc lập. Tất cả ignored, không commit nguyên nội dung. Khi sửa CSV bằng Excel, lưu CSV UTF-8 và giữ ID.

## Quy trình gắn nhãn

Đọc định nghĩa trong `data-mining.md`. Minh đã xác nhận trong chat rằng nhãn Codex khớp với phần nhãn của mình và yêu cầu ghi vào phần Minh. Đã điền `nhan_minh` cho 504 dòng, căn cứ xác nhận vào `can_cu_minh`, người duyệt cuối `Nguyễn Nhật Minh`, `loai_duyet=human`. `nhan_tay` và mọi giá trị nhãn giữ nguyên. Nhãn hợp lệ: bi_lua_coc, khong_du_bang_chung, khong_lien_quan. Manifest ghi cách xác nhận qua chat và nguồn gợi ý ban đầu Codex.

`private/pilot-minh.csv` có 30 nhãn Minh xác nhận; `private/pilot-khanh.csv` vẫn trống. Chưa có file nhãn riêng của Minh để đối chiếu tự động hoặc hai người chấm độc lập. Không tự điền phần Khánh. Bản trước xác nhận được sao lưu trong private; nhật ký `private/minh-confirmation.json` ghi cơ sở cập nhật theo lời Minh trong chat.

Cột `de_xuat_ai/can_cu_ai` giữ 85 bản nháp ban đầu; không tự tính vào nhãn cuối. Cột labels gốc chỉ là lọc từ khóa. Bản trước sửa: `private/sample.before-codex-final.csv`; nhật ký 504 nhãn và hash nội dung: `private/codex-final-audit.json`. Bản nhãn chỉ có mã/căn cứ để review trong repo: `annotations-codex.csv`; báo cáo tổng hợp chia nguồn AI/người thật: `label-report.json`. Không tự điền kết quả phỏng vấn hoặc khảo sát.

Lệnh count yêu cầu manifest `.json` cùng tên mẫu, kiểm không thêm/bớt ID hoặc đổi tầng/pilot; kiểm nhãn, căn cứ, người duyệt và `loai_duyet`; báo số nhãn theo người duyệt cuối cùng, số nhãn Minh/Khánh và tình trạng pilot. Không có % gộp. Hiện nhãn Minh 504, nhãn Khánh 0; pilot có nhãn Minh 30 nhưng số cặp Minh/Khánh vẫn bằng 0. Xác nhận qua chat không tự tạo kết quả hai người chấm độc lập.

## Thu thập mới chỉ khi cần

Snapshot đã có, không chạy scraper để ghi đè. Nếu sau này cần snapshot khác, sửa OUT sang tên mới, ghi ngày/nguồn/hash riêng và không dùng ID mới thay ID Cxxxx cũ.

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

Gói [google-play-scraper 1.2.7](https://pypi.org/project/google-play-scraper/1.2.7/) chỉ dùng khi lấy dữ liệu mới. Phân tích/count không cần gói này.

## Bàn giao

- Nguồn, số kiểm lại, ví dụ và giới hạn: `data-mining.md`.
- Tổng hợp tiến độ: `summary.md`; checklist còn lại: `issue-5-handoff.md`.
- Form và liên kết: `survey/questions.md`; phỏng vấn tham khảo: `interviews/schedule-reference.md` (lịch đề xuất), `interviews/guide.md` (kịch bản), `interviews/record-reference.md` (phiếu trắng).
- Không stage raw, file nhãn đầy đủ, câu trả lời hoặc liên hệ chưa ẩn danh. `git check-ignore --no-index evidence/raw-chotot_reviews.csv evidence/private/sample.csv` phải in cả hai đường dẫn.
