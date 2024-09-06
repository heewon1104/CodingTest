N = int(input())
def move(start, to):
    print(start, to)

def hanoi(n, start, tmp, end):
    if(n == 1):
        move(start, end)
        return 
    else:
        hanoi(n-1, start, end, tmp)
        move(start, end)
        hanoi(n-1, tmp, start, end)

if(N == 1):
    print(1)
else:
    print(2**N-1)

if(N <= 20):
    hanoi(N, 1, 2, 3)