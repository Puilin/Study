T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    table = [
        [1],
        [2, 4, 8, 6],
        [3, 9, 7, 1],
        [4, 6],
        [5],
        [6],
        [7, 9, 3, 1],
        [8, 4, 2, 6],
        [9, 1]
    ]
    if (a % 10 == 0):
        print(10)
        continue
    i = a % 10 - 1
    length = len(table[i])
    ans = table[i][b % length - 1]
    print(ans)