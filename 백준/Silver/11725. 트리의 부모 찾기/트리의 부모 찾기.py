from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

parent = [1] * (N+1)
visit = [False] * (N+1)

queue = deque()
queue.append(1)
visit[1] = True

while(queue):
    popped = queue.popleft()
    for next in graph[popped]:
        if not visit[next]:
            parent[next] = popped
            queue.append(next)
            visit[next] = True

for result in range(2, N+1):
    print(parent[result])