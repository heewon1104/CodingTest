import sys

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
ZeroIdx = []
for i in range(9):
   for j in range(9):
       if board[i][j] == 0:
           ZeroIdx.append((i, j))

def CheckSector(x, y, num):
    boardX = x // 3 * 3
    boardY = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[boardY + i][boardX + j] == num:  # board[boardY + i][boardX + j]로 수정
                return False
    return True

def CheckRow(y, num):
    for i in range(9):
        if board[y][i] == num:  
            return False
    return True

def CheckColumn(x, num):
    for i in range(9):
        if board[i][x] == num:  
            return False
    return True

def DFS(idx):
    if idx == len(ZeroIdx):
        for i in range(9):
            print(''.join(map(str, board[i])))
        exit(0) 
    
    y, x = ZeroIdx[idx]  # x, y 순서를 맞추기 위해 y, x로 설정
    for i in range(1, 10):
        if CheckColumn(x, i) and CheckRow(y, i) and CheckSector(x, y, i):
            board[y][x] = i
            DFS(idx + 1)
            board[y][x] = 0

DFS(0)
