sinh_vien = {
    "id": "SV001",
    "ten": "Nguyen Van A",
    "nganh": "Cong nghe thong tin",
    "diem": 8.5
}

print("Dictionary ban đầu:", sinh_vien)

key = input("Nhập key cần xóa: ")

if key in sinh_vien:
    del sinh_vien[key]
    print("Dictionary sau khi xóa:", sinh_vien)
else:
    print("Key không tồn tại trong Dictionary.")