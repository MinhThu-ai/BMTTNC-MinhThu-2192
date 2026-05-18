# ex02_07.py
lines = []

while True:
    s = input("Nhập chuỗi (enter để kết thúc): ")
    if s == "":
        break
    lines.append(s.upper())

for line in lines:
    print(line)