# ACM Craft
import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    cost = list(map(int, sys.stdin.readline().split()))
    degree = [0] * (N+1)
    arcs = [[] for _ in range (N+1)]
    for i in range(K):
        start, end = map(int, sys.stdin.readline().split())
        arcs[start].append(end)
        degree[end] += 1
    W = int(sys.stdin.readline())
    
    queue = deque()
    result = [0] * (N+1)
    for i in range(1, N+1):
        if(degree[i] == 0):
            queue.append(i)
            result[i] = cost[i-1]
    
    while(queue):
        currentNode = queue.popleft()
        for i in range(len(arcs[currentNode])):
            next = arcs[currentNode][i]
            degree[next] -= 1 
            result[next] = max(result[next], result[currentNode] + cost[next-1])

            if(degree[next] == 0):
                queue.append(next)
    print(result[W])