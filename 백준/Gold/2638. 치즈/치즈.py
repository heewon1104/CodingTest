import sys
import copy
from collections import deque
N, M = map(int, input().split())

board = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))

def bfs(X, Y, num):
    visit = [([0] * M) for _ in range(N)]
    queue = deque()
    queue.append([X, Y])

    while(queue):
        poppedX, poppedY = queue.popleft()

        if(visit[poppedY][poppedX] != 0):
            continue

        visit[poppedY][poppedX] = 1
        board[poppedY][poppedX] = num
        
        for i in range(4):
            if(poppedX+dx[i]<0 or poppedX+dx[i]>=M or poppedY+dy[i]<0 or poppedY+dy[i]>=N):
                continue
            if(board[poppedY+dy[i]][poppedX+dx[i]] != 0):
                continue
            queue.append([poppedX+dx[i],poppedY+dy[i]])

def chcekBoard():
    for i in range(N):
        for j in range(M):
            if(board[i][j] == 1):
                return False
    return True

bfs(0,0,2)
count = 0
while(True):
    if(chcekBoard()):
        print(count)
        break

    tmpBoard = copy.deepcopy(board)
    for i in range(1,N-1):
        for j in range(1, M-1):
            if(board[i][j] == 1):
                chcekOutside = 0
                for k in range(4):
                    if(board[i+dy[k]][j+dx[k]]==2):
                        chcekOutside += 1
                if(chcekOutside > 1):
                    tmpBoard[i][j] = 2
    
    board = copy.deepcopy(tmpBoard)

    for i in range(1,N):
        for j in range(1, M):
            if(board[i][j] == 0):
                chcekInside = False
                for k in range(4):
                    if(board[i+dy[k]][j+dx[k]]==2):
                        chcekInside += True
                        break
                if(chcekInside):
                    bfs(j, i, 2)
    count += 1

                

