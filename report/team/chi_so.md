# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % nhân viên nhóm trợ lý dùng trợ lý mỗi tuần | Số `staff_id` nhóm trợ lý có ít nhất 1 `staff_review_decision` trong tuần, chia số nhân viên nhóm trợ lý | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số mẫu có `so_tien_da_hoan` khác `so_tien_dung`, chia số mẫu kế toán kiểm trong tuần (bắt lỗi ngầm mà mở lại không thấy) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

Cách tính: đếm trực tiếp trên `src/logix_requests.csv` theo đúng công thức ở cột 3; ba chỉ số này không dùng cột `_simulated`. Trong phạm vi `noi_dia` + `hang_nang`, tỉ lệ mở lại 7 ngày là 3,97% (39/982), là mức nền để đặt luật an toàn trong `pilot_plan.yaml`.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | Hệ thống ticket | request_id, depot, staff_id, loai, so_tien_vnd, arm (trợ lý / đối chứng), created_at, trace_id | Khi khách gửi yêu cầu hoàn phí |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| handoff_to_staff | Agent | reason, so_lan_chay, tom_tat, trace_id | Khi chạy hết 3 lần vẫn lỗi hoặc thiếu dữ liệu |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| staff_review_decision | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi bấm giữ, sửa hoặc bỏ |
| staff_rework_completed | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi ticket đóng |
| ticket_reopened | Hệ thống ticket | reopened_at, reason, trace_id | Khi khách mở lại trong 7 ngày |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, trên mẫu ngẫu nhiên |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `ticket_closed` (closed_at − created_at của `refund_request_created` ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- Dùng (bỏ qua gợi ý): số `staff_review_decision` có quyet_dinh là sua hoặc bo, chia tổng số `staff_review_decision`.
- An toàn (lỗi lọt đến khách): số `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- Dùng (tự đề xuất): `staff_review_decision` nhóm theo staff_id và tuần, mẫu số là staff_id có arm = trợ lý trong `refund_request_created`.
- An toàn (tự đề xuất): `audit_sample_checked`, so so_tien_da_hoan với so_tien_dung.
- Chi phí mỗi việc thành công (A): `agent_run_completed` cho token và tool, `staff_review_decision` và `staff_rework_completed` cho phút đo thật thay cột `_simulated`.

**Event cho bảng khắc phục** (`bang_loi.md`), thêm vào danh sách trên để mọi cách phát hiện đều đo được:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_account_validation_failed | Form hoàn tiền | ngan_hang, truong_sai, trace_id | Khi số tài khoản sai định dạng (ca 1) |
| refund_success_notified | Dịch vụ thông báo | kenh, noi_dung, trace_id | Khi gửi tin "đã hoàn" cho khách (ca 7) |
| refund_destination_disputed | Hệ thống ticket | noi_nhan_mong_doi, noi_da_hoan, trace_id | Khi khách báo chưa nhận tiền (ca 3) |
| refund_outside_retention_window | Agent | ngay_don, trace_id | Khi đơn cũ hơn 12 tháng (ca 19) |
| refund_amount_mismatch | Đối soát tài chính | so_tien_da_hoan, so_tien_dung, trace_id | Khi đối soát hằng ngày thấy lệch (ca 5) |

`ledger_refund_committed` trong `bang_loi.md` là `refund_ledger_write` có ket_qua = ok; `refund_handoff_created` là `handoff_to_staff`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,77%: từ 4.472 đ lên 6.787 đ mỗi việc thành công; làm lại đã chiếm 51,8% tổng chi phí [simulated] | `staff_rework_completed` chia `refund_request_created` theo tuần > 7% (đợt chạy thử: 4,89% trong phạm vi, riêng hang_nang 11,39%) | Thu hẹp về noi_dia; Kỹ sư trưởng agent rà 20 trace làm lại trong 3 ngày | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ mỗi việc thành công = 0,98× của 12.000 đ; 12.414 đ = 1,03× nếu làm lại 15,3 phút [simulated] | % yêu cầu nhóm trợ lý có `staff_review_decision` còn > 50% cuối bước 0.25 (đợt chạy thử: 13,03% trong phạm vi) | Giảm xem lại theo bậc khi tỉ lệ bỏ qua gợi ý < 15% (đợt chạy thử: 21,09% trong phạm vi) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: 1.185 đ mỗi việc ở 45.000 yêu cầu/tháng, 2.370 đ nếu còn một nửa; tổng 4.599 đ lên 5.784 đ [simulated] | Việc thành công cộng dồn 4 tuần (`ticket_closed` không có `ticket_reopened`) < 16.875, tức 50% của 33.750 | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |

Giá token ít rủi ro: gấp đôi chỉ +5,62% (4.723 đ) [simulated], nên không cần dấu hiệu theo dõi riêng.

Cách tính: tác động lấy từ B1, B4, A4 trong `bang_chi_phi.md`; tỉ lệ đợt chạy thử đếm trên `src/logix_requests.csv` (làm lại 48/982, riêng hang_nang 18/158; xem lại 128/982; bỏ qua gợi ý 27/128).
