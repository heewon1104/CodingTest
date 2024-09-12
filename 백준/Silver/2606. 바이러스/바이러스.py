import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

edge = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
ConnectCount = 0

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    edge[start].append(end)
    edge[end].append(start)

def findParent(node):
    while(parent[node] != node):
        node = parent[node]
    return parent[node]

def UnionSet(node1, node2):
    node1root = findParent(node1)
    node2root = findParent(node2)

    if(node1root != node2root):
        if(node1root < node2root):
            parent[node2root] = node1root
        else:
            parent[node1root] = node2root

for i in range(1, N+1):
    for j in range(len(edge[i])):
        UnionSet(i, edge[i][j])

for i in range(1, N+1):
    if(findParent(i) == 1):
        ConnectCount += 1

print(ConnectCount-1)