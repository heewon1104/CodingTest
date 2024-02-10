n = int(input())
arr = []
res = list([1] * n)

for i in range(n):
    tmp = list(map(int, input().split(' ')))
    arr.append(tmp)

for i in range(n):
    for j in range(n):
        if(arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]):
            res[i] += 1

for i in range(n):
    print(res[i], end=' ')