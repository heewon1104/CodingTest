import sys
N = int(sys.stdin.readline())
students = [[] for _ in range(N*N+1)]
order = []
seats = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 학생 정보 입력
for _ in range(N*N):
    student, friend1, friend2, friend3, friend4 = map(int, sys.stdin.readline().split())
    students[student].extend([friend1, friend2, friend3, friend4])
    order.append(student)

# 좌석 체크 함수
def CheckSeat(studentIdx):
    maxFriends = -1
    maxSpaces = -1
    bestX, bestY = -1, -1

    for i in range(N):
        for j in range(N):
            if seats[i][j] != 0:  # 이미 배치된 좌석은 건너뜀
                continue

            tmpFriends = 0
            tmpSpaces = 0

            for k in range(4):
                nextY = i + dy[k]
                nextX = j + dx[k]

                if 0 <= nextX < N and 0 <= nextY < N:
                    if seats[nextY][nextX] in students[studentIdx]:
                        tmpFriends += 1
                    elif seats[nextY][nextX] == 0:
                        tmpSpaces += 1

            # 최적의 좌석 갱신 조건
            if tmpFriends > maxFriends or (tmpFriends == maxFriends and tmpSpaces > maxSpaces) or (tmpFriends == maxFriends and tmpSpaces == maxSpaces and (bestY > i or (bestY == i and bestX > j))):
                maxFriends = tmpFriends
                maxSpaces = tmpSpaces
                bestX, bestY = j, i

    return bestX, bestY

# 학생 배치
for student in order:
    x, y = CheckSeat(student)
    seats[y][x] = student

# 행복도 계산
res = 0
resHappy = [0, 1, 10, 100, 1000]

for i in range(N):
    for j in range(N):
        tmpFriends = 0
        for k in range(4):
            nextY = i + dy[k]
            nextX = j + dx[k]
            if 0 <= nextX < N and 0 <= nextY < N:
                if seats[nextY][nextX] in students[seats[i][j]]:
                    tmpFriends += 1
        res += resHappy[tmpFriends]

print(res)
