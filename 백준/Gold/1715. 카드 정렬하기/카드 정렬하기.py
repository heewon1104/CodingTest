import heapq

n = int(input())
arr = []
count = 0

for _ in range(n):
    heapq.heappush(arr, int(input()))

while(len(arr) != 1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    count += a
    count += b
    heapq.heappush(arr, a+b)

print(count)