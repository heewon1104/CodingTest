import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
heap = []

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (cost, start, end))

roots = [i for i in range(N+1)]
result = 0
countEdge = 0

def findRoots(node):
    if(roots[node] != node):
        roots[node] = findRoots(roots[node])
    return roots[node]

while(countEdge < N-2):
    currentCost, currentStart, currentEnd= heapq.heappop(heap)
    rootStart = findRoots(currentStart)
    rootEnd = findRoots(currentEnd)

    if(rootStart != rootEnd):
        if(rootStart < rootEnd):
            roots[rootEnd] = rootStart
        else:
            roots[rootStart] = rootEnd

        result += currentCost
        countEdge += 1
        
print(result)