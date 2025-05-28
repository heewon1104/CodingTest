import sys
sys.setrecursionlimit(10**7)

K = int(sys.stdin.readline())
result = True
stop = False

def DFS(node, visited, prevCheck, firstFlag):
    global result, stop

    if(stop):
        return
    
    if(firstFlag):
        if(visited[node] == 0):
            visited[node] = 1
    else:
        if(prevCheck == 2):
            visited[node] = 1
        elif(prevCheck == 1):
            visited[node] = 2
    
    for i in range(len(edges[node])):
        nextNode = edges[node][i]
        if(visited[nextNode] == 0):
            DFS(nextNode, visited, visited[node], False)
        else:
            if(visited[nextNode] == visited[node]):
                result = False
                stop = True
                return

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, sys.stdin.readline().split())
        edges[start].append(end)
        edges[end].append(start)

    visited = [0] * (V+1)
    for i in range(1, V+1):
        DFS(i, visited, 2, True)
    
    visited[0] = 2
    if(result):
        if(0 in visited):
             print("NO")
        else:
            print("YES")
    else:
        print("NO")

    result = True
    stop = False
