import sys
sys.setrecursionlimit(10**7)

N = int(input())

Graph = []
result = 0
maxHeight = 0
minHeight = sys.maxsize
Count = 0

# 우측, 아래, 좌측, 위
dx = [1, 0 ,-1, 0]
dy = [0, 1, 0 ,-1]

for _ in range(N):
    inputStr = list(map(int, input().split()))
    maxHeight = max(maxHeight, max(inputStr))
    minHeight = min(minHeight, min(inputStr))
    Graph.append(inputStr)

def Dfs(x, y, visited, height):
    if(Graph[y][x] > height):
        return
    if(visited[y][x] == True):
        return
    else:
        visited[y][x] = True
        for i in range(4):
            if(x + dx[i] < 0 or x + dx[i] >= N or y + dy[i] < 0 or y + dy[i] >= N):
                continue
            else:
                if(Graph[y + dy[i]][x + dx[i]] <= height):
                    visited[y + dy[i]][x + dx[i]] = True
                    Dfs(x + dx[i], y + dy[i], visited, height)

# 잠긴 지역은 True, 안잠긴 지역은 False
def checkArea(x, y, visited, firstFlag):
    global Count
    if(visited[y][x] == True):
        return
    else:
        visited[y][x] = True
        if(firstFlag == True):
            Count += 1
        for i in range(4):
            if(x + dx[i] < 0 or x + dx[i] >= N or y + dy[i] < 0 or y + dy[i] >= N):
                continue
            else:
                if(visited[y + dy[i]][x + dx[i]] == False):
                    checkArea(x + dx[i], y + dy[i], visited, False)

for height in range(minHeight-1, maxHeight+1):
    visited = list(list(False for _ in range(N)) for _ in range(N))
    Count = 0
    for i in range(N):
        for j in range(N):
            Dfs(j, i, visited, height)
    
    for i in range(N):
        for j in range(N):
            checkArea(j, i, visited, True)

    result = max(result, Count)

print(result)