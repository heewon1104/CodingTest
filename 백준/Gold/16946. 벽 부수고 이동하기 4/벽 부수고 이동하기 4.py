# 벽 부수고 이동하기 4
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip('\n')))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
areaIdx = 1

def Dfs(currentX, currentY, visited, location):
    total = 0
    for i in range(4):
        nextX = currentX + dx[i]
        nextY = currentY + dy[i]
        if(0<=nextX<M and 0<= nextY<N and board[nextY][nextX] == '0' and visited[nextY][nextX][0] == 0):
            visited[nextY][nextX][0] = 1
            total += Dfs(nextX, nextY, visited, location) + 1
            location.append([nextX, nextY])
        
    return total

for i in range(N):
    for j in range(M):
        if(board[i][j] == '0' and visited[i][j][0] == 0):
            location = [[j, i]]
            visited[i][j][0] = 1
            area = Dfs(j, i, visited, location) + 1
            for x, y in location:
                visited[y][x][0] = area
                visited[y][x][1] = areaIdx
            areaIdx += 1

for i in range(N):
    for j in range(M):
        if(board[i][j] == '1'):
            res = 0
            idxCheck = []
            for k in range(4):
                nextX = j + dx[k]
                nextY = i + dy[k]
                if(0<=nextX<M and 0<= nextY<N and visited[nextY][nextX][1] not in idxCheck):
                    idxCheck.append(visited[nextY][nextX][1])
                    res += visited[nextY][nextX][0]
            print((res+1) % 10, end='')
        else:
            print(0, end='')
    print()