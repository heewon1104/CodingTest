n = int(input())

d = [0] *(n+1)
res = list([] for _ in range(n+1))

if(n == 1):
    print(0)
    print(1)
else:
    for i in range(2, n+1):
        check = 0
        d[i] = d[i-1] + 1
       
        if(i%2 == 0):
            d[i] = min(d[i], d[i//2] + 1)
            if(d[i] == d[i//2] + 1):
                check = 1
        
        if(i%3 == 0):
            d[i] = min(d[i], d[i//3] + 1)
            if(d[i] == d[i//3] + 1):
                check = 2

        if(check == 0):
            res[i] = res[i-1].copy()
            res[i].append(i-1)

        elif(check == 1):
            res[i] = res[i//2].copy()
            res[i].append(i//2)

        else:
            res[i] = res[i//3].copy()
            res[i].append(i//3)

    res[n].append(n)

    print(d[n])

    while(res[n]):
        print(res[n].pop(), end=' ')
    print()

       