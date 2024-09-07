import sys

N = int(input())
inputArr = set(map(int, sys.stdin.readline().split()))

M = int(input())
resArr = list(map(int, sys.stdin.readline().split()))

for i in resArr:
    if(i in inputArr):
        print(1)
    else:
        print(0)