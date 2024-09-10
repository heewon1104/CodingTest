N, C = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

start = 0
end = arr[N-1]- arr[0]+1
res = 0

while(start+1 < end):
    mid = (start + end)//2
    prevhouse = arr[0]
    count = 1
    for i in range(1, N):
        if(arr[i] - prevhouse >= mid):
            count += 1
            prevhouse = arr[i]
    
    if(count >= C):
        res = max(res, mid)
        start = mid

    else:
        end = mid

print(res)