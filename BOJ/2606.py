from collections import deque

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]

for i in range(M):
    x, y = tuple(map(int, input().split()))
    adj[x].append(y)

queue = deque(adj[1]) # [2,5]
history = []
while queue:
    now = queue.popleft()
    if not now in history:
        history.append(now)
    for i in adj[now]:
        queue.append(i)

print(len(history))