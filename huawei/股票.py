prices = [2, 21, 28, 6, 56]

a = 0
for index in range(1, len(prices)):
    a += max(0, prices[index] - prices[index - 1])

print(a)