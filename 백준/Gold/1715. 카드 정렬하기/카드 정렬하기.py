import heapq

N = int(input())
arr = []
total = 0
for _ in range(N):
    heapq.heappush(arr, int(input()))

while(len(arr) > 1):
    num1 = heapq.heappop(arr)
    num2  = heapq.heappop(arr)
    total += num1 + num2
    heapq.heappush(arr, num1+num2)

print(total)