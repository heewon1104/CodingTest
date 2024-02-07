from collections import deque

N = int(input())
board = []
warm = deque()

for _ in range(N):
    board.append(list([0] * N))

y = 0
x = 0

# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 0

apple = int(input())
for _ in range(apple):
    ay, ax = map(int, input().split())
    board[ay-1][ax-1] = 1

command = int(input())
cmd_arr = []
cmd_idx = 0

for _ in range(command):
    input_cmd = input().split()
    cmd_arr.append(input_cmd)


time = 0
warm.append([0,0])

while(1):
    # 방향전환시
    if(time == int(cmd_arr[cmd_idx][0])):
        #오른쪽, 시계
        if(cmd_arr[cmd_idx][1] == 'D'):
            dir = (dir +1)%4

        #왼쪽,반시계
        elif(cmd_arr[cmd_idx][1] == 'L'):
            dir = (dir+3)%4
        
        if(y + dy[dir] < 0 or y + dy[dir] >= N or x + dx[dir] < 0 or x + dx[dir] >= N):
            print(time+1)
            break

        if(warm.count([x+dx[dir], y + dy[dir]]) != 0):
            print(time+1)
            break

        x = x + dx[dir]
        y = y + dy[dir]

        if(cmd_idx < command-1):
            cmd_idx += 1

        if(board[y][x] == 0):
            warm.popleft()
        else:
            board[y][x] = 0
        
        warm.append([x,y])
            
    #안할시 
    else:
        if(y + dy[dir] < 0 or y + dy[dir] >= N or x + dx[dir] < 0 or x + dx[dir] >= N):
            print(time+1)
            break

        if(warm.count([x+dx[dir], y + dy[dir]]) != 0):
            print(time+1)
            break

        x = x + dx[dir]
        y = y + dy[dir]

        if(board[y][x] == 0):
            warm.popleft()
        else:
            board[y][x] = 0
        
        warm.append([x,y])

    time += 1