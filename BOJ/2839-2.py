inp = int(input())

dp = [0, -1, -1, 1, -1, 1]

def func(n):
    if n <= 5:
        return dp[n]
    else:
        for i in range(6, n+1):
            temp = []
            if dp[i-3] != -1:
                temp.append(dp[i-3] + 1)
            if dp[i-5] != -1:
                temp.append(dp[i-5] + 1)
            else:
                temp.append(-1)
            if -1 not in temp:
                dp.append(min(temp))
            else:
                dp.append(max(temp))
        return dp[n]

print(func(inp))