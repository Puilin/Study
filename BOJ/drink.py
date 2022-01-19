N, M = map(int, input().split())

adj = []
for _ in range(N):
    arr = list(map(int, list(input())))
    adj.append(arr)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if adj[x][y] != 0:
        return False
    adj[x][y] = 1 # 구멍이 뚫려 있을경우(0) 방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
    return True

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1
print(count)