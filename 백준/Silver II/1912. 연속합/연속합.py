import sys

n = int(input())

arr = list(map(int,input().split()))

d = [0] * n
d[0] = arr[0]

if(n == 1):
    print(d[0])

else:
    for i in range(1,n):
        d[i] = max(d[i-1] + arr[i], arr[i])

    res = -1001
    for i in range(0,n):
        res = max(res,d[i])

    print(res)

