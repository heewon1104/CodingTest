N = int(input())
M = int(input())
arr = list(map(int, input().split()))

res = 0
for i in range(M):
    if(i == 0):
        res = max(res, arr[i])
    if(i == M-1):
        res = max(res, N-arr[i])
    if(i != 0 and i!= M-1):
        res = max(res, int((arr[i] - arr[i-1])/2 + 0.5))

print(res)