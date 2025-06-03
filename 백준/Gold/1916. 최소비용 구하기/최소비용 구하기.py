import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    inputStart, inputEnd, inputCost = map(int, sys.stdin.readline().split())
    graph[inputStart].append([inputEnd, inputCost])

start, end = map(int, sys.stdin.readline().split())
cost = [sys.maxsize] * (N+1)
cost[start] = 0
heap = []
heapq.heappush(heap, (0, start))

while(heap):
    currentCost, currentNode = heapq.heappop(heap)
    if(currentNode == end):
        break
    
    for nextNode, nextCost in graph[currentNode]:
        if(currentCost+nextCost < cost[nextNode]):
            heapq.heappush(heap, (currentCost+nextCost, nextNode))
            cost[nextNode] = currentCost+nextCost

print(cost[end])
