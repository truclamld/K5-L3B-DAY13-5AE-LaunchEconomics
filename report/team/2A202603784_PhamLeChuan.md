# Báo cáo cá nhân — Phạm Lê Chuẩn (2A202603784)

## 1. Thông tin thành viên

- Họ tên: Phạm Lê Chuẩn
- MSSV: 2A202603784
- Email: 26ai.chuanpl@vinuni.edu.vn
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

- Phụ trách vai người viết code; phối hợp hoàn thiện `src/lab13.py` cho mô hình chi phí, chi phí cố định A4 và phân tích độ nhạy/giới hạn chạy lại B.
- Theo dõi tính đầy đủ của `report/team/bang_chi_phi.md`, nhất là các mục A4 và B1–B4.

## 3. Đóng góp cụ thể

- Xác định phần cần hoàn thiện là A4 và B; rà soát báo cáo, phát hiện các bảng còn dấu `...` và yêu cầu hoàn thiện các mục còn thiếu.
- Phối hợp dùng ChatGPT/Codex để triển khai phép tính A4, các kịch bản độ nhạy, giới hạn 1–3 lần chạy và kịch bản xem lại 100%; rà lại phần trình bày và giả định trong báo cáo.
- Kết quả chính: giới hạn chạy 2 lần có tổng chi phí hệ thống thấp nhất, khoảng 6,901 triệu đồng; giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất, khoảng 4.111 đồng.

## 4. Bằng chứng

- `src/lab13.py`: mô hình chi phí, tính A4 và các kịch bản B1–B4.
- `report/team/bang_chi_phi.md`: bảng chi phí cố định A4, độ nhạy B1–B2, giới hạn chạy lại B3 và kịch bản xem lại 100% B4.
- Chi phí ở B4 dùng giả định thời gian xem lại/làm lại; các số dựa trên phút `*_simulated` được ghi nhãn simulated trong báo cáo.
- Đã chạy `python lab13.py` sau khi cài dependencies: chương trình chạy hết, ba phép thử A1 đều ĐẠT; đầu ra A4/B được đối chiếu với bảng chi phí.

## 5. Công cụ AI đã dùng

- Dùng ChatGPT/Codex để hỗ trợ viết và chỉnh sửa mã, tính các kịch bản, rà soát báo cáo và hoàn thiện nội dung theo cấu trúc lab.
- Đã yêu cầu làm rõ các phần còn thiếu và xử lý lỗi thiếu `pandas`; xác nhận chương trình chạy hết sau khi cài dependencies.

## 6. Tự đánh giá

Đã chủ động theo dõi tiến độ phần A4/B, phát hiện nội dung còn thiếu và phối hợp dùng AI để hoàn thiện mã cùng báo cáo. Đã chạy chương trình và kiểm tra A1 cùng các đầu ra A4/B trước khi cập nhật nhánh nộp.
