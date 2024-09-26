import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    total = int(sys.stdin.readline())
    dp = [0] * (total+1)
    
    for coin in coins:
        for i in range(1, total+1):
            if(i == coin):
                dp[coin] += 1

            if(i - coin > 0):
                dp[i] = dp[i-coin] + dp[i]

    print(dp[total])