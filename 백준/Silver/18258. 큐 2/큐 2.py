from collections import deque
import sys

N = int(input())
queue = deque()

for i in range(N):
    inputCommand = list(sys.stdin.readline().split())

    if(inputCommand[0] == "push"):
        queue.append(inputCommand[1])

    elif(inputCommand[0] == "pop"):
        if(not queue):
            print(-1)
        else:
            print(queue.popleft())

    elif(inputCommand[0] == "size"):
        print(len(queue))

    elif(inputCommand[0] == "empty"):
        if(not queue):
            print(1)
        else:
            print(0)

    elif(inputCommand[0] == "front"):
        if(not queue):
            print(-1)
        else:
            print(queue[0])

    else:
        if(not queue):
            print(-1)
        else:
            print(queue[-1])