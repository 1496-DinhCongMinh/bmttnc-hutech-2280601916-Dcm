so_h_lam = float(input("Nhập số h làm: "))
luong = float(input("Nhập thù lao trên mỗi h tiêu chuẩn: "))
h_tieu_chuan = 44
gio_vuot = max(0, (so_h_lam-h_tieu_chuan))

thuc_linh = h_tieu_chuan*luong + gio_vuot*luong*1.5
print(f"Số tiền thực lĩnh: {thuc_linh}")