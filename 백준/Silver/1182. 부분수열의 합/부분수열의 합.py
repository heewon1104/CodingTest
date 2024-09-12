from itertools import combinations

N, S = map(int, input().split())

arr = list(map(int, input().split()))

res = []
count = 0

for i in range(1, N+1):
    cal = list(combinations(arr, i))
    res.append(cal)

for i in res:
    for j in range(len(i)):
        if(sum(i[j]) == S):
            count += 1

print(count)
