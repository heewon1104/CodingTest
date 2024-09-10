import sys
import bisect

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

lis = []

for x in arr:
    pos = bisect.bisect_left(lis, x)
    if pos == len(lis):
        lis.append(x)
    else:
        lis[pos] = x

print(len(lis))
