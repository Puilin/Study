n, m = map(int, input().split())

def dfs(board, i, j):
    if board[i][j] == 0:
        board[i][j] = 1
        if j > 0:
            dfs(board, i, j-1)
        if j < m-1:
            dfs(board, i, j+1)
        if i > 0:
            dfs(board, i-1, j)
        if i < n-1:
            dfs(board, i+1, j)

board = []
for _ in range(n):
    row = list(map(int, list(input())))
    board.append(row)

count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            dfs(board, i, j)
            count += 1

print(count)