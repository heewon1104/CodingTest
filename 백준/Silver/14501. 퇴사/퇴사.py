n = int(input())
arr = []
d = list([0] * (n+1))

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n-1, -1, -1):
    if(arr[i][0] + i > n):
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], d[i+arr[i][0]] + arr[i][1])
print(d[0])