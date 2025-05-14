import heapq
import sys

N = int(input())
heap = []

for _ in range(N):
    inputNum = int(sys.stdin.readline())
    if(inputNum == 0):
        if(not heap):
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -inputNum)