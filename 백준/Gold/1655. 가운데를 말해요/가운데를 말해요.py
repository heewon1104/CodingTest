import heapq
import sys

N = int(input())

large = []  
small = [] 

for i in range(N):
    num = int(sys.stdin.readline())

    if len(large) == len(small):
        heapq.heappush(small, -num) 
    else:
        heapq.heappush(large, num) 
    
    if large and (-small[0] > large[0]):
        small_top = -heapq.heappop(small)
        large_top = heapq.heappop(large)
        heapq.heappush(small, -large_top)
        heapq.heappush(large, small_top)

    print(-small[0])
