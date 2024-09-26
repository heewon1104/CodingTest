import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
count = 0

for i in range(N-1, -1, -1):
    if(coins[i] <= K):
        count += K // coins[i]
        K %= coins[i]

print(count)