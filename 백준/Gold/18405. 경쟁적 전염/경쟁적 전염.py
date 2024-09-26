import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
board = []
heap = []

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if(board[i][j] != 0):
            heapq.heappush(heap, [board[i][j], j, i])
            
    
S, Y, X = map(int, sys.stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
time = 0

def Bfs():
    tmpList = []

    while(heap):
        virus, currentX, currentY = heapq.heappop(heap)
        
        for i in range(4):
            nextX, nextY = currentX+dx[i], currentY+dy[i]
            if(0 <= nextX < N and 0 <= nextY < N and virus and board[nextY][nextX] == 0):
                board[nextY][nextX] = virus
                tmpList.append([virus, nextX, nextY])
    
    return tmpList


for second in range(S):
    heap = Bfs()

print(board[Y-1][X-1])