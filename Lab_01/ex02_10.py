def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]


chuoi = input("Nhập một chuỗi: ")

print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(chuoi))