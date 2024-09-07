import sys

N = int(input())

Graph = []
result = sys.maxsize

for _ in range(N):
    Graph.append(list(map(int, input().split())))


def Dfs(current, start, visited, total):
    global result

    if(not False in visited):
        if(Graph[current][start] != 0):
            result = min(result, total + Graph[current][start])
    
    else:
        for i in range(N):
            if(Graph[current][i] > 0 and visited[i] == False and  total+Graph[current][i] < result):
                visited[i] = True
                Dfs(i, start, visited, total + Graph[current][i])
                visited[i] = False

for i in range(N):
    visited = [False] * N
    visited[i] = True
    Dfs(i, i, visited ,0)

print(result)