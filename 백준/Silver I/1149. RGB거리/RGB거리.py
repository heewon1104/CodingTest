import sys

n = int(input())

d = [[0] * 3 for i in range(n)]

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

d[0] = arr[0]

for i in range(1, n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + arr[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + arr[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + arr[i][2]

print(min(d[n-1]))