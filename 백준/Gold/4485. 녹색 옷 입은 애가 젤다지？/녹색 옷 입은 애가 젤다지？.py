# 녹색 옷 입은 애가 젤다지?
import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
TestCount = 1

def serarchGraph():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = board[0][0]

    while(queue):
        currentX, currentY = queue.popleft()
        for i in range(4):
            nextX, nextY = currentX+dx[i], currentY+dy[i]
            if(0 <= nextX < N and 0 <= nextY < N and visited[nextY][nextX] > visited[currentY][currentX] + board[nextY][nextX]):
                visited[nextY][nextX] = visited[currentY][currentX] + board[nextY][nextX]
                queue.append([nextX, nextY])

while(1):
    N = int(sys.stdin.readline())
    if(N == 0):
        break
    board = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
    visited = [([sys.maxsize] * (N)) for _ in range(N)]
    serarchGraph()
    print(f"Problem {TestCount}: {visited[N-1][N-1]}")
    TestCount += 1