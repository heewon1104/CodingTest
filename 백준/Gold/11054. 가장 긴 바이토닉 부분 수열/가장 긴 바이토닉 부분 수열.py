import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

smallDP = [1] * N
largeDP = [1] * N

for i in range(N):
    for j in range(0, i):
        if(arr[i] > arr[j]):
            smallDP[i] = max(smallDP[i], smallDP[j]+1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if(arr[i] > arr[j]):
            largeDP[i] = max(largeDP[i], largeDP[j]+1)

res = 0
for i in range(N):
    res = max(res, smallDP[i] + largeDP[i]-1)
print(res)