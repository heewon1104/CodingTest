import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
value = sys.stdin.readline().rstrip('\n')
edges = list([] for _ in range(N+1))
Count = 0

for _ in range(N-1):
    num1, num2 = map(int, sys.stdin.readline().split())
    edges[num1].append(num2)
    edges[num2].append(num1)
    if(value[num1-1] == '1' and value[num2-1] == '1'):
        Count += 2


def Dfs(node, visited, firstFlag):
    insideCount = 0
    visited[node] = True

    for i in range(len(edges[node])):
        nextnode = edges[node][i]
        if(value[nextnode-1] == '1'):
            insideCount += 1
        elif(not visited[nextnode] and value[nextnode-1] == '0'):
            insideCount += Dfs(nextnode, visited, False)
        
    return insideCount


visited = [False] * (N+1)
for i in range(1, N+1):
    if(value[i-1] == '0' and not visited[i]):
        total = Dfs(i, visited, True)
        Count += total * (total-1)
print(Count)