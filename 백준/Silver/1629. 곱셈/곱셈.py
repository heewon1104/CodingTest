A, B, C = map(int, input().split())
total = 0
count = 0

def Calculate(A, B, C):
    if(B == 1):
        return A%C
    else:
        Fomula =  Calculate(A, B//2, C)
        if(B%2 == 0):
            return Fomula * Fomula % C
        else:
            return  (Fomula * Fomula * A)%C


print(Calculate(A, B, C))