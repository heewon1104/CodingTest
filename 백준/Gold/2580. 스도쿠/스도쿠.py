# 스토쿠
import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
location = []

for i in range(9):
    for j in range(9):
        if(board[i][j] == 0):
            location.append([j, i])

def checkSide(X, Y):
    for i in range(9):
        if(i == Y):
            continue
        if(board[Y][X] == board[i][X]):
            return False
    for i in range(9):
        if(i == X):
            continue
        if(board[Y][X] == board[Y][i]):
            return False
    return True

def checkArea(X, Y):
    areaX = (X//3)*3
    areaY = (Y//3)*3

    for i in range(areaY, areaY+3):
        for j in range(areaX, areaX+3):
            if(i == Y and j == X):
                continue
            if(board[Y][X] == board[i][j]):
                return False
    return True

locationIdx = 0
def Dfs():
    global locationIdx
    if(locationIdx == len(location)):
        for i in board:
            print(' '.join(map(str, i)))
        exit()

    currentX, currentY = location[locationIdx]

    for i in range(1, 10):
        board[currentY][currentX] = i
        if(checkSide(currentX, currentY) and checkArea(currentX, currentY)):
            board[currentY][currentX] = i
            locationIdx += 1
            Dfs()
    
    board[currentY][currentX] = 0
    locationIdx -= 1

Dfs()
