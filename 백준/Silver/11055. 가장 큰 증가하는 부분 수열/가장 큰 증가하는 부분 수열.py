import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp = arr[:]

for i in range(N):
    for j in range(i):
        if(arr[i] > arr[j]):
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
