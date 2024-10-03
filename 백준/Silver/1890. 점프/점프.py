import sys

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [([0] * N) for _ in range(N)]
dp[0][0] = 1

def DP():
    for i in range(0, N):
        for j in range(i, N):
            if(i == N-1 and j == N-1):
                break
            nextX = j + board[i][j]
            nextY = i + board[i][j]
            if(dp[i][j] != 0):
                if(nextX < N):
                    dp[i][nextX] += dp[i][j]
                if(nextY < N):
                    dp[nextY][j] += dp[i][j]
            
            nextX2 = i + board[j][i]
            nextY2 = j + board[j][i]
            if(dp[j][i] != 0 and i != j):
                if(nextX2 < N):
                    dp[j][nextX2] += dp[j][i]
                if(nextY2 < N):
                    dp[nextY2][i] += dp[j][i]
DP()
print(dp[N-1][N-1])