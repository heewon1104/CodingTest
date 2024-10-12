# 치킨 배달 
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
houses = []
chicken = []
res = sys.maxsize

for i in range(N):
    inputStr = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if(inputStr[j] == 1):
            houses.append([j, i])
        if(inputStr[j] == 2):
            chicken.append([j, i])

tmp = list(combinations(chicken, M))

for i in range(len(tmp)):
    total = 0
    for j in range(len(houses)):
        tmpsum = sys.maxsize
        for k in range(M):
            tmpsum = min(tmpsum, abs(houses[j][0]-tmp[i][k][0]) + abs(houses[j][1]-tmp[i][k][1]))
        total += tmpsum
    res = min(res, total)

print(res)