# ex02_08.py
binary_list = input("Nhập các số nhị phân: ").split(",")

result = []

for b in binary_list:
    if int(b, 2) % 5 == 0:
        result.append(b)

print(",".join(result))