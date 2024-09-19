import sys
from collections import deque 

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(sys.stdin.readline().rstrip('\n'))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def Bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited = [([False] * M) for _ in range(N)]
    visited[0][0] = True

    while(queue):
        X, Y, count = queue.popleft()
        if(X == M-1 and Y == N-1):
            print(count+1)
            break

        for i in range(4):
            nextX = X+dx[i]
            nextY = Y+dy[i]
            if(nextX >= 0 and nextX < M and nextY >= 0 and nextY < N and not visited[nextY][nextX] and board[nextY][nextX] == '1'):
                queue.append([nextX, nextY, count+1])
                visited[nextY][nextX] = True

Bfs()
