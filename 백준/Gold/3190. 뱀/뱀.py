from collections import deque

N = int(input())
K = int(input())
apples = []
for _ in range(K):
    x, y = map(int, input().split())
    apples.append([x-1, y-1])
L = int(input())
command = []
for _ in range(L):
    num, tmp= input().rstrip('\n').split()
    command.append([int(num), tmp])

currentX = 0
currentY = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
queue.append([currentX, currentY])
direction = 0
directionIdx = 0
time = 0

while(1):
    if([queue[-1][1]+dy[direction], queue[-1][0]+dx[direction]] in apples):
        apples.remove([queue[-1][1]+dy[direction], queue[-1][0]+dx[direction]])
        x, y = queue[-1]
    else:
        x,y = queue.popleft()
    
    if(queue):
        newx, newy = queue[-1][0]+dx[direction], queue[-1][1]+dy[direction]
    else:
        newx, newy = x+dx[direction], y+dy[direction]
    time += 1

    if(newx < 0 or newx >=N or newy<0 or newy>=N):
        print(time)
        break

    elif([newx,newy] in queue or (newx == x and newy == y)):
        print(time)
        break

    queue.append([newx, newy])

    if(directionIdx < len(command)):
        if(command[directionIdx][0] == time):
            if(command[directionIdx][1] == 'D'):
                direction = (direction+1)%4
            else:
                direction = (direction-1+4)%4
            directionIdx+=1
