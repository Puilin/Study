n = int(input())

coins = [500, 100, 50, 10]

count = 0
while n > 0:
    for coin in coins:
        if n >= coin:
            n -= coin
            count += 1
            break

print(count)