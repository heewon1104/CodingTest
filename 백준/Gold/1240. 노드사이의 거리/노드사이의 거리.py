import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    node1, node2, cost = map(int, input().split())
    edges[node1].append((node2, cost))
    edges[node2].append((node1, cost))

def dfs(current, end, count, visited):
    if current == end:
        return count
    for next_node, cost in edges[current]:
        if next_node not in visited:
            visited.add(next_node)  # Set으로 변경하여 효율성을 높임
            result = dfs(next_node, end, count + cost, visited)
            if result != -1:  # 경로를 찾은 경우에만 반환
                return result
    return -1  # 경로를 못 찾으면 -1 반환 (실제로는 실행되지 않음)

for _ in range(M):
    start, end = map(int, input().split())
    visited = set([start])
    print(dfs(start, end, 0, visited))
