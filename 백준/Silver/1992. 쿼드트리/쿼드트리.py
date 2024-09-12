import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip('\n'))
 
res = []

def checkArea(startX, endX, startY, endY):
    value = arr[startY][startX]
    for i in range(startY, endY + 1):
        for j in range(startX, endX + 1):
            if(value != arr[i][j]):
                return -1
    
    if(value == '1'):
        return 1
    else:
        return 0

def devide(startX, endX, startY, endY):
    check = checkArea(startX, endX, startY, endY)
    
    if(check == -1):
        midX = (startX+endX)//2
        midY = (startY+endY)//2
        
        res.append('(')
        devide(startX, midX, startY, midY)
        devide(midX+1, endX, startY, midY)
        devide(startX, midX, midY+1, endY)
        devide(midX+1, endX, midY+1, endY)
        res.append(')')

    elif(check == 0):
        res.append(0)
        return
    else:
        res.append(1)
        return

devide(0, N-1, 0, N-1)

for i in res:
    print(i, end='')
print()