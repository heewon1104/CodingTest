import sys
T = int(input())

for _ in range(T):

    N = int(input())
    arr = []
    count = 0
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr.sort(key=lambda x:x[0])
    
    res = 1
    cutLine = arr[0][1]
    for i in range(1, N):
        if(arr[i][1] < cutLine):
            res+=1
            cutLine = arr[i][1]
    print(res)