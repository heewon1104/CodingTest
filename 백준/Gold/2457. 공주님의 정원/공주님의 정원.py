import sys
import heapq

def changeDay(Month, Day):
    total = 0
    for i in range(1, Month):
        if(i == 4 or i == 6 or i == 9 or i == 11):
            total += 30
        elif(i == 2):
            total += 28
        else:
            total += 31
    return total + Day

N = int(sys.stdin.readline())
flowers = []

# 입력 받기 및 시작일과 종료일을 날짜로 변환하여 flowers 리스트에 추가
for _ in range(N):
    startMonth, startDay, endMonth, endDay = map(int, sys.stdin.readline().split())
    start = changeDay(startMonth, startDay)
    end = changeDay(endMonth, endDay)
    flowers.append((start, end))

# 시작 날짜 기준 정렬 (시작일이 같을 경우 종료일이 빠른 순서로 정렬)
flowers.sort()

# 필요한 변수 초기화
currentEnd = changeDay(3, 1)
EndTerm = changeDay(11, 30)
res = 0
heap = []
idx = 0

# 정원이 피어 있는 기간을 유지하며 탐색
while currentEnd <= EndTerm:
    # 현재 범위 내에 피는 꽃을 힙에 추가
    while idx < N and flowers[idx][0] <= currentEnd:
        heapq.heappush(heap, -flowers[idx][1])  # 종료일을 최대화하기 위해 음수로 저장
        idx += 1
    # 범위를 확장할 수 있는 꽃이 없다면 종료
    if not heap:
        res = 0
        break
    # 가장 늦게 지는 꽃을 선택하여 현재 범위 확장
    currentEnd = -heapq.heappop(heap)
    res += 1

# 최종적으로 EndTerm을 덮었는지 확인
if currentEnd < EndTerm:
    res = 0
print(res)
