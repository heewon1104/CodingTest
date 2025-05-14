import sys
import heapq

N = int(sys.stdin.readline())

homes = []
for _ in range(N):
    inputArr = list(map(int, sys.stdin.readline().split()))
    homes.append([min(inputArr), max(inputArr)])
D = int(sys.stdin.readline())

homes.sort(key=lambda x: (x[0], x[1]))

heap = []
result = 0

for i in range(N-1, -1, -1):
    if(homes[i][1] - homes[i][0] > D):
        continue
    else:
        if(not heap or -heap[0] - homes[i][0] <= D):
            heapq.heappush(heap, -homes[i][1])
            result = max(result, len(heap))
        else:
            while(heap and -heap[0] - homes[i][0] > D):
                heapq.heappop(heap)
            heapq.heappush(heap, -homes[i][1])
            result = max(result, len(heap))
print(result)
            