def move(start, via, end, item):
    if(item == 1):
        print(start, end)
    else:
        move(start, end, via, item-1)
        print(start, end)
        move(via, start, end, item-1)

N = int(input())
if(N == 1):
    print(1)
else:
    print(2**N-1)
if(N <= 20):
    move(1, 2, 3, N)