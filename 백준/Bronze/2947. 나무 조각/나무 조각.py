arr = list(map(int, input().split()))

while(1):
    check = True

    for i in range(4):
        if(arr[i] > arr[i+1]):
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp

            for k in range(5):
                print(arr[k], end=' ')
            print()

    for i in range(5):
        for j in range(i, 5):
            if(arr[i] > arr[j]):
                check = False
    
    if(check):
        break