# ex02_06.py
X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))

matrix = []

for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    matrix.append(row)

print(matrix)