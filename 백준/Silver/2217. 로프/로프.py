n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
res = []
for i in range(n):
    res.append(arr[i] * (i+1))

print(max(res))