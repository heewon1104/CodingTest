# 강의실 배정
import sys
import heapq

N = int(sys.stdin.readline())
lectures = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lectures.append([start, end])
lectures.sort()

heap = []
heapq.heappush(heap, lectures[0][1])

for i in range(1, N):
    currentStart, currentEnd = lectures[i]
    if(heap[0] > currentStart):
        heapq.heappush(heap, currentEnd)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, currentEnd)

print(len(heap))