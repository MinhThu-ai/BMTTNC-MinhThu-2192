# ex02_05.py
hours = float(input("Nhập số giờ làm: "))
rate = float(input("Nhập tiền công mỗi giờ: "))

standard_hours = 44

if hours <= standard_hours:
    salary = hours * rate
else:
    overtime = hours - standard_hours
    salary = standard_hours * rate + overtime * rate * 1.5

print("Tiền lương thực lĩnh:", salary)