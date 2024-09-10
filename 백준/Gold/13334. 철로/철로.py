import heapq
N = int(input())

arr = []
trailAvailable = []
idxSet = []
maxPeople = 0

startpoint = 0

for _ in range(N):
    start, end = map(int, input().split())
    arr.append([min(start, end), max(start, end)])

distance = int(input())

# 시작점을 기준으로 정렬
arr.sort(key= lambda x : (x[1], x[0]))

trailStart = arr[0][0]

for i in range(N):
    start,end = arr[i][0],arr[i][1] 

    heapq.heappush(trailAvailable, [start, end])

    checkStart = end - distance

    while(trailAvailable):
        if(checkStart > trailAvailable[0][0]):
            heapq.heappop(trailAvailable)
        else:
            break
    
    maxPeople = max(maxPeople, len(trailAvailable))

print(maxPeople)