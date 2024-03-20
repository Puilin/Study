from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(300001)]
distance = [-1] * 300001

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)

def bfs(x, k):
    queue = deque()
    queue.append(x)
    distance[x] = 0

    while queue:
        city = queue.popleft()

        for another in graph[city]:
            if distance[another] == -1:
                distance[another] = distance[city] + 1
                queue.append(another)

    found = False
    for i in range(len(distance)):
        if distance[i] == k:
            found = True
            print(i)
    
    if not found:
        print(-1)

bfs(x, k)