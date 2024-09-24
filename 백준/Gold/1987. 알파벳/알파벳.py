import sys

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 결과값 저장 변수
res = 0

def dfs(x, y, visited, count):
    global res
    res = max(res, count)

    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]

        if (0 <= nextX < M and 0 <= nextY < N):
            next_char = board[nextY][nextX]

            if(visited[ord(next_char) - 65] == 0):
                visited[ord(next_char) - 65] = 1
                dfs(nextX, nextY, visited, count + 1)
                visited[ord(next_char) - 65] = 0


visited = [0] * 26
visited[ord(board[0][0]) - 65] = 1
dfs(0, 0, visited, 1)

print(res)
