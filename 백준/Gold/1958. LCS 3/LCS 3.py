# LCS 3
import sys
strArr = []
for _ in range(3):
    strArr.append(list(sys.stdin.readline().rstrip('\n')))

length1, length2, length3 = len(strArr[2]), len(strArr[1]), len(strArr[0])

dp = []
for _ in range(length1+1):
    apeendArr = [([0] * (length3+1)) for _ in range(length2+1)]
    dp.append(apeendArr)

for i in range(length1):
    for j in range(length2):
        for k in range(length3):
            if(strArr[0][k] == strArr[1][j] == strArr[2][i]):
                dp[i+1][j+1][k+1] = dp[i][j][k] + 1
            else:
                dp[i+1][j+1][k+1] = max(dp[i][j+1][k+1], dp[i+1][j][k+1], dp[i+1][j+1][k])


print(dp[length1][length2][length3])

