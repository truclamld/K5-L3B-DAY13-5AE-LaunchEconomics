# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 5AE · Lớp: L3B · Phạm vi đề xuất: chỉ `noi_dia` + `hang_nang` (982/1.200 yêu cầu của đợt chạy thử)

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu, gấp 16,3 lần hoá đơn token và tool chia số yêu cầu (274,7 đ); trong phạm vi 3.414 đ, cộng chi phí cố định 4.599 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Gấp đôi số ca làm lại +51,77%; gấp đôi tỉ lệ xem lại +40,70%; lương tăng 25% +23,12%. Giá token gấp đôi chỉ +5,62% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Trong phạm vi 4.599 đ = 0,38× của 12.000 đ (0,48× nếu khối lượng còn một nửa); xem lại 100%: 0,98×; `quoc_te` 1,88× nên loại khỏi phạm vi [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại trong 7 ngày 4,25% (51/1.200); 15 event có `trace_id` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 19/20 = 95%; 5 ca khắc phục đủ năm loại; nặng nhất là báo "đã hoàn" khi sổ cái lỗi 503 (ca 7) và hoàn trùng (ca 20) | Xong, có bằng chứng | Kỹ sư backend |
| 6 · Pilot plan | Chia ngẫu nhiên 20 + 20 nhân viên, phân tầng theo depot; mức chênh 6 điểm (859 hiệu dụng, từ 299 yêu cầu mỗi người); power chỉ 0,64 nếu tác động thật là 5 điểm; 4 luật dừng; quyết định ngày 2027-01-12 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,77%); xem lại 100%: 11.743 đ (0,98×); khối lượng còn một nửa: chi phí cố định 2.370 đ mỗi việc [simulated] | Giả lập | PM trợ lý hoàn phí |

Con số bất lợi: `hang_nang` có tỉ lệ mở lại 8,23% (13/158), cao hơn trần 6% của luật an toàn, và làm lại 11,39% (18/158); xem lại 100% gần như mất hết lợi thế chi phí (0,98×) [simulated]; power 0,64 ở mức 5 điểm.

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang` theo `pilot_plan.yaml`, bắt đầu 2026-12-07.

- Chỉ báo "đã hoàn" sau khi sổ cái ghi ok (ca 7) và bật khoá chống trùng theo `idempotency_key` (ca 20), kiểm thử trên 20 trace mẫu · Kỹ sư backend · 2026-12-04.
- Ký chấp nhận mức chênh 6 điểm, tức power 0,64 nếu tác động thật chỉ 5 điểm · Giám đốc vận hành LogiX-VN · 2026-12-04.
- Bật đủ event có `trace_id` trong `chi_so.md` và nối thử được với trace của 1 ngày chạy thử · Kỹ sư trưởng agent · 2026-12-04.
- Thay phút xem lại, làm lại simulated bằng phút đo thật sau tuần 1, tính lại chi phí mỗi việc thành công · PM trợ lý hoàn phí · 2026-12-14.
- Giảm xem lại theo bậc xuống dưới 50% yêu cầu cuối bước 0.25, vì xem lại 100% chỉ còn 0,98× (B4) · Trưởng nhóm CSKH · 2026-12-21.
- Theo dõi riêng mở lại của `hang_nang`; nếu nhóm trợ lý vẫn trên 6% cuối bước 0.25 thì thu hẹp về `noi_dia` · PM trợ lý hoàn phí · 2026-12-21.
