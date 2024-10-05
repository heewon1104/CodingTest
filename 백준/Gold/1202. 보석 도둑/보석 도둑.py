import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewel = []

for i in range(N):
    weight, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, [weight, cost])

bags = [int(sys.stdin.readline()) for _ in range(K)]
bags.sort()


res = 0
tmpheap = []
for i in range(K):
    currentBag = bags[i]

    for j in range(len(jewel)):
        currentW, currentC = heapq.heappop(jewel)
        
        if(currentW > currentBag):
            heapq.heappush(jewel, [currentW, currentC])
            break

        heapq.heappush(tmpheap, [-currentC, currentW])
    
    if(len(tmpheap) > 0):
        C, W = heapq.heappop(tmpheap)
        res -= C

print(res)