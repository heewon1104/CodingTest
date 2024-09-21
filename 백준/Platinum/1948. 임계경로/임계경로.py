import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
cost = [[0, set()] for _ in range(N+1)] 
countRoad = 0

for _ in range(M):
    start, end, value = map(int, sys.stdin.readline().split())
    edges[start].append([end, value])
    degree[end] += 1

startNode, endNode = map(int, sys.stdin.readline().split())


def TopologicalSort():
    global countRoad

    queue = deque()
    queue.append(startNode)

    while(queue):
        poppedNode = queue.popleft()
        
        for i in range(len(edges[poppedNode])):
            nextNode = edges[poppedNode][i]
            degree[nextNode[0]] -= 1

            if(degree[nextNode[0]] == 0):
                queue.append(nextNode[0])

            if(nextNode[1] + cost[poppedNode][0] > cost[nextNode[0]][0]):
                cost[nextNode[0]][0] = nextNode[1] + cost[poppedNode][0]
                cost[nextNode[0]][1] = set(cost[poppedNode][1]) 
                cost[nextNode[0]][1].add((poppedNode, nextNode[0]))

            elif(nextNode[1] + cost[poppedNode][0] < cost[nextNode[0]][0]):
                cost[nextNode[0]][0] = cost[nextNode[0]][0]
                

            else:
                cost[nextNode[0]][1].update(cost[poppedNode][1]) 
                cost[nextNode[0]][1].add((poppedNode, nextNode[0]))

        if(poppedNode != endNode):
            cost[poppedNode][1] = None

    print(cost[endNode][0])
    print(len(cost[endNode][1]))

TopologicalSort()
