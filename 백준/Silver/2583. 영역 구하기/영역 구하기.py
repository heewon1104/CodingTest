import sys
sys.setrecursionlimit(10**6)

N, M, K= map(int, sys.stdin.readline().split())
matrix = [([False] * M) for _ in range(N)]
result = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(K):
    startX, startY, endX, endY = map(int, sys.stdin.readline().split())
    for y in range(startY, endY):
        for x in range(startX, endX):
            matrix[y][x] = True

def Dfs(currentX, currentY):
    if(matrix[currentY][currentX] == True):
        return 1
    
    count = 1
    matrix[currentY][currentX] = True
    for i in range(4):
        nextX = currentX + dx[i]
        nextY = currentY + dy[i]
        if(0 <= nextX < M and 0 <= nextY < N and not matrix[nextY][nextX]):
            count += Dfs(nextX, nextY)
    return count

for i in range(N):
    for j in range(M):
        if(not matrix[i][j]):
            result.append(Dfs(j, i))

print(len(result))
result.sort()
print(' '.join(map(str, result)))