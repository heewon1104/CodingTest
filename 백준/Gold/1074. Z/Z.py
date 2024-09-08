N, r, c = map(int, input().split())

Result = 0

def Recrusive(x, y, Width):
    global Result
    half = Width // 2
    
    if(Width == 2):
        if(x == 0 and y == 0):
            Result += 1
        elif(x==1 and y == 0):
            Result += 2
        elif(x == 0 and y==1):
            Result += 3
        else:
            Result += 4
        return

    # 1사분면
    if(x < half  and y < half):
        Recrusive(x, y, Width//2)
    # 2사분면
    elif(half <= x and y < half):
        Result += half*half
        Recrusive(x-half, y, Width//2)
    # 3사분면
    elif(x < half  and half <= y):
        Result += half*half*2
        Recrusive(x, y-half, Width//2)
    # 4사분면
    elif(half <= x and y >= half):
        Result += half*half*3
        Recrusive(x-half, y-half, Width//2)

Recrusive(c, r, pow(2,N))
print(Result-1)
