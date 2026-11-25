# Team

## Thông tin nhóm

- Tên nhóm: 5AE
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-5AE-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/truclamld/K5-L3B-DAY13-5AE-LaunchEconomics
- Nhánh nộp: `main`
- Commit chốt: 

## Thành viên

| STT | Họ tên          | MSSV        | Email                     | GitHub    | Vai trò         |
|----:|-----------------|-------------|---------------------------|-----------|-----------------|
|   1 | Lê Đức Trúc Lâm | 2A202603787 | 26ai.lamldt@vinuni.edu.vn | truclamld | Người viết code |
|   2 | Phạm Lê Chuẩn                 |   2A202603784          | 26ai.chuanpl@vinuni.edu.vn                          | 22520160          | Người viết code                |
|   3 | Ngô Chí Vĩnh    | 2A202603724 | 26ai.vinhnc2@vinuni.edu.vn | NgChiVinh | Người kiểm số; phụ trách Nhiệm vụ D |
|   4 | Hoàng Dương Anh Quân | 2A202603735 | 26ai.quanhda@vinuniversity.edu.vn | HoangQuan23112004 | Người gắn nhãn 1 |
|   5 | Phan Trung Hiếu | 2A202603763 | 26ai.hiept3@vinuni.edu.vn | TrungHieuPh | Người gắn nhãn 2 kiêm giữ hồ sơ; phụ trách Nhiệm vụ E |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## LeDucTrucLam-2A202603787

### Phần việc phụ trách

Phụ trách phần code nhiệm vụ A: hoàn thiện các hàm tính kinh tế chạy lại và mô hình chi phí, phân tích chi phí theo loại yêu cầu và phân bổ chi phí cố định; ghi kết quả vào `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

Hoàn thiện `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` và `mo_hinh`; dùng mô hình để tính A2, tách A3 theo bốn loại yêu cầu và tính A4 cho phạm vi `noi_dia` + `hang_nang`. Ba phép thử A1 đều in `ĐẠT`. Kết quả chính: tổng chi phí 4.373.585 đ, 978 yêu cầu thành công, chi phí 4.472 đ/việc thành công; chi phí cố định làm A4 thành 4.599 đ/việc ở 45.000 yêu cầu/tháng và 5.784 đ ở nửa khối lượng (các kết quả có phần phút nhân viên được ghi nhãn `simulated`).

### Bằng chứng

Commit `db721d65aafa47245711595d6b2858f00e994c69` có thay đổi ở `src/lab13.py` và `report/team/bang_chi_phi.md`. Đã chạy `python lab13.py`: A1 đạt; kết quả A2–A4 khớp số đối chiếu trong hướng dẫn lab. Báo cáo chi phí nằm trong `report/team/bang_chi_phi.md`.


## PhamLeChuan-2A202603784

### Phần việc phụ trách

- Người viết code: phụ trách `src/lab13.py`; tập trung hoàn thiện tính chi phí cố định A4 và phân tích độ nhạy, giới hạn chạy lại ở nhiệm vụ B.

### Đóng góp cụ thể

- Hoàn thiện mô hình tính chi phí theo trace và các kịch bản B1–B4; phối hợp dùng ChatGPT/Codex để triển khai phép tính, rồi rà soát kết quả và các giả định trong báo cáo.
- Hoàn thiện bảng A4 cho phạm vi `noi_dia` + `hang_nang`, gồm mức 45.000 và 22.500 yêu cầu/tháng; rà soát để báo cáo không còn phần mẫu B1–B4 bị lặp.
- Đối chiếu chi phí giới hạn chạy lại 1/2/3 lần; ghi nhận giới hạn 2 lần có tổng chi phí hệ thống thấp nhất, khoảng 6,901 triệu đồng.

### Bằng chứng

- `src/lab13.py`: các phép tính A4, B1, B3, B4 và kịch bản kết hợp B2.
- `report/team/bang_chi_phi.md`: bảng A4, B1–B4 và kết luận về giới hạn 2 lần.
- Các phép tính có thành phần phút `*_simulated`; cần chạy lại `python lab13.py` với đủ thư viện và kiểm tra đầu ra trước khi nộp.

## NgoChiVinh-2A202603724

### Phần việc phụ trách

- Nhiệm vụ D (CP4): cỡ mẫu D1 trong `src/lab13.py` và `report/team/pilot_plan.yaml`.
- Người kiểm số: tính tay một con số của Nhiệm vụ A để đối chiếu với code.

### Đóng góp cụ thể

- Viết phần D1 trong `src/lab13.py`: hàm `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `m_toi_thieu`, `nhiem_vu_d`.
  - In năm câu D1: 1.251 · 3.103 (42 người mỗi nhóm) · 1.000 · 300 · m ≥ 299.
  - In power 0,64 khi chọn mức chênh 6 điểm.
  - In tỉ lệ mở lại hiện tại: 4,25% toàn mẫu, 3,97% trong phạm vi.
