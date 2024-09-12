import sys
import heapq
sys.setrecursionlimit(10**7)

V, E = map(int,  sys.stdin.readline().split())
edges = []
parent = list(i for i in range(0, V+1))

for i in range(E):
    start, end, value = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (value, start, end))

# 무도건 값이 적은 노드를 parent로 설정하여 연결된 가장 작은 노드까지 이동
def findParent(node):
    if(parent[node] != node):
        parent[node] = findParent(parent[node])
    return parent[node]

def union_parent(a, b):
    a = findParent(a)
    b = findParent(b)

    if a < b: # 작은 쪽이 부모가 된다. (한 집합 관계라서 부모가 따로 있는 건 아님)
        parent[b] = a
    else:
        parent[a] = b        

def same_parent(a, b):
    return findParent(a) == findParent(b)



answer = 0
for i in range(len(edges)):
    value, a, b = heapq.heappop(edges)
    if not same_parent(a, b):
        union_parent(a, b)
        answer += value

print(answer)
