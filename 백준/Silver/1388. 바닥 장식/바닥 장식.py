import sys

N, M = map(int, sys.stdin.readline().split())
board = []
count = 0
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))


def func(X, Y, visited):
    if(board[Y][X] == '-'):
        for i in range(X, M):
            if(board[Y][i] != '-'):
                break
            visited[Y][i] = True
    else:
         for i in range(Y, N):
            if(board[i][X] != '|'):
                break
            visited[i][X] = True



visited = [([False] * M) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if(not visited[i][j]):
            visited[i][j] = True
            func(j, i, visited)
            count += 1

print(count)