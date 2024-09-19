import sys
sys.setrecursionlimit(10**5)

N, M = map(int, sys.stdin.readline().split())
heavyList = [[] for _ in range(N+1)]
lightList = [[] for _ in range(N+1)]
count = 0
lefthalf = (N+1)//2
if(N %2 == 1):
    righthalf = (N+1)//2
else:
    righthalf = (N+1)//2 + 1


for i in range(M):
    heavy, light = map(int, sys.stdin.readline().split())
    heavyList[light].append(heavy)
    lightList[heavy].append(light)

def lightDfs(node, visited):
    count = 1
    visited[node] = True
    for i in range(len(lightList[node])):
        if(not visited[lightList[node][i]]):
            count += lightDfs(lightList[node][i], visited)
    
    return count
    
def heavyDfs(node, visited):
    count = 1
    visited[node] = True
    for i in range(len(heavyList[node])):
        if(not visited[heavyList[node][i]]):
            count += heavyDfs(heavyList[node][i], visited)
    
    return count

for i in range(1,N+1):
    visited = [False] * (N+1)
    lightcount = lightDfs(i, visited)

    if(lightcount > lefthalf):
        count += 1
        continue

    heavycount = heavyDfs(i, visited)

    if(heavycount > righthalf):
        count += 1

print(count)

    