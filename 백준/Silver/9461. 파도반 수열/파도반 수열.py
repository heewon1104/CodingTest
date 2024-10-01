import sys

T = int(sys.stdin.readline())
inputArr = [int(sys.stdin.readline()) for _  in range(T)]
maxnum = max(inputArr)
if(maxnum < 4):
    maxnum = 4
dp = [0] * (maxnum+1)

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5, maxnum+1):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(T):
    print(dp[inputArr[i]])