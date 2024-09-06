data = """2 3 10 
2 4 20 
1 3 15 
1 4 25 
3 4 8 
1 4 16"""

total_hour = 4
hour_discount_mapping = [list(map(int, item.strip().split(" "))) for item in data.split("\n")]
print(hour_discount_mapping)

sorted_mapping = sorted(hour_discount_mapping, key=lambda x: x[-1])

total = 0
for current_hour in range(1, total_hour + 1):
    # 1 2 3 4
    for start, end, price in sorted_mapping:
        if start <= current_hour and end >= current_hour:
            total += price
            break
print(total)