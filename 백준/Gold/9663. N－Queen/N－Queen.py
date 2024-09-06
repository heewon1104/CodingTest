import copy

N = int(input())

Board = [0 for _ in range(N)]
Count = 0   

def checkPlace(y):
    for i in range(y):
        if(Board[y] == Board[i] or abs(Board[y] - Board[i]) == abs(y - i)):
            return False
    return True

def placeQueen(y):
    global Count

    if(y == N):
        Count += 1
    else:
        for i in range(N):
            Board[y] = i
            if(checkPlace(y)):
                placeQueen(y+1)

          
placeQueen(0)
print(Count)



