import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
dp = [([0]*(N+1)) for _ in range(N+1)]

for card in range(1, N+1):
    for cost in range(1, N+1):
        dp[card][cost] = dp[card-1][cost]
        if(cost >= card):    
            tmpcost = cost
            idx = 0
            while(1):
                tmpcost -= card
                idx += 1
                if(tmpcost < 0):
                    break
                dp[card][cost] = max(dp[card][cost], cards[card-1]*idx + dp[card][tmpcost])



print(dp[N][N])

