numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tong_chan = 0

for number in numbers:
    if number % 2 == 0:
        tong_chan += number

print("Danh sách:", numbers)
print("Tổng các số chẵn là:", tong_chan)