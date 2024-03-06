from collections import deque
N = int(input())

board = []
sharkIdxX = -1
sharkIdxY = -1
sharkSize = 2
sharkExp = 0
time = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    if(9 in tmp):
        sharkIdxY = i
        sharkIdxX = tmp.index(9)
    board.append(tmp)

board[sharkIdxY][sharkIdxX] = 0

# 거리같을시 상 -> 위쪽 여러개면 좌
dx =[0,1,0,-1]
dy =[-1,0,1,0]

while(1):
    visit = [[0]*(N) for i in range(N)]
    resDistane = 10000
    resIdxX = 21
    resIdxY = 21

    queue = deque()
    queue.append([sharkIdxX, sharkIdxY, 0])

    while(queue):
        poppedX, poppedY, distance = queue.popleft()

        if(visit[poppedY][poppedX] != 0):
            continue
        visit[poppedY][poppedX] = 1
        
        if(poppedY + dy[0] >= 0):
            if(board[poppedY + dy[0]][poppedX + dx[0]] <= sharkSize):
                queue.append([poppedX + dx[0], poppedY + dy[0], distance+1])
                if(board[poppedY + dy[0]][poppedX + dx[0]] < sharkSize and board[poppedY + dy[0]][poppedX + dx[0]] != 0):
                    if(resDistane > distance+1):
                        resDistane = distance + 1
                        resIdxX = poppedX + dx[0]
                        resIdxY = poppedY + dy[0]
                    elif(resDistane == distance+1 and resIdxY > poppedY+dy[0]):
                        resIdxX = poppedX + dx[0]
                        resIdxY = poppedY + dy[0]
                    elif(resDistane == distance+1 and resIdxY == poppedY+dy[0] and resIdxX > poppedX+dx[0]):
                        resIdxX = poppedX + dx[0]
        
        if(poppedY + dy[2] < N):
            if(board[poppedY + dy[2]][poppedX + dx[2]] <= sharkSize):
                queue.append([poppedX + dx[2], poppedY + dy[2], distance+1])
                if(board[poppedY + dy[2]][poppedX + dx[2]] < sharkSize and board[poppedY + dy[2]][poppedX + dx[2]] != 0):
                    if(resDistane > distance+1):
                        resDistane = distance + 1
                        resIdxX = poppedX + dx[2]
                        resIdxY = poppedY + dy[2]
                    elif(resDistane == distance+1 and resIdxY > poppedY+dy[2]):
                        resIdxX = poppedX + dx[2]
                        resIdxY = poppedY + dy[2]
                    elif(resDistane == distance+1 and resIdxY == poppedY+dy[2] and resIdxX > poppedX+dx[2]):
                        resIdxX = poppedX + dx[2]

        if(poppedX + dx[3] >= 0):
            if(board[poppedY + dy[3]][poppedX + dx[3]] <= sharkSize):
                queue.append([poppedX + dx[3], poppedY + dy[3], distance+1])
                if(board[poppedY + dy[3]][poppedX + dx[3]] < sharkSize and board[poppedY + dy[3]][poppedX + dx[3]] != 0):
                    if(resDistane > distance+1):
                        resDistane = distance + 1
                        resIdxX = poppedX + dx[3]
                        resIdxY = poppedY + dy[3]
                    elif(resDistane == distance+1 and resIdxY > poppedY+dy[3]):
                        resIdxX = poppedX + dx[3]
                        resIdxY = poppedY + dy[3]
                    elif(resDistane == distance+1 and resIdxY == poppedY+dy[3] and resIdxX > poppedX+dx[3]):
                        resIdxX = poppedX + dx[3]
        
        if(poppedX + dx[1] < N):
            if(board[poppedY + dy[1]][poppedX + dx[1]] <= sharkSize):
                queue.append([poppedX + dx[1], poppedY + dy[1], distance+1])
                if(board[poppedY + dy[1]][poppedX + dx[1]] < sharkSize and board[poppedY + dy[1]][poppedX + dx[1]] != 0):
                    if(resDistane > distance+1):
                        resDistane = distance + 1
                        resIdxX = poppedX + dx[1]
                        resIdxY = poppedY + dy[1]
                    elif(resDistane == distance+1 and resIdxY > poppedY+dy[1]):
                        resIdxX = poppedX + dx[1]
                        resIdxY = poppedY + dy[1]
                    elif(resDistane == distance+1 and resIdxY == poppedY+dy[1] and resIdxX > poppedX+dx[1]):
                        resIdxX = poppedX + dx[1]
    
    if(resDistane == 10000):
        print(time)
        break

    board[resIdxY][resIdxX] = 0
    time += resDistane
    sharkExp += 1
    if(sharkExp == sharkSize):
        sharkSize += 1
        sharkExp = 0

    sharkIdxX = resIdxX
    sharkIdxY = resIdxY

