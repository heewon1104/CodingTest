N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

roots = [i for i in range(N+1)]
marged = 0

def findParent(node):
    while(roots[node] != node):
        node = roots[node]
    return node

for i in range(1, N+1):
    for j in range(len(graph[i])):
        if(findParent(i) != findParent(graph[i][j])):
            if(roots[i] < roots[graph[i][j]]):
                roots[graph[i][j]] = roots[i]
            else:
                roots[i] = roots[graph[i][j]]
            marged += 1

print(N-marged)