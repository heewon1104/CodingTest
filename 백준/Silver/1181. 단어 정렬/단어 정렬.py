import sys

n = int(input())

arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().rstrip('\n'))

removedArr = set(arr)
arr = list(removedArr)

arr.sort()
arr.sort(key = lambda x : len(x))

for i in arr:
    print(i)