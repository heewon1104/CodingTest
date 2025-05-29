import sys

N = int(input())
M = int(input())
graph = [([sys.maxsize] * (N+1)) for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start][end] = min(graph[start][end], cost)

for via in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            if(via != start and via != end and start != end):
                graph[start][end] = min(graph[start][end], graph[start][via] + graph[via][end])

for i in range(1, N+1):
    for j in range(1, N+1):
        if(graph[i][j] != sys.maxsize):
            print(graph[i][j], end=' ')
        else:
            print(0, end=' ')
    print()
