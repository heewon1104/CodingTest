import sys
sys.setrecursionlimit(10**7)

N = int(input())
Board = []
Cuttings = []
CountWhite = 0
CountBlue = 0

for _ in range(N):
    Board.append(list(map(int, sys.stdin.readline().split())))

def checkPaper(StartX, StartY, EndX, EndY):
    value = Board[StartY][StartX]

    for i in range(StartY, EndY):
         for j in range(StartX, EndX):
             if(value != Board[i][j]):
                 return 0
    if(value == 0):
        return 1
    if(value == 1):
        return 2

def DividePaper(StartX, StartY, EndX, EndY):
    global CountWhite, CountBlue

    check = checkPaper(StartX, StartY, EndX, EndY) 
    if(check == 1):
        CountWhite += 1
        return
    elif(check == 2):
        CountBlue += 1
        return
    else:
        DividePaper(StartX, StartY, (EndX+StartX)//2, (EndY + StartY)//2)
        DividePaper((EndX+StartX)//2, StartY, EndX, (EndY + StartY)//2)
        DividePaper(StartX, (EndY + StartY)//2, (EndX+StartX)//2, EndY)
        DividePaper((EndX+StartX)//2, (EndY + StartY)//2, EndX, EndY)
    
DividePaper(0,0, N, N)
print(CountWhite)
print(CountBlue)