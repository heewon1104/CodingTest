N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(input())

res = 0
length = min(N, M) - 1
while(1):
    flag = False
    for i in range(0, N-length):
        for j in range(0, M-length):
            if(arr[i][j] == arr[i][j+length] == arr[i+length][j] == arr[i+length][j+length]):
                flag = True
                break
        if(flag):
            break
    if(flag):
        break
    length-=1
    
    
print((length+1)*(length+1))