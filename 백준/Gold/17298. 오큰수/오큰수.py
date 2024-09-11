import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
Stack = []
result = []

for i in range(N-1, 0, -1):
    if(not Stack):
        result.append(-1)
        Stack.append(arr[i])
        continue

    if(Stack[-1] <= arr[i]):
        while(Stack and arr[i] >= Stack[-1]):
            Stack.pop()
        
        if(not Stack):
            result.append(-1)
            Stack.append(arr[i])
        else:
            result.append(Stack[-1])
        Stack.append(arr[i])
        
    else:
        result.append(Stack[-1])
        if(arr[i-1] < arr[i]):
            Stack.append(arr[i])

while(Stack and arr[0] >= Stack[-1]):
    Stack.pop()
if(not Stack):
    result.append(-1)
else:
    result.append(Stack[-1])

for i in range(len(result)):
    print(result.pop(), end=' ')
print()