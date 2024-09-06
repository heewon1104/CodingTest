n = int(input())
graph = []
minNum = 1e8

for i in range(n):
    graph.append(list(map(int, input().split())))

def Dfs(num, start, visited, total):
    global minNum

    if(False not in visited):
        if(graph[num][start] > 0):
            total += graph[num][start]
            minNum = min(minNum, total)
        return
    

    for i in range(n):
        if (graph[num][i] != 0) and (not visited[i]) and (total < minNum):
            visited[i] = True
            tmp = total +graph[num][i]
            Dfs(i, start,visited, tmp)
            visited[i] = False

for i in range(n):
    visited = [False] * n
    visited[i] = True
    Dfs(i, i, visited, 0)

print(minNum)



