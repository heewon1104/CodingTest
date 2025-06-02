import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    inputStart, inputEnd, inputCost = map(int, sys.stdin.readline().split())
    graph[inputStart].append((inputCost, inputEnd))

start, end = map(int, sys.stdin.readline().split())

cost = [sys.maxsize] * (N+1)
heap = []
heapq.heappush(heap, (0, start))
cost[start] = 0

while(heap):
    currentCost, current = heapq.heappop(heap)
    if(current == end):
        break
    
    for nextCost, next in graph[current]:
        if(nextCost + currentCost < cost[next]):
            cost[next] = nextCost + currentCost
            heapq.heappush(heap, (nextCost + currentCost, next))

print(cost[end])
