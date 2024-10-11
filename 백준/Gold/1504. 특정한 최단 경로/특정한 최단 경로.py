import sys
import heapq

# 무한대를 sys.maxsize로 설정
INF = sys.maxsize

N, E = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    edges[start].append([end, cost])
    edges[end].append([start, cost])

V1, V2 = map(int, sys.stdin.readline().split())

def Dijkstra(start, end):
    cost = [sys.maxsize] * (N+1)
    cost[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while(heap):
        currentCost, currentNode = heapq.heappop(heap)
        for j in range(len(edges[currentNode])):
            nextNode, nextCost = edges[currentNode][j]
            if(nextCost >= cost[nextNode]):
                continue

            else:
                if(cost[nextNode] > cost[currentNode] + nextCost):
                    cost[nextNode] = cost[currentNode] + nextCost
                    heapq.heappush(heap, [cost[nextNode], nextNode])
    
    return cost[end]

# 시작점은 1로 설정 (문제에서 시작점은 1번 노드로 지정)
start = 1
end = N

# 세 가지 경로의 비용을 각각 계산
route1 = Dijkstra(start, V1) + Dijkstra(V1, V2) + Dijkstra(V2, end)
route2 = Dijkstra(start, V2) + Dijkstra(V2, V1) + Dijkstra(V1, end)

# 경로가 없을 경우(INF인 경우)를 처리
result = min(route1, route2)
if(result >= INF):
    print(-1)
else:
    print(result)
