n = input()

if(not '0' in  n):
    print("-1")

else:
    res = 0
    for i in range(len(n)):
        res += int(n[i])
    
    if(res % 3 != 0):
        print("-1")
    else:
        arr = sorted(n, reverse = True)
        answer = ''.join(arr)
        print(answer)