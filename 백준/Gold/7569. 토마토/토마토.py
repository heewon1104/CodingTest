import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
boxes = [[] for _ in range(H)]
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0 ,0, 0, 1, -1]
queue = deque()

for h in range(H):
    for y in range(N):
        inputArr = list(map(int, sys.stdin.readline().split()))
        boxes[h].append(inputArr)
        for x in range(M):
            if(boxes[h][y][x] == 1):
                queue.append([x, y, h, 0])

def CheckBoxes():
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if(boxes[h][y][x] == 0):
                    return False
    return True

result = 0
while(queue):
    check = CheckBoxes()
    if(check):
        break

    currentX, currentY, currentH, currentTime = queue.popleft()
    for i in range(6):
        nextH = currentH + dh[i]
        nextY = currentY + dy[i]
        nextX = currentX + dx[i]
        
        if(0<=nextH<H and 0<=nextY< N and 0<=nextX< M and boxes[nextH][nextY][nextX] == 0):
            boxes[nextH][nextY][nextX] = 1
            queue.append([nextX, nextY, nextH, currentTime + 1])
            result = max(result, currentTime + 1)

if(not CheckBoxes()):
    print(-1)
else:
    print(result)