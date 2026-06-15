chuoi = input("Nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")

ds_nhi_phan = chuoi.split(",")
ket_qua = []

for so in ds_nhi_phan:
    so = so.strip()
    gia_tri_thap_phan = int(so, 2)

    if gia_tri_thap_phan % 5 == 0:
        ket_qua.append(so)

print(",".join(ket_qua))