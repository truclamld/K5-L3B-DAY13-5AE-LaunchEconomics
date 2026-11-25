"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
import pandas as pd

# Đảm bảo các thông báo tiếng Việt in được trong terminal Windows không dùng UTF-8.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] / 1000 * gia_vao
                  + runs['tokens_out'] / 1000 * gia_ra)
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = (reqs['phut_xem_lai_simulated'].sum()
               * luong_phut * he_so_xem_lai)
    lam_lai = (reqs['phut_lam_lai_simulated'].sum()
               * luong_phut * he_so_lam_lai)
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else float('inf'),
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs)
        if len(reqs) else 0,
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu cho pilot ----------
# Cho sẵn: baseline 0,70; mục tiêu +5 điểm; alpha 0,05; power 0,8; ICC 0,02.
ICC = 0.02


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức so sánh hai tỉ lệ, z chính xác)."""
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """DE = 1 + (m - 1) × ICC, m là số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(c, m, icc=ICC):
    """Cỡ mẫu hiệu dụng khi chia theo cụm: c × m / DE (luôn nhỏ hơn c / ICC)."""
    return c * m / he_so_thiet_ke(m, icc)


def m_toi_thieu(n_can, c, icc=ICC):
    """Số yêu cầu tối thiểu mỗi cụm để c cụm đạt n_can: giải c·m / (1 + (m-1)·ICC) ≥ n_can."""
    if n_can >= c / icc:
        return math.inf      # vượt trần c / ICC, không m nào đạt
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


