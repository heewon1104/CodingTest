import sys
from collections import deque

input = sys.stdin.readline
INF = 10**9

M, N, H = map(int, input().split())
boxes = [[[0] * M for _ in range(N)] for _ in range(H)]
queue = deque()

zero_count = 0

dx = [1, -1, 0,  0, 0,  0]
dy = [0,  0, 1, -1, 0,  0]
dz = [0,  0, 0,  0, 1, -1]

for z in range(H):
    for y in range(N):
        row = list(map(int, input().split()))
        for x in range(M):
            val = row[x]
            boxes[z][y][x] = val
            if val == 0:
                zero_count += 1
            elif val == 1:
                queue.append((x, y, z, 0))

if zero_count == 0:
    print(0)
    sys.exit(0)

result = 0

while queue:
    x, y, z, t = queue.popleft()
    result = max(result, t)

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = 1
                zero_count -= 1
                queue.append((nx, ny, nz, t + 1))

if zero_count > 0:
    print(-1)
else:
    print(result)
