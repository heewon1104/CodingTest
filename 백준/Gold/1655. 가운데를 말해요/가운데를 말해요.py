import heapq
import sys

N = int(input())

largeHeap = []
smallHeap = []

for i in range(N):
    inputNum = int(sys.stdin.readline())
    if(not largeHeap or largeHeap[0] < inputNum):
        heapq.heappush(largeHeap, inputNum)
    else:
        heapq.heappush(smallHeap, -inputNum)
    
    if((len(largeHeap) + len(smallHeap)) % 2 == 1):
        if(len(largeHeap) > len(smallHeap)):
            print(largeHeap[0])
        else:
            print(-smallHeap[0])
    else:
        if(len(largeHeap) > len(smallHeap)):
            heapq.heappush(smallHeap, -heapq.heappop(largeHeap))
        elif(len(largeHeap) < len(smallHeap)):
            heapq.heappush(largeHeap, -heapq.heappop(smallHeap))

        print(min(largeHeap[0], -smallHeap[0]))

