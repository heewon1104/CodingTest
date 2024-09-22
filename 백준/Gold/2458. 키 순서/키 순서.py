import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
board = [list(False for _ in range(N+1)) for _ in range(N+1)]
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    board[start][end] = True

def floyd():
    for i in range(1, N+1):
        for start in range(1, N+1):
            if(start == i):
                continue
            for end in range(1, N+1):
                if(start == end or end == i):
                    continue
                if(board[start][i] and board[i][end]):
                    board[start][end] = True

    res = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if(board[i][j]):
                res[i] += 1
                res[j] += 1 
    count = 0
    for i in range(1, N+1):
        if(res[i] == N-1):
            count += 1
    print(count)

floyd()
                
        