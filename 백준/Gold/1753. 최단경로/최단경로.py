import heapq
import sys

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
start = int(input())

for _ in range(E):
    inputStart, inputEnd, inputCost = map(int, input().split())
    graph[inputStart].append([inputCost, inputEnd])

cost = [sys.maxsize]*(V+1)

heap = []
heapq.heappush(heap, (0, start))
cost[start] = 0

while(heap):
    currentCost, current = heapq.heappop(heap)
    for nextCost, next in graph[current]:
        if(currentCost + nextCost < cost[next]):
            heapq.heappush(heap, (currentCost + nextCost, next))
            cost[next] = currentCost + nextCost

for i in range(1, V+1):
    if(cost[i] != sys.maxsize):
        print(cost[i])
    else:
        print("INF")