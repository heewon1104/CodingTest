import sys

N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

startValue = 0
endValue = max(arr)
result = sys.maxsize
Height = 0
midValue = 0

while(1):
    if(result == M or abs(startValue-endValue) == 1):
        break
    Woods = 0
    midValue = int((endValue + startValue) / 2)

    for i in arr:
        if(i - midValue > 0):
            Woods += i - midValue

    if(Woods >= M and result > Woods): 
        result = Woods
        Height = midValue
        startValue = midValue
        continue

    elif(Woods < M):
        endValue = midValue

print(Height)


