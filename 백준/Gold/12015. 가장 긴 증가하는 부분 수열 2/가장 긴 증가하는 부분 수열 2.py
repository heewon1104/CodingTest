import sys
import bisect

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

checkArr = []
for i in range(N):
    num = bisect.bisect_left(checkArr, arr[i])
    if(len(checkArr) == num):
        checkArr.append(arr[i])
    else:
        checkArr[num] = arr[i]

print(len(checkArr))