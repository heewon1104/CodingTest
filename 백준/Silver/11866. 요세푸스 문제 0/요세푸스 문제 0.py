from collections import deque

N, K = map(int, input().split())

queue = deque()
for i in range(N):
    queue.append(i+1)

count = 0
print('<' , end='')
while(len(queue) > 1):
    popped = queue.popleft()
    count += 1

    if(count != K):
        queue.append(popped)
    else:
        print(popped, end=', ')
        count = 0
    
print(queue.popleft(), end='>\n')
