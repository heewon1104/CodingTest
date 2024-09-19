import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이를 줄임

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# DFS 대신 스택을 이용한 반복 구조로 변경
def checkDivide(X, Y, visited):
    stack = [(X, Y)]
    visited[Y][X] = True
    while stack:
        curX, curY = stack.pop()
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < M and 0 <= nextY < N and not visited[nextY][nextX] and board[nextY][nextX] > 0:
                visited[nextY][nextX] = True
                stack.append((nextX, nextY))

def melted():
    # 빙산을 녹이는 함수
    new_board = [row[:] for row in board]  # 녹은 상태를 바로 반영하기 위해 복사본 사용
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                count = 0
                for k in range(4):
                    nextX = j + dx[k]
                    nextY = i + dy[k]
                    if 0 <= nextX < M and 0 <= nextY < N and board[nextY][nextX] == 0:
                        count += 1
                new_board[i][j] = max(board[i][j] - count, 0)
    return new_board

Year = 0

while True:
    visited = [[False] * M for _ in range(N)]
    count = 0
    isAllMelted = True

    # 빙산 구역 나누기 (DFS 반복 구조 사용)
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                checkDivide(j, i, visited)
                count += 1
                isAllMelted = False

    # 두 개 이상의 빙산이 존재하거나 빙산이 다 녹았을 경우 종료
    if count >= 2:
        print(Year)
        break
    if isAllMelted:
        print(0)
        break

    # 빙산을 녹이고 board 업데이트
    board = melted()
    Year += 1