def nhiem_vu_d(reqs, baseline=0.70, muc_tieu=0.05):
    """In năm câu D1, power khi chấp nhận mức chênh 6 điểm, và tỉ lệ mở lại hiện tại (cho luật an toàn)."""
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    print('\n=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    n = co_mau(baseline, baseline + muc_tieu)
    print(f'a) Chia theo yêu cầu: {n:,} yêu cầu mỗi nhóm')

    de_b = he_so_thiet_ke(75)
    n_b = math.ceil(n * de_b)
    nv_b = math.ceil(n_b / 75)
    print(f'b) Theo nhân viên, m = 75: DE = {de_b:.2f}; n = {n_b:,} mỗi nhóm → {nv_b} nhân viên mỗi nhóm, '
          f'tổng {2 * nv_b} > 40 → {"KHÔNG đủ người" if 2 * nv_b > 40 else "đủ người"}')

    tran_c = 20 / ICC
    print(f'c) 20 nhân viên mỗi nhóm: hiệu dụng tối đa = 20 / {ICC} = {tran_c:,.0f} '
          f'{"<" if tran_c < n else "≥"} {n:,} → {"KHÔNG đạt" if tran_c < n else "đạt"}')

    print(f'd) 6 depot mỗi nhóm: hiệu dụng tối đa = 6 / {ICC} = {6 / ICC:,.0f}')

    n6 = co_mau(baseline, baseline + 0.06)
    m_e = m_toi_thieu(n6, 20)
    print(f'e) Mức chênh 6 điểm ({n6} mỗi nhóm), 20 nhân viên mỗi nhóm: m ≥ {m_e} yêu cầu mỗi người '
          f'(DE = {he_so_thiet_ke(m_e):.2f}; hiệu dụng = {co_mau_hieu_dung(20, m_e):,.0f})')

    h5 = proportion_effectsize(baseline + muc_tieu, baseline)
    power_5 = NormalIndPower().power(h5, nobs1=n6, alpha=0.05)
    print(f'Đánh đổi: thiết kế cho 6 điểm (n = {n6}) mà tác động thật chỉ 5 điểm thì power còn {power_5:.2f}')

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    print('\n=== D3 · Tỉ lệ hiện tại trước khi đặt luật dừng ===')
    print(f'mo_lai_trong_7_ngay toàn mẫu: {reqs["mo_lai_trong_7_ngay"].mean():.2%} '
          f'({reqs["mo_lai_trong_7_ngay"].sum()}/{len(reqs)})')
    print(f'mo_lai_trong_7_ngay noi_dia + hang_nang: {pham_vi["mo_lai_trong_7_ngay"].mean():.2%} '
          f'({pham_vi["mo_lai_trong_7_ngay"].sum()}/{len(pham_vi)})')
    print(f'Tỉ lệ lam_lai trong phạm vi: {(pham_vi["ket_qua"] == "lam_lai").mean():.2%}')
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    print(f'Tỉ lệ bỏ qua gợi ý (sua + bo): {xem["quyet_dinh_xem_lai"].isin(["sua", "bo"]).mean():.2%} '
          f'({xem["quyet_dinh_xem_lai"].isin(["sua", "bo"]).sum()}/{len(xem)})')
    yc_moi_ngay = 1500 / 40 * len(pham_vi) / len(reqs)
    print(f'Yêu cầu trong phạm vi mỗi nhân viên mỗi ngày ≈ {yc_moi_ngay:.1f} → '
          f'{m_e} yêu cầu cần ≈ {math.ceil(m_e / yc_moi_ngay)} ngày ở bước 0.50')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:12s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:12s} {gia_tri:>14,.0f}')
    print('\nA3 · Theo loại yêu cầu')
    for loai in reqs['loai'].unique():
        nhom = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, nhom)
        ti_le = kq['thanh_cong'] / len(nhom)
        so_lan = nhom['so_lan_chay'].sum() / len(nhom)
        print(f'{loai:12s} yeu_cau={len(nhom):4d} thanh_cong={ti_le:.1%} '
              f'lan_chay/yc={so_lan:.2f} cps={kq["cps"]:,.0f} '
              f'so_voi_12k={kq["cps"] / BASELINE:.2f}x')

    print('\nA4 · Chi phí cố định (noi_dia + hang_nang)')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pham_vi = mo_hinh(runs, pham_vi)
    thanh_cong_thang = 45000 * kq_pham_vi['thanh_cong'] / len(reqs)
    cps_bien_doi = kq_pham_vi['cps']
    for ten, he_so_khoi_luong in [('45.000 yêu cầu/tháng', 1),
                                 ('Một nửa khối lượng', 0.5)]:
        thanh_cong_ky = thanh_cong_thang * he_so_khoi_luong
        co_dinh_moi_viec = 40_000_000 / thanh_cong_ky
        cps_co_dinh = cps_bien_doi + co_dinh_moi_viec
        print(f'{ten:25s} viec_thanh_cong={thanh_cong_ky:,.0f} '
              f'co_dinh/viec={co_dinh_moi_viec:,.0f} '
              f'tong_cps={cps_co_dinh:,.0f} '
              f'so_voi_12k={cps_co_dinh / BASELINE:.2f}x [simulated]')
    # B1 · Độ nhạy từng yếu tố
    print('\nB1 · Độ nhạy (CPS, thay đổi so với cơ sở)')
    base = ket_qua['cps']
    cases = {
        'token_x2': mo_hinh(runs, reqs, gia_vao=52, gia_ra=260),
        'token_x0.5': mo_hinh(runs, reqs, gia_vao=13, gia_ra=65),
        'review_x2': mo_hinh(runs, reqs, he_so_xem_lai=2),
        'review_x0.5': mo_hinh(runs, reqs, he_so_xem_lai=.5),
        'rework_x2': mo_hinh(runs, reqs, he_so_lam_lai=2),
        'rework_x0.5': mo_hinh(runs, reqs, he_so_lam_lai=.5),
        'wage_2500': mo_hinh(runs, reqs, luong_phut=2500),
        'cap_2': mo_hinh(runs, reqs, max_lan_chay=2),
        'cap_1': mo_hinh(runs, reqs, max_lan_chay=1),
    }
    for name, result in cases.items():
        print(name, f"{result['cps']:,.2f}",
              f"{(result['cps'] / base - 1) * 100:+.2f}%")
    paired = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print('token_x2_and_review_x2', f"{paired['cps']:,.2f}",
          f"{(paired['cps'] / base - 1) * 100:+.2f}%")

    # B3 · So sánh chi phí toàn hệ thống sau khi chuyển ca lỗi cho nhân viên.
    print('\nB3 · Giới hạn chạy lại (tổng trợ lý, lỗi, tổng hệ thống, CPS)')
    for cap in (1, 2, 3):
        result = mo_hinh(runs, reqs, max_lan_chay=cap)
        failed = len(reqs) - result['thanh_cong']
        system = result['tong'] + failed * BASELINE
        print(cap, f"{result['tong']:,.0f}", failed,
              f"{system:,.0f}", f"{result['cps']:,.2f}")

    # B4 · 100% review theo giả định của hướng dẫn; các phút là simulated.
    print('\nB4 · Xem lại 100% trong noi_dia + hang_nang')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pham_vi = runs[runs['request_id'].isin(pham_vi['request_id'])]
    trace_cost = mo_hinh(runs_pham_vi, pham_vi, luong_phut=0)
    ok_ids = set(runs_pham_vi.loc[runs_pham_vi['status'] == 'ok', 'request_id'])
    review_cost = len(ok_ids) * 5 * LUONG_PHUT
    rework_cost = (pham_vi['ket_qua'] == 'lam_lai').sum() * 9 * LUONG_PHUT
    total_review_all = trace_cost['tong'] + review_cost + rework_cost
    print('5-min-review_9-min-rework', f"{total_review_all:,.0f}",
          f"CPS={total_review_all / trace_cost['thanh_cong']:,.2f} [simulated]")
    # Hướng dẫn dùng mức trung bình 15,3 phút/ca trên toàn bộ ca làm lại,
    # áp dụng cho số ca làm lại trong phạm vi pilot.
    rework_cases_scope = (pham_vi['ket_qua'] == 'lam_lai').sum()
    rework_mean_all = round(reqs.loc[reqs['ket_qua'] == 'lam_lai',
                                     'phut_lam_lai_simulated'].mean(), 1)
    rework_observed = rework_cases_scope * rework_mean_all * LUONG_PHUT
    print('using observed simulated rework minutes',
          f"CPS={(trace_cost['tong'] + review_cost + rework_observed) / trace_cost['thanh_cong']:,.2f}")

    # CP4 · Nhiệm vụ D: cỡ mẫu (D1) và tỉ lệ hiện tại cho luật dừng (D3).
    nhiem_vu_d(reqs)
