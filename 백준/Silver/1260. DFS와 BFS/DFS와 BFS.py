import sys
from collections import deque
sys.setrecursionlimit(10**7)

N, M, V = map(int, sys.stdin.readline().split())
edges = list([] for _ in range(N+1))

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    edges[start].append(end)
    edges[end].append(start)

for i in range(1, N+1):
    edges[i].sort()

def Dfs(node, visited):
    if(visited[node]):
        return
    visited[node] = True
    print(node, end=' ')
    for i in range(len(edges[node])):
        Dfs(edges[node][i], visited)

def Bfs(start):
    queue = deque()
    queue.append(start)
    visited = [False] * (N+1)
    
    while(queue):
        node = queue.popleft()
        visited[node] = True
        print(node, end=' ')

        for i in range(len(edges[node])):
            if(visited[edges[node][i]] == False):
                queue.append(edges[node][i])
                visited[edges[node][i]] = True

visited = [False] * (N+1)   
Dfs(V, visited)
print()
Bfs(V)
print()
