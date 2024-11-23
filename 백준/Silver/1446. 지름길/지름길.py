import sys

N, D = map(int, sys.stdin.readline().split())
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dist = [sys.maxsize] * (D + 1)
dist[0] = 0

positions = [[] for _ in range(D + 1)]
for s, e, l in roads:
    if e <= D and l < e - s:
        positions[s].append((e, l))

for i in range(D):
    if dist[i + 1] > dist[i] + 1:
        dist[i + 1] = dist[i] + 1
    for e, l in positions[i]:
        if dist[e] > dist[i] + l:
            dist[e] = dist[i] + l

print(dist[D])
