import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arcs = [[] for _ in range(N+1)]
heap = []
costs = [sys.maxsize for _ in range(N+1)]

for _ in range(M):
    start, end, value = map(int, sys.stdin.readline().split())
    arcs[start].append([end, value])

startNode, endNode = map(int, sys.stdin.readline().split())

def Dijkstra():
    heapq.heappush(heap, [0, startNode])
    costs[startNode] = 0

    while(heap):
        popvalue, popNode = heapq.heappop(heap) 
        if(popvalue > costs[popNode]):
            continue
        for i in range(len(arcs[popNode])):
            nextNode = arcs[popNode][i]
            if(costs[nextNode[0]] > nextNode[1] + costs[popNode]):
                costs[nextNode[0]] = nextNode[1] + costs[popNode]
                heapq.heappush(heap, [nextNode[1], nextNode[0]])
    
    print(costs[endNode])

Dijkstra()