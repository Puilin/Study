from collections import deque

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = tuple(map(int, input().split()))
    adj[x].append(y)

def dfs(x):
    if len(adj[x]) == 0:
        return
    global count
    count += 1 # 방문처리
    for item in adj[x]:
        dfs(item)

count = 0
dfs(1)
print("dfs")
print(count)

# bfs
queue = deque(adj[1]) # [2,5]
history = []
while queue:
    now = queue.popleft()
    if not now in history:
        history.append(now)
    for i in adj[now]:
        queue.append(i)

print("bfs")
print(len(history))