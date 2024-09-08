from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
res = permutations(arr, N)
maxnum = 0

resarr = list(res)

for i in range(len(resarr)):
    total = 0
    for j in range(0, N-1):
        total += abs(resarr[i][j] - resarr[i][j+1])
    maxnum = max(maxnum, total)

print(maxnum)