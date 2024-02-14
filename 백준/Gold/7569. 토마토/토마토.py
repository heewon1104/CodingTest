from collections import deque

#m: 가로 n: 세로 h: 높이
m,n,h = map(int, input().split())

res = []
for _ in range(h):
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    res.append(arr)

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if(res[i][j][k] == 1):
                queue.append([i,j,k,0])

lastday = -1

while(queue):
    poparr = queue.popleft()
    z = poparr[0]
    y = poparr[1]
    x = poparr[2]
    day = poparr[3]
    lastday = day

    if(z-1 >= 0):
        if(res[z-1][y][x] == 0):
            queue.append([z-1,y,x,day+1])
            res[z-1][y][x]=1
    
    if(z+1 < h):
        if(res[z+1][y][x] == 0):
            queue.append([z+1,y,x,day+1])
            res[z+1][y][x]=1
    
    if(y-1 >= 0):
        if(res[z][y-1][x] == 0):
            queue.append([z,y-1,x,day+1])
            res[z][y-1][x]=1
    
    if(y+1 < n):
        if(res[z][y+1][x] == 0):
            queue.append([z,y+1,x,day+1])
            res[z][y+1][x]=1
    
    if(x-1 >= 0):
        if(res[z][y][x-1] == 0):
            queue.append([z,y,x-1,day+1])
            res[z][y][x-1]=1
    
    if(x+1 < m):
        if(res[z][y][x+1] == 0):
            queue.append([z,y,x+1,day+1])
            res[z][y][x+1]=1

check = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if(res[i][j][k] == 0):
               check = True
               break
        if(check == True):
            break
    if(check == True):
            break

if(check == True):
    print(-1)
else:
    print(lastday)