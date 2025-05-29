from collections import deque
import sys

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visit = [([sys.maxsize] * M) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

queue = deque()
queue.append((0, 0))
visit[0][0] = 1

while(queue):
    currentX, currentY = queue.popleft()
    for i in range(4):
        nextX = currentX + dx[i]
        nextY = currentY + dy[i]
        if(0 <= nextX < M and 0 <= nextY < N and visit[nextY][nextX] == sys.maxsize and board[nextY][nextX] == '1'):
            queue.append([nextX, nextY])
            visit[nextY][nextX] = min(visit[currentY][currentX] + 1, visit[nextY][nextX])


print(visit[N-1][M-1])
