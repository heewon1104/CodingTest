N = int(input())
arr = list(map(int, input().split()))
stack = []

prev = arr[N-1]
res = [0] * N

stack.append((prev, N-1))
for i in range(N-2, -1, -1):

    if(prev < arr[i]):
        while(len(stack) != 0  and stack[-1][0] < arr[i]):
            popped, idx = stack.pop()
            res[idx] = i+1
    prev = arr[i]
    stack.append((arr[i], i))

for i in res:
    print(i, end=' ')
