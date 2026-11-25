# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): 5AE
- Nhóm được chấm: T100

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất Go có điều kiện khớp với CPS B4 11.743–12.415 đ (0,98–1,03× baseline) và power ~0,64 nếu tác động chỉ 5 điểm; yêu cầu đo lại phút thật, giới hạn rollout và giữ ngưỡng an toàn trước khi mở rộng. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Gắn nhãn `simulated` cho số chi phí dựa trên phút ước tính; chọn `noi_dia` + `hang_nang`, loại `quoc_te` vì 22.515 đ = 1,88× baseline, và nêu điều kiện mở `hang_nang` theo CPS. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Có đối chứng đồng thời 20+20 nhân viên, ngẫu nhiên phân tầng depot; n hiệu dụng 859/nhánh, DE 6,96, MDE 6 điểm; luật dừng có ngưỡng, kỳ theo dõi và người quyết định dừng. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go · **Go có điều kiện** · No-go (giữ một)

**Lý do:** Hồ sơ có đối chứng, cỡ mẫu và luật dừng cụ thể; đề xuất giới hạn phạm vi/rollout và nêu rõ bất lợi về chi phí xem lại 100% cùng power ở mức chênh 5 điểm. Chỉ triển khai theo các điều kiện đã ghi trong hồ sơ T100.

**Một câu hỏi cho đội trình:** Ngưỡng 8.000 đ trong luật chi phí loại trừ 40 triệu đ chi phí cố định; nhóm sẽ dùng chỉ báo nào để quyết định không mở rộng nếu sản lượng thực tế thấp hơn giả định 45.000 yêu cầu/tháng?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm dùng chỉ báo ở E2: số việc thành công quy đổi theo tuần trong phạm vi noi_dia + hang_nang (đo từ ticket_closed không mở lại, kết hợp agent_suggestion_shown).

Ngưỡng: nếu sản lượng tụt < 50% kế hoạch (< 16.875 việc/tháng, tương ứng < 22.500 yêu cầu/tháng — cố định đội gấp đôi lên 2.370 đ/việc, tổng CPS 5.784 đ, simulated) trong 2 tuần liên tiếp ở bước 20 người, PM trợ lý hoàn phí sẽ không mở rộng và đàm phán lại hợp đồng 40 triệu/tháng.
