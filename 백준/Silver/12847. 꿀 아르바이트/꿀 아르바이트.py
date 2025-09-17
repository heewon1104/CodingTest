N, M = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:M])   
ans = window          

for i in range(M, N):
    window += arr[i] - arr[i - M] 
    if window > ans:
        ans = window

print(ans)