N = int(input())

i = 1
while(N > 1):
    i += 1
    if(N % i == 0):
        print(i)
        N //= i
        i=1