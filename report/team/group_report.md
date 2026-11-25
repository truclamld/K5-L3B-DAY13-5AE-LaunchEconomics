# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: 5AE
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Mục tiêu: lập hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có cho chạy pilot hay không. Hồ sơ trả lời bốn câu: mỗi việc thành công tốn bao nhiêu, rẻ hơn nhân viên tự làm không, trợ lý sai kiểu gì, và pilot phải thiết kế ra sao để ra được quyết định.

Dữ liệu: 1.200 yêu cầu (`src/logix_requests.csv`) và 1.624 lần chạy (`src/logix_runs.csv`) của đợt chạy thử, đều là dữ liệu giả lập; phút xem lại và làm lại lấy từ cột `_simulated`. Mỗi thành viên làm trên nhánh riêng (`nhiem-vu-X-Ten`) rồi mở PR vào `main`; mỗi PR có một người khác đọc lại.

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md), [lab13.py](../../src/lab13.py)): cộng token, tool của mọi lần chạy kể cả lần lỗi, cộng tiền xem lại và làm lại, chia cho 978 việc thành công; tách theo loại yêu cầu; cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`.
- **B · Độ nhạy và giới hạn chạy lại** ([bang_chi_phi.md](bang_chi_phi.md)): gấp đôi từng yếu tố một để xếp hạng; so tổng chi phí hệ thống khi giới hạn 1, 2, 3 lần chạy; tính lại khi phải xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn 20 ca độc lập theo năm loại của Google PAIR, so sau, viết quy tắc cho ca lệch; chọn 5 ca, mỗi loại một ca, viết cách phát hiện bằng event và ngưỡng.
- **D · Pilot plan** ([pilot_plan.yaml](pilot_plan.yaml)): chia ngẫu nhiên theo nhân viên (20 + 20, phân tầng theo depot) thay vì theo depot, tính cỡ mẫu hiệu dụng với ICC 0,02, viết 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): tính thử chỉ số chính, dùng, an toàn; 15 event có `trace_id`, kiểm tra chéo từng chỉ số tính được từ event; 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy; gom bảy mục vào một trang.

## 4. Kết quả

- Chi phí mỗi việc thành công: 4.472 đ, gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ) [simulated].
- Trong phạm vi `noi_dia` + `hang_nang`, đã cộng chi phí cố định: 4.599 đ = 0,38× của 12.000 đ khi nhân viên tự làm [simulated]; `quoc_te` 1,88× nên loại khỏi pilot.
- Yếu tố nhạy nhất là làm lại (+51,77% khi gấp đôi), rồi xem lại (+40,70%); giá token gấp đôi chỉ +5,62% [simulated]. Giới hạn 2 lần chạy cho tổng chi phí hệ thống thấp nhất: 6,90 triệu đ [simulated].
- Chỉ số trong đợt chạy thử là: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại trong 7 ngày 4,25% (51/1.200).
- Đồng thuận gắn nhãn ban đầu 19/20 = 95%.
- Pilot: mức chênh phát hiện được 6 điểm (859 hiệu dụng mỗi nhóm); power 0,64 nếu tác động thật chỉ 5 điểm.
- Con số bất lợi: xem lại 100% còn 0,98× (11.743 đ) [simulated]; `hang_nang` mở lại 8,23% (13/158), cao hơn trần 6%.
- **Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, 6 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra (xem [ho_so_launch_v0.md](ho_so_launch_v0.md)).
- Kết quả duyệt chéo từ hội đồng: điền sau phiên 17:25.

## 5. Khó khăn và cách xử lý

- Một số máy trong nhóm thiếu `pandas` nên chưa chạy được `lab13.py`: người viết code chạy trên máy đã cài đủ thư viện (ba phép thử A1 in `ĐẠT`); số E1 được đếm lại bằng thư viện `csv` chuẩn và khớp số đối chiếu trong hướng dẫn.
- Bản gộp đầu tiên của `bang_loi.md` chép sai nhãn người 2 ở ca 13 và 15 và ghi đồng thuận 17/20: đối chiếu lại với commit `2969d36` (nhãn người 2 commit trước khi so), sửa về 19/20, chỉ lệch ca 8. Không đổi nhãn sau khi đã so.
- Mức chênh 5 điểm cần 1.251 mỗi nhóm, vượt trần 1.000 khi chỉ có 20 + 20 nhân viên: nhóm chấp nhận mức 6 điểm, ghi rõ power 0,64 ở 5 điểm và để Giám đốc vận hành ký chấp nhận.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

- **Lê Đức Trúc Lâm (2A202603787) — Người viết code:** ba hàm A1 và `mo_hinh` trong `src/lab13.py` (ba phép thử A1 in `ĐẠT`); A2, A3 theo bốn loại yêu cầu và A4 trong `bang_chi_phi.md`.
- **Phạm Lê Chuẩn (2A202603784) — Người viết code:** phụ trách hoàn thiện mô hình chi phí trong `src/lab13.py`, phần chi phí cố định A4 và các kịch bản độ nhạy/giới hạn chạy lại B; phối hợp dùng ChatGPT/Codex và rà soát các kết quả trong `report/team/bang_chi_phi.md`. Chương trình cần được chạy lại với đủ thư viện trước khi nộp.
- **Hoàng Dương Anh Quân (2A202603735) — Người gắn nhãn 1:** gắn nhãn 20 ca độc lập, bảng so nhãn và bảng khắc phục 5 ca trong `bang_loi.md`.
- **Ngô Chí Vĩnh (2A202603724) — Người kiểm số:** D1 cỡ mẫu và `pilot_plan.yaml` (cách chia, luật dừng, ngày quyết định).
- **Phan Trung Hiếu (2A202603763) — Người gắn nhãn 2 kiêm giữ hồ sơ:** gắn nhãn 20 ca độc lập (commit `2969d36`); E1, E2 và danh sách event trong `chi_so.md`; `ho_so_launch_v0.md`; tổng hợp báo cáo nhóm.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập: mọi kết luận chi phí phải tính lại bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chưa nói được trợ lý làm chỉ số tốt hơn hay kém đi; pilot mới tách được tác động.
- ICC 0,02 là giả định; nếu ICC thật cao hơn, cỡ mẫu hiệu dụng giảm và power còn thấp hơn 0,64 ở mức 5 điểm.
- `quoc_te` và `doi_tac` chưa được đánh giá trong pilot; `hang_nang` có tỉ lệ mở lại 8,23% nên cần theo dõi riêng.
- 20 ca lỗi chỉ là mẫu nhỏ; cần gắn nhãn thêm trace thật từ tuần đầu pilot để kiểm tra lại quy tắc ca 8.

## 8. Tài liệu tham khảo

- Đề bài Lab 13, Hướng dẫn học viên Ngày 13 và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Erol và cộng sự (2025), *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*: chương Errors + Graceful Failure.
- statsmodels, `NormalIndPower` (tính power cho hai tỉ lệ).
