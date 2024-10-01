import sys

N, M = map(int, sys.stdin.readline().split())
board = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
dp = [([0] * N) for _ in range(N)]
dp[0][0] = board[0][0]

for i in range(1, N):
    dp[0][i] = board[0][i] + dp[0][i-1]
    dp[i][0] = board[i][0] + dp[i-1][0]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + board[i][j] - dp[i-1][j-1]

for i in range(M):
    startY, startX, endY, endX = map(int, sys.stdin.readline().split())
    startX -= 1
    startY -= 1
    endX -= 1
    endY -= 1

    
    if(startX == 0 and startY != 0):
        print(dp[endY][endX] - dp[startY-1][endX])
    elif(startX != 0 and startY == 0):
        print(dp[endY][endX] - dp[endY][startX-1])
    elif(startX == 0 and startY == 0):
        print(dp[endY][endX])
    else:
        print(dp[endY][endX] - dp[endY][startX-1] - dp[startY-1][endX] + dp[startY-1][startX-1])