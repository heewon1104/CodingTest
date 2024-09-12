import sys

N, M = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
mergedCount = 0

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    edge[start].append(end)
    edge[end].append(start)

def findParent(node):
    while(parent[node] != node):
        node = parent[node]
    return parent[node]

def UnionSet(node1, node2):
    global mergedCount

    node1root = findParent(node1)
    node2root = findParent(node2)

    if(node1root != node2root):
        if(node1root < node2root):
            parent[node2root] = node1root
        else:
            parent[node1root] = node2root
        mergedCount += 1

for i in range(1, N+1):
    for j in range(len(edge[i])):
        UnionSet(i, edge[i][j])

print(N - mergedCount)