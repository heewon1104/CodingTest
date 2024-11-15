import sys

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
height = r2 - r1 + 1
width = c2 - c1 + 1

arr = [[0] * width for _ in range(height)]

max_range = max(abs(r1), abs(r2), abs(c1), abs(c2))
total_numbers = (max_range * 2 + 1) ** 2

dx = [1, 0, -1, 0]  # 오른쪽, 위쪽, 왼쪽, 아래쪽
dy = [0, -1, 0, 1]
x, y = 0, 0
value = 1
direction = 0
length = 1
turns = 0
max_value = 1

while value <= total_numbers:
    for _ in range(length):
        if r1 <= y <= r2 and c1 <= x <= c2:
            arr[y - r1][x - c1] = value
            max_value = max(max_value, value)
        if value == total_numbers:
            value += 1
            break
        x += dx[direction]
        y += dy[direction]
        value += 1
    direction = (direction + 1) % 4
    turns += 1
    if turns % 2 == 0:
        length += 1

max_width = len(str(max_value))
for i in range(height):
    for j in range(width):
        print(f"{arr[i][j]:>{max_width}}", end=' ')
    print()
