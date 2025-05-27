from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N+1):
    graph[i].sort()

def DFS(current, visit):
    visit[current] = True
    print(current, end=" ")
    for i in range(len(graph[current])):
        next = graph[current][i]
        if(not visit[next]):
            DFS(next, visit)

def BFS(start):
    visit = [False] * (N+1)
    visit[0] = True

    queue = deque()
    queue.append(start)
    visit[start] = True

    while(queue):
        current = queue.popleft()
        print(current, end=" ")
        for i in range(len(graph[current])):
            next = graph[current][i]
            if(not visit[next]):
                queue.append(next)
                visit[next] = True

visit = [False] * (N+1)
visit[0] = True
DFS(V, visit)
print()
BFS(V)