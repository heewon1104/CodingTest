from collections import deque

N, M = map(int, input().split())
queue = deque()

for i in range(N):
    queue.append(i+1)

print("<", end="")

while(len(queue) > 1):
    for i in range(M-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=", ")


print(queue.popleft(), end=">")