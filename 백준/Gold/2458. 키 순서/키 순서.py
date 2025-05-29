N, M = map(int, input().split())
graph = [([False] * (N+1)) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = True

for i in range(1, N+1):
    graph[i][i] = True

for via in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            if(graph[start][via] and graph[via][end]):
                graph[start][end] = True

result = 0
for check in range(1, N+1):
    flag = True
    for idx in range(1, N+1):
        if(not graph[check][idx] and not graph[idx][check]):
            flag = False
            break
    if(flag):
        result += 1
print(result)