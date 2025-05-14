N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

res = []

def Check(startX, endX, startY, endY):
    checkFlag = arr[startY][startX]
    for y in range(startY, endY):
        for x in range(startX, endX):
            if(checkFlag != arr[y][x]):
                return -1
    return checkFlag

def Devide(startX, endX, startY, endY):
    checkFlag = Check(startX, endX, startY, endY)
    if(checkFlag == -1):
        res.append('(')
        Devide(startX, (startX+endX)//2, startY, (startY+endY)//2)
        Devide((startX+endX)//2, +endX, startY, (startY+endY)//2)
        Devide(startX, (startX+endX)//2, (startY+endY)//2, endY)
        Devide((startX+endX)//2, endX, (startY+endY)//2, endY)
        res.append(')')
    elif(checkFlag == 0):
        res.append('0')
    else:
        res.append('1')


startX, endX, startY, endY = 0, N, 0, N
Devide(startX, endX, startY, endY)

for i in res:
    print(i, end='')