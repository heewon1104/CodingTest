N = int(input())
arr = list(map(int, input().split()))
res = [-1] * N
stack = []

prev = arr[0]
stack.append((prev, 0))

for i in range(1, N):
    if(prev < arr[i]):
        while(stack and stack[-1][0] < arr[i]):
            popped, idx = stack.pop()
            res[idx] = arr[i]
    prev = arr[i]
    stack.append((arr[i],i))

for i in res:
    print(i, end=' ')