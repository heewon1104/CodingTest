from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    degree[end] += 1

queue = deque()
for i in range(1, N+1):
    if(degree[i] == 0):
        queue.append(i)

while(queue):
    popped = queue.popleft()
    print(popped, end=' ')
    for i in range(len(graph[popped])):
        next = graph[popped][i]
        degree[next] -= 1
        if(degree[next]==0):
            queue.append(next)


