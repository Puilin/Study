N = int(input())

adj = []
for _ in range(N):
    arr = list(map(int, list(input())))
    adj.append(arr)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N or adj[x][y] == 0:
        return False
    adj[x][y] = 0 # 방문 처리
    global home
    home += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
    return True
    

count = 0; home = 0
temp = []
for i in range(N):
    for j in range(N):
        if dfs(i, j):
            temp.append(home)
            home = 0
            count += 1

print(count)
temp.sort()
for i in range(len(temp)): print(temp[i])