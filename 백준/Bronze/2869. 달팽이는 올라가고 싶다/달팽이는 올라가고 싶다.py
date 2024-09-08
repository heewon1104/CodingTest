import math

A, B, V= map(int, input().split())
height = 0
Day = 0

V -= A
print(int(math.ceil(V/(A-B)))+1)