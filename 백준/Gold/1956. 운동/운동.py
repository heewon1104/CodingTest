import sys

V, E = map(int, sys.stdin.readline().split())
matrix = [list(sys.maxsize for _ in range(V+1)) for _ in range(V+1)]

for i in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    matrix[start][end] = cost
 
def Floyd():
    for via in range(1, V+1):
         for start in range(1, V+1):
              if(via == start):
                   continue
              for end in range(1, V+1):
                   if(via == end):
                        continue
                   matrix[start][end] = min(matrix[start][end], matrix[start][via] + matrix[via][end])

    res = sys.maxsize

    for i in range(1, V+1):
        for j in range(1, V+1):
             res = min(res, matrix[i][j] + matrix[j][i])

    if(res == sys.maxsize):
         print(-1)
    else:
         print(res)

Floyd()