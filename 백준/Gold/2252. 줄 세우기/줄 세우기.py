import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
student = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
for i in range(M):
    short, long = map(int, sys.stdin.readline().split())
    student[short].append(long)
    degree[long] += 1

def topology_sort():
    result = []
    queue = deque()
    for i in range(1, N+1):
        if(degree[i] == 0):
            queue.append(i)
    
    while(queue):
        popped = queue.popleft()
        result.append(popped)

        for i in range(len(student[popped])):
            degree[student[popped][i]] -= 1
            if(degree[student[popped][i]] == 0):
                queue.append(student[popped][i])

    for i in result:
        print(i, end=' ')
    print()

topology_sort()