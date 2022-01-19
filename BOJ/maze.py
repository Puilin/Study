from collections import deque

N, M = map(int, input().split())

adj = []
for _ in range(N):
    arr = list(map(int, list(input())))
    adj.append(arr)

# 도착지는 늘 우하단이므로 동쪽과 남쪽에 대한 방향만 정의 (Greedy)
dx = [1, 0]
dy = [0, 1]


def bfs(x, y):
    queue = deque([(0,0)])
    global count
    while queue:
        X, Y = queue.popleft()
        if 0<=X<N and 0<=Y<M and adj[X][Y] == 1:
            count += 1
            for i in range(2):
                nx = X + dx[i]
                ny = Y + dy[i]
                queue.append((nx, ny))

count = 0
bfs(0, 0)
print(count)