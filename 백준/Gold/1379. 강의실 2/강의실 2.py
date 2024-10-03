import sys
import heapq

N = int(sys.stdin.readline())
lecture = []

for i in range(N):
    num, start, end = map(int, sys.stdin.readline().split())
    lecture.append((start, end, num))

lecture.sort(key=lambda x: x[0])  # 시작 시간을 기준으로 정렬

# 힙을 이용하여 강의실을 관리
classrooms = []
result = [0] * (N + 1)  # 각 강의가 배정된 강의실 번호를 저장할 리스트
room_count = 0  # 배정된 강의실 수

for start, end, num in lecture:
    if classrooms and classrooms[0][0] <= start:
        # 기존 강의실을 사용할 수 있는 경우
        available_end_time, room_num = heapq.heappop(classrooms)
        result[num] = room_num
        heapq.heappush(classrooms, (end, room_num))  # 종료 시간을 업데이트
    else:
        # 새로운 강의실을 사용하는 경우
        room_count += 1
        result[num] = room_count
        heapq.heappush(classrooms, (end, room_count))

print(room_count)  # 필요한 강의실 수 출력

# 각 강의가 배정된 강의실 번호 출력
for i in range(1, N + 1):
    print(result[i])
