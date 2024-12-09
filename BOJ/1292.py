a, b = map(int, input().split())

dp = [0 for _ in range(b+1)]
dp[1] = 1

i, step, count = 2, 2, 0
while i <= b:
    dp[i] = dp[i-1] + step
    count += 1
    i += 1
    if count == step:
        step += 1
        count = 0

print(dp[b]-dp[a-1])