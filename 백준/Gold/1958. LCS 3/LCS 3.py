import sys

str1 = list(sys.stdin.readline().rstrip('\n'))
str2 = list(sys.stdin.readline().rstrip('\n'))
str3 = list(sys.stdin.readline().rstrip('\n'))

N = len(str1)
M = len(str2)
L = len(str3)

dp = [([([0]*(M+1)) for _ in range(N+1)]) for _ in range(L+1)]

for k in range(L):
    for i in range(N):
        for j in range(M):
            if(str1[i] == str2[j] == str3[k]):
                dp[k+1][i+1][j+1] = dp[k][i][j] + 1

            else:
                dp[k+1][i+1][j+1] = max(dp[k+1][i+1][j],  dp[k+1][i][j+1],  dp[k][i+1][j+1])

print(dp[L][N][M])