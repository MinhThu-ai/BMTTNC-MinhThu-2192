chuoi = input("Nhập các phần tử, cách nhau bằng dấu phẩy: ")

danh_sach = chuoi.split(",")
tuple_ket_qua = tuple(danh_sach)

print("List:", danh_sach)
print("Tuple:", tuple_ket_qua)