import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

dp = [sys.maxsize for _ in range(K+1)]
dp[0] = 0

for coin in coins:
    for i in range(coin, K+1):
        if(dp[i - coin] != sys.maxsize):
            dp[i] = min(dp[i], dp[i-coin]+1)

if(dp[K] == sys.maxsize):
    print(-1)
else:
    print(dp[K])