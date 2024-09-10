N, K = map(int, input().split())
str = input()
Stack = []
Stack.append(int(str[0]))
count = 0
for i in range(1, N):

    if(count == K):
        Stack.append(int(str[i]))
        continue

    else:
        while(Stack and int(Stack[-1]) < int(str[i])):
            if(count == K):
                break
            Stack.pop()
            count += 1
        
        Stack.append(int(str[i]))

if(count < K):
    for i in range(K - count):
        Stack.pop()
        
for i in Stack:
    print(i, end='')
print()