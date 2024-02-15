import sys

n = int(input())

for i in range(n):
    num = int(input())
    d = [0] * (num+1)

    if(num == 1):
            print(1)
    elif(num == 2):
            print(2)
    elif(num == 3):
         print(4)

    else:
        d[1] = 1
        d[2] = 2
        d[3] = 4
        for i in range(4,num+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
        
        print(d[num])
