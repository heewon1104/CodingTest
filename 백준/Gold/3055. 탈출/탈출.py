import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 큐에 물과 고슴도치의 위치를 함께 저장하여 BFS 처리
queue = deque()

# 방문 기록
visited = [[False for _ in range(M)] for _ in range(N)]

# 고슴도치와 목적지 위치
hedgehog = None
goal = None

# 초기 상태 저장
for y in range(N):
    for x in range(M):
        if board[y][x] == 'S':
            hedgehog = (x, y, 0)  # 고슴도치 위치 (X, Y, 시작 시간)
        elif board[y][x] == 'D':
            goal = (x, y)
        elif board[y][x] == '*':
            queue.append((x, y, -1))  # 물의 위치는 시간 정보가 필요 없음

# 고슴도치의 위치를 물보다 나중에 처리하기 위해 큐에 따로 추가
queue.append(hedgehog)

# BFS 시작
def bfs():
    while queue:
        currentX, currentY, time = queue.popleft()

        # 고슴도치가 목적지에 도착한 경우
        if (currentX, currentY) == goal:
            return time

        # 4방향 탐색
        for i in range(4):
            nextX = currentX + dx[i]
            nextY = currentY + dy[i]

            if 0 <= nextX < M and 0 <= nextY < N and not visited[nextY][nextX]:
                # 물이 퍼지는 경우
                if time == -1 and board[nextY][nextX] == '.':
                    board[nextY][nextX] = '*'
                    queue.append((nextX, nextY, -1))

                # 고슴도치가 이동하는 경우
                elif time >= 0 and (board[nextY][nextX] == '.' or board[nextY][nextX] == 'D'):
                    visited[nextY][nextX] = True
                    queue.append((nextX, nextY, time + 1))

    return "KAKTUS"

print(bfs())
