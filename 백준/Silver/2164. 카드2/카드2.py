from collections import deque

N = int(input())
arr = [i+1 for i in range(N)]
queue = deque(arr)

while(len(queue) > 1):
    num1 = queue.popleft()
    num2 = queue.popleft()

    queue.append(num2)

print(queue[0])