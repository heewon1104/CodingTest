import sys

N = int(sys.stdin.readline())
arr = [[] for _ in range(4)]

# 입력 배열 생성
for _ in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    for i in range(4):
        arr[i].append(num[i])

# 두 배열의 합을 각각 mergedArr[0]과 mergedArr[1]에 저장
sumAB = []
sumCD = []

for i in range(N):
    for j in range(N):
        sumAB.append(arr[0][i] + arr[1][j])
        sumCD.append(arr[2][i] + arr[3][j])

# sumAB를 오름차순, sumCD를 내림차순으로 정렬
sumAB.sort()
sumCD.sort(reverse=True)

# 투 포인터로 합이 0이 되는 경우의 수 찾기
count = 0
left, right = 0, 0

while left < len(sumAB) and right < len(sumCD):
    current_sum = sumAB[left] + sumCD[right]
    if current_sum == 0:
        # sumAB[left]와 sumCD[right]에 동일한 값이 여러 개 있을 수 있으므로,
        # 각각의 빈도를 계산하여 그 곱만큼 count에 더함
        left_count, right_count = 1, 1
        
        # sumAB에서 같은 값의 빈도 계산
        while left + 1 < len(sumAB) and sumAB[left] == sumAB[left + 1]:
            left += 1
            left_count += 1
        
        # sumCD에서 같은 값의 빈도 계산
        while right + 1 < len(sumCD) and sumCD[right] == sumCD[right + 1]:
            right += 1
            right_count += 1
        
        count += left_count * right_count
        left += 1
        right += 1
    elif current_sum < 0:
        left += 1
    else:
        right += 1

print(count)
