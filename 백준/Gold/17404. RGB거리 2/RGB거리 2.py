# RGB거리 2
import sys

N = int(sys.stdin.readline())
house = []
for _ in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))

res = sys.maxsize

for color in range(3):
    dp = [[sys.maxsize,sys.maxsize,sys.maxsize] for _ in range(N)]
    dp[0][color] = house[0][color]

    for i in range(1, N):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]
    
    for i in range(3):
        if(color != i):
            res = min(res, dp[N-1][i])

print(res)