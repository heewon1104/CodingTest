import sys
from collections import deque 

N = int(sys.stdin.readline())
board = [sys.stdin.readline().rstrip('\n') for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited = [list([sys.maxsize] * N) for _ in range(N)]

    while(queue):
        currentX, currentY, cost = queue.popleft()
        for i in range(4):
            nextX, nextY = currentX + dx[i], currentY + dy[i]
            if(nextX >= 0 and nextX < N and nextY >=0 and nextY < N):
                nextCost = cost
                if(board[nextY][nextX] == '0'):
                    nextCost += 1
                
                if(nextCost < visited[nextY][nextX]):
                     visited[nextY][nextX] = nextCost
                     queue.append([nextX, nextY, nextCost])
    
    print(visited[N-1][N-1])

bfs()