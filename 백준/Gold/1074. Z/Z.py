N, R, C = map(int, input().split())

count = 0

def Devide(startX, startY, endX, endY):
    global count
    
    if(endX-startX == 2):
        if(startY == R and startX == C):
            print(count)
            return
        elif(startY == R and endX-1 == C):
            print(count+1)
            return
        elif(endY-1 == R and startX == C):
            print(count+2)
            return
        else:
            print(count+3)
            return
    
    else:
        midX = (startX + endX) // 2
        midY = (startY + endY) // 2
        if(C < midX and R < midY):
            Devide(startX, startY, (startX+endX)//2, (startY+endY)//2)
        elif(C >= midX and R < midY):
            count += (midX-startX)*(midX-startX)
            Devide((startX+endX)//2, startY, endX, (startY+endY)//2)
        elif(C < midX and R >= midY):
            count += (midX-startX)*(midX-startX)*2
            Devide(startX, (startY+endY)//2, (startX+endX)//2, endY)
        else:
            count += (midX-startX)*(midX-startX)*3
            Devide((startX+endX)//2, (startY+endY)//2, endX, endY)

Devide(0, 0, 2**N, 2**N)