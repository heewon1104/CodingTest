import sys

str1 = list(sys.stdin.readline().rstrip('\n'))
str2 = list(sys.stdin.readline().rstrip('\n'))

N = len(str1)
M = len(str2)

dp = [([0]*(M+1)) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if(str1[i] == str2[j]):
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])


print(dp[N][M])

res = []
X = M-1
Y = N-1

while(1):
    if(dp[Y+1][X+1] == 0):
        break

    if(dp[Y+1][X+1] == dp[Y][X+1]):
        Y-=1
    elif(dp[Y+1][X+1] == dp[Y+1][X]):
        X-=1
    else:
        res.append(str2[X])
        X -= 1
        Y -= 1

for i in range(len(res)-1, -1, -1):
    print(res[i], end='')
