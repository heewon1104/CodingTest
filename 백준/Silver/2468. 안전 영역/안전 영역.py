from collections import deque
import sys

# 임력 및 변수 설정
N = int(input())
minNum, maxNum = sys.maxsize, 0
board = []
result = 0
for _ in range(N):
    inputArr = list(map(int, input().split()))
    board.append(inputArr)
    minNum = min(minNum, min(inputArr))
    maxNum = max(maxNum, max(inputArr))

dx = [0, 1, 0 , -1]
dy = [-1, 0, 1, 0]

# BFS로 영역을 검사하는 함수
def CheckArea(currentX, currentY, visit):
    # 큐 선언 및 현재 좌표 삽입
    queue = deque()
    queue.append((currentX, currentY))

    # 큐가 빌때까지
    while(queue):
        # 큐에서 꺼내와 상하좌우 검사
        poppedX, poppedY = queue.popleft()
        for i in range(4):
            nextX = poppedX + dx[i]
            nextY = poppedY + dy[i]

            # 다음 좌표가 보드 내의 영역이고, 방문을 하지 않았고, 높이가 물의 높이보다 더 높다면
            if(nextX >= 0 and nextX < N and nextY >= 0 and nextY < N and not visit[nextY][nextX] and board[nextY][nextX] > height):
                # 큐에 추가 및 방문처리
                queue.append((nextX, nextY))
                visit[nextY][nextX] = True

# 가장 낮은 높이부터 최대 높이까지 모든 높이에 대해 검사
for height in range(minNum-1, maxNum+1):
    # 방문 배열 및 영역 개수에 대한 변수 선언
    visit = []
    count = 0
    for _ in range(N):
        visit.append([False]*N)

    # 보드 전체에 대하여
    for y in range(N):
        for x in range(N):
            # 만약 방문하지 않았고 물의 높이보다 현재의 높이가 높다면 BFS 검사 수행 및 영역 개수 +1
            if(not visit[y][x] and board[y][x] > height):
                CheckArea(x, y, visit)
                count += 1
    # 최종 결과는 현재 영역 개수중 가장 많은 것을 저장
    result = max(result, count)

print(result)