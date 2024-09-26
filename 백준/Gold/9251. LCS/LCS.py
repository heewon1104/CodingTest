import sys

str1 = list(sys.stdin.readline().rstrip('\n'))
str2 = list(sys.stdin.readline().rstrip('\n'))

N = len(str1) 
M = len(str2) 

dp = [([0]* (M+1)) for _ in range(N+1)]
letterCount = [0] * 52


for i in range(N):
    count = 0
    for j in range(M):
        if(str1[i] == str2[j]):
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    letterCount[ord(str1[i]) - 64] += 1

print(dp[N][M])