inp = int(input())
test_case = list(int(input()) for i in range(inp))
def padoban(n):
    memo = []
    for i in range(n+1):
        if i <= 3:
            memo.append(1)
        else:
            memo.append(memo[i-2] + memo[i-3])
    return memo[n]
for j in test_case:
    print(padoban(int(j)))
