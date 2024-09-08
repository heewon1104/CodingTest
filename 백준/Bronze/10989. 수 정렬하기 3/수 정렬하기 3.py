import sys

N = int(input())
arr = [0 for _ in range(10001)]
maxValue = 0

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num-1] += 1
    maxValue = max(maxValue, num)

for i in range(maxValue):
    for j in range(arr[i]):
        print(i+1)