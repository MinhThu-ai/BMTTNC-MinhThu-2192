# Nhập số giờ làm việc và lương theo giờ
so_gio = float(input("Nhập số giờ làm việc trong tuần: "))
luong_gio = float(input("Nhập mức lương theo giờ: "))

# Tính lương
if so_gio <= 44:
    luong = so_gio * luong_gio
else:
    gio_tieu_chuan = 44
    gio_lam_them = so_gio - 44
    luong = gio_tieu_chuan * luong_gio + gio_lam_them * luong_gio * 1.5

print("Tiền lương thực nhận là:", luong)