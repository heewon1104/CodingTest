import sys

N, K= map(int, sys.stdin.readline().split())
coins =[int(sys.stdin.readline()) for _ in range(N)]
dp = [0]*(K+1)

for i in range(1, N+1):
    for cost in range(0, K+1):
        if(cost == 0):
            dp[cost] = 1
        else:
            if(cost >= coins[i-1]):
                dp[cost] = dp[cost] + dp[cost-coins[i-1]]

print(dp[K])