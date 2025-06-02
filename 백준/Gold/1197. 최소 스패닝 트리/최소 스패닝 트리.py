import sys
import heapq
sys.setrecursionlimit(10**7)

V, E = map(int, sys.stdin.readline().split())
heap = []

for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, [cost, start, end])

roots = [i for i in range(V+1)]
edgeCount = 0
result = 0

def findRoot(node):
    if(roots[node] != node):
        roots[node] = findRoot(roots[node])
    return roots[node]

while(edgeCount < V-1):
    poppedCost, poppedStart, poppedEnd = heapq.heappop(heap)
    startRoot = findRoot(poppedStart)
    endRoot = findRoot(poppedEnd)

    if(startRoot != endRoot):
        if(startRoot < endRoot):
            roots[endRoot] = poppedStart
        elif(startRoot > endRoot):
            roots[startRoot] = poppedEnd
        result += poppedCost
        edgeCount += 1

print(result)