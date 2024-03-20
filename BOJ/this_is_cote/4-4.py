n, m = tuple(map(int, input().split()))

a, b, d = tuple(map(int, input().split()))

maps = []
for _ in range(n):
    row = list(map(int, input().split()))
    maps.append(row)

dx = [-1, 0, 1, 0] # 0 1 2 3
dy = [0, 1, 0, -1]

count = 0
left = False
while True:
    for i in range(4):
        left = False
        d = (d + 3) % 4

        nx = a + dx[d]
        ny = b + dy[d]

        if maps[nx][ny] == 0:
            maps[a][b] = -1
            a = nx
            b = ny
            count += 1
            left = True
            break

    if left:
        continue
    
    # go backward
    nx = a + dx[(d + 2) % 4]
    ny = b + dy[(d + 2) % 4]

    print("backward nx :", nx, end=" ")
    print("backward ny :", ny)

    if maps[nx][ny] == 1:
        break
    else:
        maps[a][b] = -1
        a = nx
        b = ny
        count += 1

print(count)