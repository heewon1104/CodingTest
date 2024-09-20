import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parts = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
costs = [{} for _ in range(N+1)]

for i in range(M):
    make, part, num = map(int, sys.stdin.readline().split())
    parts[part].append([make, num])
    degree[make] += 1

def topology_sort():
    queue = deque()
    for i in range(1, N+1):
        if(degree[i] == 0):
            queue.append(i)
            costs[i][i] = 1
    
    while(queue):
        popped = queue.popleft()

        for next, nextcost in parts[popped]:
            for key, value in costs[popped].items():
                if(key in costs[next]):
                    costs[next][key] += value * nextcost
                else:
                    costs[next][key] = value * nextcost

            degree[next] -= 1
            if(degree[next] == 0):
                queue.append(next)
    
    sorted_dict = sorted(costs[N].items(), key = lambda item: item[0])

    for key, value in sorted_dict:
        print(key, value)
topology_sort()