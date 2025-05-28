N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visit = [False] * (N+1)
visit[1] = True
infected = 0

def DFS(current):
    global infected
    
    for next in graph[current]:
        if(not visit[next]):
            visit[next] = True
            infected += 1
            DFS(next)

DFS(1)
print(infected)