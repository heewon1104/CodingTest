import sys
import heapq

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]

degree = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]
countResultIdx = N

for i in range(1, N+1):
    inputstr = list(sys.stdin.readline().rstrip('\n'))
    
    for idx, val in enumerate(inputstr):
        if(val == '1'):
            graph[idx+1].append(i)
            degree[i] += 1

def topology_sort():
    global countResultIdx

    queue = []
    for i in range(1, N+1):
        if(degree[i] == 0):
            heapq.heappush(queue, -i)
    
    while(queue):
        popnum = -heapq.heappop(queue)
        result[popnum] = countResultIdx

        for i in graph[popnum]:
            degree[i] -= 1
            if(degree[i] == 0):
                heapq.heappush(queue, -(i))
        
        countResultIdx -= 1

topology_sort()


if result.count(0) > 2:
    print(-1)
else:
    print(' '.join(map(str, result[1:])))