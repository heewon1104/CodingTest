import sys

M, N, L = map(int, input().split())
hunterPosition = list(map(int, sys.stdin.readline().split()))
hunterPosition.sort()
animalPodition = []
count = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    animalPodition.append([x, y])


for i in range(N):
    if(animalPodition[i][1] > L):
        continue

    start = animalPodition[i][1] + animalPodition[i][0] - L
    end = L - animalPodition[i][1] + animalPodition[i][0]

    left, right = 0, M-1

    while(left <= right):
        mid = (left+right)//2
        if(hunterPosition[mid] >= start and hunterPosition[mid] <= end):
            count += 1
            break
        elif(hunterPosition[mid] < end):
            left = mid + 1
        else:
            right = mid -1

print(count)

    


