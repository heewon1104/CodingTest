import sys
import heapq

def changeDay(month, day):
    total = 0
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(month - 1):
        total += days_in_month[i]
    return total + day

flowers = []
N = int(sys.stdin.readline())
for _ in range(N):
    sm, sd, em, ed = map(int, sys.stdin.readline().split())
    start = changeDay(sm, sd)
    end = changeDay(em, ed)
    if end >= changeDay(3, 1) and start <= changeDay(11, 30):
        flowers.append((start, end))

flowers.sort()

heap = []
current_end = changeDay(3, 1)
end_goal = changeDay(11, 30)
count = 0
i = 0

while current_end <= end_goal:
    while i < len(flowers) and flowers[i][0] <= current_end:
        heapq.heappush(heap, -flowers[i][1]) 
        i += 1
    if not heap:
        count = 0
        break
    current_end = -heapq.heappop(heap)
    count += 1

print(count if current_end > end_goal else 0)
