items = ["apple", "banana", "apple", "orange", "banana", "apple"]

dem = {}

for item in items:
    if item in dem:
        dem[item] += 1
    else:
        dem[item] = 1

print("Danh sách:", items)
print("Số lần xuất hiện:", dem)