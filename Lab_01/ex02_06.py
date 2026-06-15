x = int(input("Nhập số dòng X: "))
y = int(input("Nhập số cột Y: "))

mang = []

for i in range(x):
    dong = []
    for j in range(y):
        dong.append(i * j)
    mang.append(dong)

print(mang)