from collections import deque
import sys

def dfs(start):
  visited[start] = True
  print(start, end = ' ')

  for i in arr[start]:
    if not visited[i]:
      dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in arr[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n, m, v = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n+1)]

for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  arr[x].append(y)
  arr[y].append(x)

for i in arr:
  i.sort()

visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)


