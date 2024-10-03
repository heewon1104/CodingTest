import sys

N = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))

mincost = costs[0]
res = costs[0] * roads[0]
for i in range(1, N-1):
    mincost = min(mincost, costs[i])
    res += roads[i]*mincost

print(res)