from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
costs = [{} for _ in range(N+1)]

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X,K))
    degree[X] += 1

queue = deque()
for i in range(1, N+1):
    if(degree[i] == 0):
        queue.append(i)
        costs[i][i] = 1

while(queue):
    popped = queue.popleft()
    for next, nextcost in graph[popped]:
        for key, value in costs[popped].items():
            if(not key in costs[next]):
                costs[next][key] = nextcost*value
            else:
                costs[next][key] += nextcost*value
        degree[next] -= 1
        if(degree[next] == 0):
            queue.append(next)

result = sorted(costs[N].items(), key = lambda x:x[0])
for key, value in result:
    print(key, value)