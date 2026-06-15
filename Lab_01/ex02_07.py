print("Nhập các dòng văn bản. Nhấn Enter ở dòng trống để kết thúc.")

ds_dong = []

while True:
    dong = input()
    if dong == "":
        break
    ds_dong.append(dong.upper())

for dong in ds_dong:
    print(dong)