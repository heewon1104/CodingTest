import copy

block = [
    #y,x
    [[0,0],[0,1],[1,0],[1,1]],

    [[0,0],[1,0],[2,0],[3,0]],
    [[0,0],[0,1],[0,2],[0,3]],

    [[0,0],[0,1],[0,2],[1,1]], 
    [[0,0],[1,0],[2,0],[1,1]], 
    [[1,0],[1,1],[0,1],[2,1]], 
    [[0,1],[1,1],[1,2],[1,0]], 

    [[0,0],[1,0],[1,1],[2,1]],
    [[1,0],[1,1],[0,1],[0,2]],
    [[2,0],[1,0],[1,1],[0,1]],
    [[0,0],[0,1],[1,1],[1,2]],

    [[0,0],[1,0],[2,0],[2,1]],
    [[1,0],[1,1],[1,2],[0,2]],
    [[0,0],[0,1],[1,1],[2,1]],
    [[0,0],[1,0],[0,1],[0,2]],

    [[2,0],[2,1],[1,1],[0,1]],
    [[0,0],[1,0],[1,1],[1,2]],
    [[0,0],[0,1],[1,0],[2,0]],
    [[0,0],[0,1],[0,2],[1,2]]
]

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

maxValue = 0
for i in block:
    copyBlock = copy.deepcopy(i)
    y = 0
    while(True):
        x = 0
        catchexceptX = -1
        catchexceptY = -1
        while(True):
            total = 0
            try:
                for j in range(4):
                    catchexceptY = copyBlock[j][0] + y
                    catchexceptX = copyBlock[j][1] + x
                    total += board[copyBlock[j][0] + y][copyBlock[j][1] + x]
            
            except IndexError:
                break
            
            maxValue = max(total, maxValue)
            x += 1
        if(catchexceptY >= N):
            break
        y += 1

print(maxValue)