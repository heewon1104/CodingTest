import heapq
import sys

N = int(input())
numList = []

for i in range(N):
    num = int(sys.stdin.readline())
    if(num == 0):
        if(len(numList) == 0):
            print(0)
        else:
            print(-1 * heapq.heappop(numList))
    
    else:
        heapq.heappush(numList, -1 * num)

