inp = int(input())

test_case = [int(input()) for _ in range(inp)]

def fun(n):
    if n == i:
        return 1
    elif n > i:
        return 0
    else:
        return fun(n+1) + fun(n+2) + fun(n+3)

for i in test_case:
    print(fun(0))