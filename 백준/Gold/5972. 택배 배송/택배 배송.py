# 택배 배송
import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    edge[start].append([end, cost])
    edge[end].append([start, cost])
visited = [sys.maxsize] * (N+1)
visited[1] = 0
heap = [[0, 1]]

while(heap):
    totalCost, current = heapq.heappop(heap)
    for i in range(len(edge[current])):
        nextNode = edge[current][i][0]
        nextCost = edge[current][i][1]
        if(visited[nextNode] <= totalCost + nextCost):
            continue
        visited[nextNode] = totalCost + nextCost
        heapq.heappush(heap, [visited[nextNode], nextNode])
print(visited[N])