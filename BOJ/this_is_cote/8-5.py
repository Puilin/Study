x = int(input())

dp = [0] * (x+1)

for i in range(1, x+1):
    if i in [5, 3, 2]:
        dp[i] = 1
    else:
        a, b, c, d = 30001, 30001, 30001, 30001
        if i % 5 == 0:
            a = dp[i//5]
        if i % 3 == 0:
            b = dp[i//3]
        if i % 2 == 0:
            c = dp[i//2]
        d = dp[i-1]
        dp[i] = min(a, b, c, d) + 1

print(dp[x])