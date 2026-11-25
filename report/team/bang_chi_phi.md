# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | trace + phút nhân viên | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí / việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | tổng token + tool / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Khoảng **16,3 lần** (4.472 / 274,7).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại: 51,8%** tổng chi phí [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? `quoc_te` không đáng xử lý: chi phí 22.515 đ/việc thành công (1,88× mức 12.000 đ), thành công 27,3%. Chạy lại đến 3 lần không giúp: tỉ lệ đúng theo lần 1/2/3 chỉ 30%/11,4%/2,2% [simulated].

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không ở quy mô đầy đủ: 4.599 đ/việc thành công vẫn thấp hơn 12.000 đ; khi khối lượng giảm một nửa, chi phí cố định tăng lên 2.370 đ/việc nhưng tổng vẫn 5.784 đ [simulated].

## B1 · Đổi từng yếu tố

Chi phí xem lại/làm lại dựa trên phút `*_simulated`; đây là các kịch bản **simulated**. CPS cơ sở: 4.471,97 đ trên 978 việc thành công.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723,08 đ | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346,41 đ | −2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292,01 đ | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.561,95 đ | −20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.786,90 đ | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.314,50 đ | −25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.505,71 đ | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237,29 đ | −5,25% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.110,99 đ | −8,07% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543,12 đ [simulated]/việc thành công**, tăng **46,31%** so với cơ sở **4.471,97 đ [simulated]**.
- Xếp hạng theo độ lớn tác động: **1. số ca làm lại** (−25,88%/+51,77%) · **2. tỉ lệ xem lại** (−20,35%/+40,70%) · **3. lương nhân viên** (+23,12%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | **6.901.220 đ [simulated]** | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn **2 lần** rẻ nhất cho công ty (tổng **6,90 triệu đ [simulated]**); không trùng mức CPS thấp nhất là **1 lần** (**4.111 đ [simulated]**), vốn chuyển thêm 85 yêu cầu sang nhân viên so với giới hạn 2 lần.

## B4 · Nếu phải xem lại tất cả

- Theo giả định simulated trong hướng dẫn (5 phút xem lại cho 948 yêu cầu có run `ok`, 9 phút làm lại cho 48 ca), tổng là 10.568.513 đ/900 việc thành công = **11.743 đ (0,98× 12.000 đ)**. Dùng 15,3 phút làm lại quan sát từ cột simulated, CPS thành **12.414 đ (1,03×)**.
- Pilot cần đo thời gian xem lại thực tế và tỉ lệ xem lại tối thiểu an toàn: xem lại 100% gần như mất hết lợi thế; với 15,3 phút làm lại, chi phí vượt nhân viên tự làm.
