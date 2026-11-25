# Báo cáo cá nhân — Hoàng Dương Anh Quân (2A202603735)

## 1. Thông tin thành viên

- Họ tên: Hoàng Dương Anh Quân
- MSSV: 2A202603735
- Email: 26ai.quanhda@vinuniversity.edu.vn
- Vai trong nhóm: Người gắn nhãn 1, phụ trách Nhiệm vụ C

## 2. Phần việc phụ trách

Phụ trách Nhiệm vụ C (CP3). Công việc gồm phân loại 20 ca lỗi lần 1 theo nguyên nhân gốc, đối chiếu với bộ nhãn của Hiếu và đề xuất cách khắc phục cho năm ca đại diện.

## 3. Đóng góp cụ thể

- Đối chiếu từng ca với bộ nhãn gốc của Hiếu ở commit `2969d36`. Sau khi sửa hai nhãn bị chép nhầm ở ca 13 và 15, kết quả đồng thuận ban đầu là 19/20 ca (95%).
- Ghi lý do thống nhất nhãn cho ca 8. Ca này được xếp vào **Hệ thống** vì trợ lý viện dẫn điều khoản không tồn tại trong chính sách hiện hành.
- Đề xuất biện pháp cho năm ca đại diện (1, 7, 3, 19 và 5). Mỗi ca có cách phát hiện đo được, hướng khắc phục và một vai trò phụ trách.

## 4. Bằng chứng

- Bảng 20 ca, hai bộ nhãn, nhãn thống nhất và phép tính đồng thuận. [Bảng đối chiếu](bang_loi.md#hai-bộ-nhãn-độc-lập)
- Biện pháp khắc phục cho năm loại lỗi. [Bảng khắc phục](bang_loi.md#bảng-khắc-phục-cho-5-ca-mỗi-loại-một-ca)

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc đề, đối chiếu bảng và soạn báo cáo. Phần kiểm tra gồm đối chiếu hai cột nhãn với bộ nhãn gốc của Hiếu, đếm 19 dòng trùng, đọc lại mô tả và hướng dẫn cho ca 8, rồi kiểm tra bảng khắc phục đủ năm loại lỗi.

## 6. Tự đánh giá

- **Làm tốt** — Hoàn thành bảng đối chiếu 20 ca, giải thích nhãn thống nhất cho ca 8 và đề xuất biện pháp khắc phục cho đủ năm loại lỗi.
- **Còn hạn chế** — Hai nhãn của Hiếu ở ca 13 và 15 bị chép sai khi gộp bảng. Sau khi đối chiếu với bộ nhãn gốc, kết quả được sửa thành 19/20 ca trùng (95%).
- **Cần cải thiện** — Kiểm tra từng dòng với hai bộ nhãn gốc trước khi tính tỉ lệ đồng thuận và ghi lý do ngay khi gắn nhãn các ca dễ nhầm.
