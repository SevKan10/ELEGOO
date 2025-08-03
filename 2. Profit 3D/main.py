import tkinter as tk
from tkinter import ttk, messagebox

def tinh_tien_in():
    try:
        loai_nhua = combo_loai.get()
        khoi_luong = float(entry_khoi_luong.get())
        gio = int(entry_gio.get())
        phut = int(entry_phut.get())
        thoi_gian = gio + phut / 60
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng nhập đúng định dạng số.")
        return

    # Giá nhựa theo gam
    gia_nhua = {
        "PLA": 210_000 / 1000,
        "PLA+": 260_000 / 1000,
        "ABS": 160_000 / 1000,
        "PETG": 160_000 / 1000
    }

    # Công suất máy và tiền điện
    cong_suat_kw = 310 / 1000
    dien_tieu_thu = cong_suat_kw * thoi_gian

    def tinh_tien_dien(kwh):
        tien = 0
        if kwh <= 50:
            tien = kwh * 1984
        elif kwh <= 100:
            tien = 50 * 1984 + (kwh - 50) * 2050
        elif kwh <= 200:
            tien = 50 * 1984 + 50 * 2050 + (kwh - 100) * 2380
        else:
            tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + (kwh - 200) * 2998
        return tien
    T = 1.25
    Tt = T * 100 - 100
    tien_nhua = gia_nhua[loai_nhua] * khoi_luong
    tien_dien = tinh_tien_dien(dien_tieu_thu)
    hao_mon_moi_gio = 5000
    tien_cong_moi_gio = 10000
    tien_hao_mon = thoi_gian * hao_mon_moi_gio
    tien_cong = thoi_gian * tien_cong_moi_gio

    tong_chi_phi = tien_nhua + tien_dien + tien_hao_mon + tien_cong
    gia_ban = tong_chi_phi * T  # lời **%

    ket_qua = f"""\
Thời gian in: {gio} giờ {phut} phút
Tiền nhựa: {round(tien_nhua):,} VNĐ
Tiền điện: {round(tien_dien):,} VNĐ
Hao mòn máy: {round(tien_hao_mon):,} VNĐ
Tiền công: {round(tien_cong):,} VNĐ
----------------------------
Tổng chi phí: {round(tong_chi_phi):,} VNĐ
Giá đề xuất ({Tt}% lời): {round(gia_ban):,} VNĐ
"""
    text_kq.delete("1.0", tk.END)
    text_kq.insert(tk.END, ket_qua)


# === Giao diện ===
root = tk.Tk()
root.title("Tính tiền in 3D")
root.geometry("420x460")
root.resizable(False, False)

tk.Label(root, text="Chọn loại nhựa:").pack(pady=5)
combo_loai = ttk.Combobox(root, values=["PLA", "PLA+", "ABS", "PETG"], state="readonly")
combo_loai.set("PLA")
combo_loai.pack()

tk.Label(root, text="Khối lượng nhựa cần in (g):").pack(pady=5)
entry_khoi_luong = tk.Entry(root)
entry_khoi_luong.pack()

tk.Label(root, text="Thời gian in:").pack(pady=5)
frame_time = tk.Frame(root)
frame_time.pack()

tk.Label(frame_time, text="Giờ:").pack(side=tk.LEFT, padx=5)
entry_gio = tk.Entry(frame_time, width=5)
entry_gio.pack(side=tk.LEFT)

tk.Label(frame_time, text="Phút:").pack(side=tk.LEFT, padx=5)
entry_phut = tk.Entry(frame_time, width=5)
entry_phut.pack(side=tk.LEFT)

tk.Button(root, text="Tính tiền", command=tinh_tien_in, bg="#4CAF50", fg="white").pack(pady=10)

text_kq = tk.Text(root, height=12, width=50)
text_kq.pack(pady=5)

root.mainloop()
