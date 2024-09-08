N = int(input())
arr = list(map(int, input().split()))
Stack = [[arr[0],0]]
print(0, end=' ')

for i in range(1, N):

    while(1):
        if(len(Stack) == 0):
            print(0, end=' ')
            break
         # Stack의 Top이 배열의 현재 값보다 작으면
        if(Stack[-1][0] < arr[i]):
            #해당 값은 필요 없으므로 pop, 현재값 push
            Stack.pop()
        else:
            print(Stack[-1][1] +1, end=' ')
            break
    
    Stack.append([arr[i], i])
