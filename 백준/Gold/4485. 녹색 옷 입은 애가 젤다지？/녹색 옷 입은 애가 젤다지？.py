import sys
import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
TestCount = 1

def searchGraph():
    queue = []
    heapq.heappush(queue, (board[0][0], 0, 0))
    visited[0][0] = board[0][0]

    while queue:
        currentCost, currentX, currentY = heapq.heappop(queue)

        if currentX == N - 1 and currentY == N - 1:
            return currentCost

        for i in range(4):
            nextX, nextY = currentX + dx[i], currentY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < N:
                nextCost = currentCost + board[nextY][nextX]
                if nextCost < visited[nextY][nextX]:
                    visited[nextY][nextX] = nextCost
                    heapq.heappush(queue, (nextCost, nextX, nextY))

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[sys.maxsize] * N for _ in range(N)]
    result = searchGraph()
    print(f"Problem {TestCount}: {result}")
    TestCount += 1
