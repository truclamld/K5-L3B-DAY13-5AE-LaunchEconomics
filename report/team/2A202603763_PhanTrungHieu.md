# Báo cáo cá nhân — PhanTrungHieu-2A202603763

## 1. Thông tin thành viên

- Họ tên: Phan Trung Hiếu
- MSSV: 2A202603763
- Email: 26ai.hiept3@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

Nhiệm vụ E: đặc tả chỉ số, danh sách event và rủi ro kinh tế trong `report/team/chi_so.md`; tổng hợp `report/team/ho_so_launch_v0.md` và `report/team/group_report.md`. Ở nhiệm vụ C, gắn bộ nhãn thứ hai cho 20 ca lỗi, độc lập với người gắn nhãn 1.

## 3. Đóng góp cụ thể

- Gắn nhãn 20 ca theo năm loại Google PAIR, không trao đổi, commit trước khi so. Đồng thuận với người gắn nhãn 1 là 19/20 = 95%, chỉ lệch ca 8 (tôi: Hệ thống, người 1: Ngữ cảnh). Khi gộp, phát hiện ca 13 và 15 của tôi bị chép sai và tỉ lệ ghi 17/20; đã sửa lại theo commit gốc.
- E1: tính thử chỉ số trong đợt chạy thử: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200); trong phạm vi `noi_dia` + `hang_nang` mở lại là 3,97% (39/982). Đề xuất thêm một chỉ số dùng (% nhân viên nhóm trợ lý dùng trợ lý mỗi tuần) và một chỉ số an toàn (% đơn hoàn sai tiền qua kiểm tra mẫu).
- Danh sách 15 event có `trace_id` (10 event chính và 5 event cho bảng khắc phục); kiểm tra chéo để mỗi chỉ số đều tính được từ event.
- E2: ba dòng rủi ro kinh tế lấy số từ `bang_chi_phi.md`: làm lại gấp đôi +51,77%, xem lại 100% còn 0,98×, khối lượng còn một nửa thì chi phí cố định 2.370 đ mỗi việc [simulated]; mỗi dòng có dấu hiệu theo dõi so với tỉ lệ đợt chạy thử.
- Hồ sơ launch v0: bảy mục, nêu con số bất lợi (`hang_nang` mở lại 8,23%, xem lại 100% còn 0,98× [simulated], power 0,64 ở 5 điểm); đề xuất Go có điều kiện với 6 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra.
- Rà phần của cả nhóm trước khi nộp: chạy `python lab13.py` trên máy khác (A1 in `ĐẠT`, số khớp `bang_chi_phi.md`), kiểm tra `pilot_plan.yaml` bằng `yaml.safe_load` và 4 luật dừng đủ bốn vế.

## 4. Bằng chứng

- Commit `2969d36`: bộ nhãn người 2 cho 20 ca trong `report/team/bang_loi.md`.
- Commit `ca2af57` (PR #2): E1, danh sách event và kiểm tra chéo trong `report/team/chi_so.md`.
- Nhánh `nhiem-vu-E-Hieu-ho-so`: sửa lại nhãn người 2 ở ca 13 và 15 trong `bang_loi.md`, E2 và event cho bảng khắc phục trong `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`.

## 5. Công cụ AI đã dùng

- Claude Code: viết đoạn Python (thư viện `csv`) để đếm các chỉ số E1 và tỉ lệ đợt chạy thử dùng trong E2, soạn câu chữ cho `chi_so.md`, hồ sơ và báo cáo nhóm, so hai bộ nhãn với commit gốc, thao tác git và mở PR.
- Không dùng AI để gắn nhãn: 20 nhãn người 2 do tôi tự gắn, đúng quy định trong `RULES.md`.
- Tự kiểm tra: ba chỉ số E1 khớp số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; mọi số E2 và hồ sơ đối chiếu lại với `bang_chi_phi.md` và `pilot_plan.yaml`; tìm từ "production" trong `report/team` không còn kết quả.

## 6. Tự đánh giá

Hoàn thành phần E và bộ nhãn người 2. Điều học được: chỉ số trong đợt chạy thử chưa nói được trợ lý tốt hơn vì chưa có đối chứng, và con số bất lợi phải nằm ngay trên trang hồ sơ. Cần làm tốt hơn: kiểm tra bản gộp của người khác ngay sau khi merge, vì lỗi chép nhãn ở ca 13 và 15 chỉ được phát hiện sau đó.
