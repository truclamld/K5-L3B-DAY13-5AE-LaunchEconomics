# Báo cáo cá nhân — 2A202603787_LeDucTrucLam

## 1. Thông tin thành viên

- Họ tên: Lê Đức Trúc Lâm
- MSSV: 2A202603787
- Email: 26ai.lamldt@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code

## 2. Phần việc phụ trách

Phụ trách phần code nhiệm vụ A: hoàn thiện các hàm tính kinh tế chạy lại và mô hình chi phí, phân tích chi phí theo loại yêu cầu và phân bổ chi phí cố định; ghi kết quả vào `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

Hoàn thiện `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` và `mo_hinh`; dùng mô hình để tính A2, tách A3 theo bốn loại yêu cầu và tính A4 cho phạm vi `noi_dia` + `hang_nang`. Ba phép thử A1 đều in `ĐẠT`. Kết quả chính: tổng chi phí 4.373.585 đ, 978 yêu cầu thành công, chi phí 4.472 đ/việc thành công; chi phí cố định làm A4 thành 4.599 đ/việc ở 45.000 yêu cầu/tháng và 5.784 đ ở nửa khối lượng (các kết quả có phần phút nhân viên được ghi nhãn `simulated`).

## 4. Bằng chứng

Commit `db721d65aafa47245711595d6b2858f00e994c69` có thay đổi ở `src/lab13.py` và `report/team/bang_chi_phi.md`. Đã chạy `python lab13.py`: A1 đạt; kết quả A2–A4 khớp số đối chiếu trong hướng dẫn lab. Báo cáo chi phí nằm trong `report/team/bang_chi_phi.md`.

## 5. Công cụ AI đã dùng

Dùng Codex để giải thích yêu cầu CP1, rà soát công thức và hỗ trợ hoàn thiện code/báo cáo. Tự chạy `python lab13.py`, xác nhận ba phép thử A1 đạt và đối chiếu các số A2–A4 với hướng dẫn chi tiết của lab. Có tính toán lại các chi phí bằng máy tính Casio dựa trên công thứ trong `Lab13_Huong_dan_chi_tiet_buoi_chieu.md` để đảm bảo tính chính xác của code; các kết quả đối chiếu đều đúng.

## 6. Tự đánh giá

Đã hoàn thành phần A và hiểu được vì sao chi phí phải cộng giờ xem lại/làm lại, tính mọi lần chạy vào tử số nhưng chỉ chia cho yêu cầu thành công. Cần tiếp tục rà soát cách trình bày số liệu `simulated` và phối hợp với nhóm cho các nhiệm vụ tiếp theo.
