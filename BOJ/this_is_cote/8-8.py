n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [10001] * 10001

for coin in coins:
    dp[coin] = 1
# dp - - 1 1 2
#idx 0 1 2 3 4 

for i in range(0, m+1):
    smallest = 10001
    for coin in coins:
        if i - coin < 0 or i == coin:
            continue
        if dp[i-coin] + 1 < smallest:
            smallest = dp[i-coin] + 1
    if dp[i] < smallest:
        continue
    dp[i] = smallest

print(dp[m] if dp[m] != 10001 else -1)