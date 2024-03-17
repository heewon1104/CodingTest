N = int(input())

d = [0] * 1000001

d[1] = 1
d[2] = 2

if(N < 3):
    print(d[N])
else:
    for i in range(3,N+1):
        d[i] =(d[i-1]+d[i-2])%15746
    print(d[N]%15746)