import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
items = []
for _ in range(N):
    weight, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(items, [weight, cost])

dp = [([0] * (K+1)) for _ in range(N+1)]

for i in range(1, N+1):
    currentWeight, currentCost =  heapq.heappop(items)
    for j in range(1, K+1):
        if(j < currentWeight):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(currentCost + dp[i-1][j-currentWeight], dp[i][j-1], dp[i-1][j])


print(dp[N][K])