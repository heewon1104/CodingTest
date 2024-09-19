import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
value = sys.stdin.readline().rstrip('\n')
edges = list([] for _ in range(N+1))

for _ in range(N-1):
    num1, num2 = map(int, sys.stdin.readline().split())
    edges[num1].append(num2)
    edges[num2].append(num1)

Count = 0

def Dfs(node, visited, firstFlag):
    global Count
    visited[node] = True
    
    if(not firstFlag and value[node-1] == '1'):
        Count+= 1
        return
    
    for i in range(len(edges[node])):
        nextnode = edges[node][i]
        if(not visited[nextnode]):
            Dfs(nextnode, visited, False)


for i in range(1, N+1):
    if(value[i-1] == '1'):
        visited = [False] * (N+1)
        Dfs(i, visited, True)
    
print(Count)