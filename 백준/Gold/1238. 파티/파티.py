import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())
arcs = [[] for _ in range(N+1)]
timesParty = [sys.maxsize for _ in range(N+1)]
timesHome = [sys.maxsize for _ in range(N+1)]

for i in range(M):
    start, end , time = map(int, sys.stdin.readline().split())
    arcs[start].append([end, time])

def FirstDijkstra(startNode):
    heap = []
    heapq.heappush(heap, [0, startNode])
    times = [sys.maxsize for _ in range(N+1)]
    times[startNode] = 0
    
    while(heap):
        currentTime, currentNode = heapq.heappop(heap)

        if(times[currentNode] < currentTime):
            continue

        for i in range(len(arcs[currentNode])):
            nextNode, nextTime = arcs[currentNode][i]

            tmp = min(times[nextNode], times[currentNode] + nextTime)
            if(tmp !=  times[nextNode]):
                times[nextNode] = tmp
                heapq.heappush(heap, [times[nextNode], nextNode])
        
    timesParty[startNode] = times[X]

def SrcondDijkstra(startNode):
    heap = []
    heapq.heappush(heap, [0, startNode])
    timesHome[startNode] = 0
    
    while(heap):
        currentTime, currentNode = heapq.heappop(heap)

        if(timesHome[currentNode] < currentTime):
            continue

        for i in range(len(arcs[currentNode])):
            nextNode, nextTime = arcs[currentNode][i]

            tmp = min(timesHome[nextNode], timesHome[currentNode] + nextTime)
            if(tmp !=  timesHome[nextNode]):
                timesHome[nextNode] = tmp
                heapq.heappush(heap, [timesHome[nextNode], nextNode])


for i in range(1, N+1):
    if(i == X):
        continue
    FirstDijkstra(i)
SrcondDijkstra(X)

res = 0

for i in range(1, N+1):
    if(i == X):
        continue
    res = max(timesParty[i] + timesHome[i], res)

print(res)