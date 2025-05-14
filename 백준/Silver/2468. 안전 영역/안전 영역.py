from collections import deque
import sys

N = int(input())
minNum, maxNum = sys.maxsize, 0
board = []
for _ in range(N):
    inputArr = list(map(int, input().split()))
    board.append(inputArr)
    minNum = min(minNum, min(inputArr))
    maxNum = max(maxNum, max(inputArr))

dx = [0, 1, 0 , -1]
dy = [-1, 0, 1, 0]

def CheckArea(currentX, currentY, visit):
    queue = deque()
    queue.append((currentX, currentY))

    while(queue):
        poppedX, poppedY = queue.popleft()
        for i in range(4):
            nextX = poppedX + dx[i]
            nextY = poppedY + dy[i]

            if(nextX >= 0 and nextX < N and nextY >= 0 and nextY < N and not visit[nextY][nextX] and board[nextY][nextX] > height):
                queue.append((nextX, nextY))
                visit[nextY][nextX] = True

result = 0

for height in range(minNum-1, maxNum+1):
    visit = []
    count = 0
    for _ in range(N):
        visit.append([False]*N)

    for y in range(N):
        for x in range(N):
            if(not visit[y][x] and board[y][x] > height):
                CheckArea(x, y, visit)
                count += 1
    result = max(result, count)

print(result)