n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n] * n

def dfs(x, y, u:list):
    u.append((x, y))
    global visited
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]


        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
            visited[x][y] = True
            dfs(nx, ny, u)

# count = 0
# for i in range(n):
#     for j in range(n):
#         union = []
#         dfs(i, j, union)
#         population = 0
#         for x, y in union:
#             population += graph[x][y]
#         for x, y in union:
#             graph[x][y] = population // len(union)
#             print(graph[x][y])
        
#         print(union)
        
#         if len(union) > 1:
#             count += 1

done = False
count = 0
while not done:
    unions = []
    visited = [[False] * n] * n
    for i in range(n):
        for j in range(n):
            union = []
            dfs(i, j, union)
            unions.append(union)
            population = 0
            for x, y in union:
                population += graph[x][y]
            for x, y in union:
                graph[x][y] = population // len(union)
                print(f"{x} {y}", graph[x][y])    
    
    done_checker = 0
    for i in unions:
        if len(i) == 1:
            done_checker += 1
    if done_checker == len(unions):
        break
    count += 1


print(count)

"""
10 100 20 90
       - - - -
80 100 |60 | 70
       - - - -
70 20 30 40
50 20 100 10
"""