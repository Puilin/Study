n = int(input())
arr = list(map(int, input().split()))

dp = [arr]

k = 1
while k <= n-1:
    dp.append([])
    for j in range(n-k):
        sum = 0
        for i in range(k+1):
            sum += arr[j+i]
        dp[k].append(sum)
    k += 1

m = -1001
for line in dp:
    if m < max(line):
        m = max(line)

print(m)