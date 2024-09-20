import sys
from collections import deque 

M, N, H = map(int, sys.stdin.readline().split())
boxes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0,0 ,0, 0, 1, -1]

def checkExsist(num):
    for h in range(H):
            for y in range(N):
                for x in range(M):
                    if(boxes[h][y][x] == num):
                        return True
    return False


def bfs():
    queue = deque()
    
    result = 0
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if(boxes[h][y][x] == 1):
                    queue.append([h, y, x, 0])

    while(queue):
        h, y, x, day = queue.popleft()

        for i in range(6):
            nextH = h + dh[i]
            nextY = y + dy[i]
            nextX = x + dx[i]

            if(nextH >= 0 and nextH < H and nextY >= 0 and nextY < N and nextX>=0 and nextX<M and boxes[nextH][nextY][nextX] == 0):
                queue.append([nextH, nextY, nextX, day+1])
                boxes[nextH][nextY][nextX] = 1
                result = day+1
    
    if(checkExsist(0)):
        print(-1)
    else:
        print(result)

bfs()