N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

for num in arr:
    print(num, end="\n")