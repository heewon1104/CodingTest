import sys

n, m = map(int, input().split())

set1 = set()
set2 = set()

for i in range(n):
    set1.add(sys.stdin.readline().rstrip('\n'))

for i in range(m):
    set2.add(sys.stdin.readline().rstrip('\n'))

resarr = sorted(list(set1 & set2))

print(len(resarr))
for i in range(len(resarr)):
    print(resarr[i])
