import sys
import copy
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

def dfs(y, x):
    checkBaord[y][x] = 2
    if(y+1 < N):
        if(checkBaord[y+1][x] == 0):
            dfs(y+1,x)
    if(y-1 >= 0):
        if(checkBaord[y-1][x] == 0):
            dfs(y-1,x)
    if(x+1 < M):
        if(checkBaord[y][x+1] == 0):
            dfs(y,x+1)
    if(x-1 >= 0):
        if(checkBaord[y][x-1] == 0):
            dfs(y,x-1)

def increaseIdx(x, y):
    resX = x+1
    resY = y
    while(True):
        if(resX >= M):
            resY += 1
            resX = 0
        if(resY >= N):
            break
        if(board[resY][resX] == 0):
            break
        resX += 1
    return resX, resY

def printBoard():
    for i in range(N):
        print(checkBaord[i])
    print()

firstIdxX, firstIdxY = 0,0
if(board[0][0] != 0):
    firstIdxX, firstIdxY = increaseIdx(0,0)
maxValue = 0
while(firstIdxX < M and firstIdxY < N):
    secondIdxX, secondIdxY = increaseIdx(firstIdxX, firstIdxY)
    while(secondIdxX < M and secondIdxY < N):
        thirdIdxX, thirdIdxY = increaseIdx(secondIdxX, secondIdxY)
        while(thirdIdxX < M and thirdIdxY < N):
            checkBaord = copy.deepcopy(board)
            checkBaord[firstIdxY][firstIdxX] = 1
            checkBaord[secondIdxY][secondIdxX] = 1
            checkBaord[thirdIdxY][thirdIdxX] = 1
            for i in range(N):
                for j in range(M):
                    if(checkBaord[i][j] == 2):
                        dfs(i, j)
            count = 0
            for i in range(N):
                for j in range(M):
                    if(checkBaord[i][j] == 0):
                        count += 1
            maxValue = max(maxValue, count)
            checkBaord = copy.deepcopy(board)
            thirdIdxX, thirdIdxY = increaseIdx(thirdIdxX, thirdIdxY)
        secondIdxX, secondIdxY = increaseIdx(secondIdxX, secondIdxY)
    firstIdxX, firstIdxY = increaseIdx(firstIdxX, firstIdxY)
print(maxValue)

            