- Điền `pilot_plan.yaml`: chia theo nhân viên 20 + 20, mde 0,06, n 859, DE 6,96; trả lời 5 câu D2; ghi rõ đánh đổi đã chấp nhận.
- Viết 4 luật dừng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ: an toàn (mở lại), an toàn (hoàn trùng / sổ cái), chi phí, mức độ sử dụng.
- Kiểm số Nhiệm vụ A: tính tay từ tổng các cột CSV. Token 245.585 đ; tool 84.000 đ; phần lần chạy 2–3 là 93.804 đ; tổng 4.373.585 đ (simulated); chi phí mỗi việc thành công 4.373.585 ÷ 978 = 4.472 đ (simulated); hoá đơn chia số yêu cầu 274,7 đ. Cả sáu số khớp code của Lâm.
- Đối chiếu số A3, A4 trong `pilot_plan.yaml` với output code A của Lâm: khớp.
- Kiểm tra chéo luật dừng với nhãn ca 7, 20 trong `bang_loi.md` và danh sách event trong `chi_so.md`.

### Bằng chứng

- Commit `615f021` trên nhánh `nhiem-vu-D-Vinh`; PR #4.
- `python lab13.py` chạy từ đầu đến cuối, in phần D1 ở cuối.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?` ngoài dòng chú thích.
- Báo cáo cá nhân: `report/team/2A202603724_NgoChiVinh.md`.

## PhanTrungHieu-2A202603763

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ: gắn nhãn 20 ca lỗi độc lập ở Nhiệm vụ C.
- Nhiệm vụ E: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, tổng hợp `report/team/group_report.md`.

### Đóng góp cụ thể

- Bộ nhãn người 2 cho 20 ca; đồng thuận 19/20 = 95%, chỉ lệch ca 8. Sửa lại ca 13 và 15 bị chép sai khi gộp, theo commit gốc `2969d36`.
- E1: chỉ số trong đợt chạy thử là chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200); thêm một chỉ số dùng và một chỉ số an toàn tự đề xuất.
- 15 event có `trace_id` và kiểm tra chéo từng chỉ số; E2 ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy [simulated].
- Hồ sơ launch v0 đủ bảy mục, nêu con số bất lợi; đề xuất Go có điều kiện với 6 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra.
- Chạy lại `python lab13.py` trên máy khác trong nhóm: A1 in `ĐẠT`, số khớp `bang_chi_phi.md`; `pilot_plan.yaml` đọc được bằng `yaml.safe_load`.

### Bằng chứng

- Commit `2969d36` (nhãn người 2), `ca2af57` (E1 và event, PR #2); nhánh `nhiem-vu-E-Hieu-ho-so` (E2, hồ sơ, báo cáo nhóm).
- Báo cáo cá nhân: `report/team/2A202603763_PhanTrungHieu.md`.

## Hoàng Dương Anh Quân — 2A202603735

### Phần việc phụ trách

- Nhiệm vụ C (CP3), vai trò người gắn nhãn 1 cho bộ 20 ca lỗi của trợ lý hoàn phí.

### Đóng góp cụ thể

- Đối chiếu nhãn lần 1 với bộ nhãn của Hiếu, ghi nhận 19/20 ca trùng (95%) theo bộ nhãn gốc của Hiếu và giải thích nhãn thống nhất cho ca 8.
- Đề xuất cách phát hiện, biện pháp khắc phục và vai trò phụ trách cho 5 ca đại diện thuộc 5 loại lỗi.

### Bằng chứng
- Commit `171a113` (bảng đối chiếu và biện pháp khắc phục trong `report/team/bang_loi.md`, PR #3), `a2c7526` (đồng bộ kết quả 19/20 ca, PR #10); nhánh `nhiem-vu-C-quan`.
- Báo cáo cá nhân: `report/team/2A202603735_HoangDuongAnhQuan.md`.
