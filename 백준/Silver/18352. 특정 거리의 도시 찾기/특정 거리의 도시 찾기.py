import sys
from collections import deque 

N, M, K, X = map(int, sys.stdin.readline().split())
road = [[] for _ in range(N+1)]

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    road[start].append(end)

def Bfs():
    visited = [-1 for _ in range(N+1)]
    visited[X] = 0
    queue = deque()
    queue.append([X, 0])
    
    while(queue):
        current, distance = queue.popleft()

        for i in range(len(road[current])):
            if(visited[road[current][i]] == -1):
                queue.append([road[current][i], distance+1])
                visited[road[current][i]] = distance+1

    count = 0
    for i in range(1, N+1):
        if(visited[i] == K):
            count += 1
            print(i)
    
    if(count == 0):
        print(-1)
Bfs()