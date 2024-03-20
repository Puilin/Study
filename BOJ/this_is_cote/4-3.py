origin = input()
column = origin[0]
x = int(origin[1])

y = ord(column) - 96

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)