import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
board = []
RedStartX, RedStartY = 0,0
BlueStartX, BlueStartY = 0,0
endX, endY = 0,0
Result = 0

for i in range(N):
    inputStr = list(sys.stdin.readline().rstrip('\n'))
    board.append(inputStr)

    for j in range(M):
        if(inputStr[j] == 'B'):
            BlueStartX, BlueStartY = j, i
            board[i][j] = '.'
        elif(inputStr[j] == 'R'):
            RedStartX, RedStartY = j, i
            board[i][j] = '.'
        elif(inputStr[j] == 'O'):
            endX, endY = j, i

def MoveBall(X, Y, Direction, Letter, otherX, otherY):
    if(Direction == 'L'):
        for i in range(X, -1, -1):
            if(board[Y][i] == 'O'):
                X, Y = endX, endY
                break
            elif(board[Y][i] != '.' or (otherX == i and otherY == Y)):
                X = i+1
                break

    elif(Direction == 'R'):
        for i in range(X, M):
            if(board[Y][i] == 'O'):
                X, Y = endX, endY
                break
            elif(board[Y][i] != '.' or (otherX == i and otherY == Y)):
                X = i-1
                break

    elif(Direction == 'U'):
        for i in range(Y, -1, -1):
            if(board[i][X] == 'O'):
                X, Y = endX, endY
                break
            elif(board[i][X] != '.' or (otherX == X and otherY == i)):
                Y = i+1
                break

    else:
        for i in range(Y, N):
            if(board[i][X] == 'O'):
                X, Y = endX, endY
                break
            elif(board[i][X] != '.' or (otherX == X and otherY == i)):
                Y = i-1
                break
    
    return X, Y

def MoveBoard(RedX, RedY, BlueX, BlueY, Direction):
    if(Direction == 'L'):
        if(RedY == BlueY):
            if(RedX < BlueX):
                RedX, RedY = MoveBall(RedX, RedY, 'L', 'R', BlueX, BlueY)
                BlueX, BlueY = MoveBall(BlueX, BlueY, 'L', 'B', RedX, RedY)
            else:
                BlueX, BlueY = MoveBall(BlueX, BlueY, 'L', 'B', RedX, RedY)
                RedX, RedY = MoveBall(RedX, RedY, 'L', 'R', BlueX, BlueY)
        else:
            RedX, RedY = MoveBall(RedX, RedY, 'L', 'R', BlueX, BlueY)
            BlueX, BlueY = MoveBall(BlueX, BlueY, 'L', 'B', RedX, RedY)

    elif(Direction == 'R'):
        if(RedY == BlueY):
            if(RedX < BlueX):
                BlueX, BlueY = MoveBall(BlueX, BlueY, 'R', 'B', RedX, RedY)
                RedX, RedY = MoveBall(RedX, RedY, 'R', 'R', BlueX, BlueY)
            else:
                RedX, RedY = MoveBall(RedX, RedY, 'R', 'R', BlueX, BlueY)
                BlueX, BlueY = MoveBall(BlueX, BlueY, 'R', 'B', RedX, RedY)
        else:
            RedX, RedY = MoveBall(RedX, RedY, 'R', 'R', BlueX, BlueY)
            BlueX, BlueY = MoveBall(BlueX, BlueY, 'R', 'B', RedX, RedY)

    elif(Direction == 'U'):
        if(RedX == BlueX):
            if(RedY < BlueY):
                RedX, RedY = MoveBall(RedX, RedY, 'U', 'R', BlueX, BlueY)
                BlueX, BlueY = MoveBall(BlueX, BlueY, 'U', 'B', RedX, RedY)
            else:
                BlueX, BlueY = MoveBall(BlueX, BlueY, 'U', 'B', RedX, RedY)
                RedX, RedY = MoveBall(RedX, RedY, 'U', 'R', BlueX, BlueY)
        else:
            RedX, RedY = MoveBall(RedX, RedY, 'U', 'R', BlueX, BlueY)
            BlueX, BlueY = MoveBall(BlueX, BlueY, 'U', 'B', RedX, RedY)
    
    else:
        if(RedX == BlueX):
            if(RedY < BlueY):
                BlueX, BlueY = MoveBall(BlueX, BlueY, 'D', 'B', RedX, RedY)
                RedX, RedY = MoveBall(RedX, RedY, 'D', 'R', BlueX, BlueY)
            else:
                RedX, RedY = MoveBall(RedX, RedY, 'D', 'R', BlueX, BlueY)
                BlueX, BlueY = MoveBall(BlueX, BlueY, 'D', 'B', RedX, RedY)
        else:
            RedX, RedY = MoveBall(RedX, RedY, 'D', 'R', BlueX, BlueY)
            BlueX, BlueY = MoveBall(BlueX, BlueY, 'D', 'B', RedX, RedY)

    return [RedX, RedY, BlueX, BlueY]

def BFS(RedX, RedY, BlueX, BlueY):
    global Result

    queue = deque()
    queue.append((RedX, RedY, BlueX, BlueY, 0)) 
    
    while queue:
        RedX, RedY, BlueX, BlueY, count = queue.popleft()

        if count >= 10:
            Result = -1
            return

        for direction in ['L', 'R', 'U', 'D']:
            next_state = MoveBoard(RedX, RedY, BlueX, BlueY, direction)
            nextRedX, nextRedY, nextBlueX, nextBlueY = next_state[:4]

            if nextBlueX == endX and nextBlueY == endY:
                continue

            if nextRedX == endX and nextRedY == endY:
                Result = count + 1
                return

            queue.append((nextRedX, nextRedY, nextBlueX, nextBlueY, count + 1))

    Result -= 1




BFS(RedStartX, RedStartY, BlueStartX, BlueStartY)
print(Result)