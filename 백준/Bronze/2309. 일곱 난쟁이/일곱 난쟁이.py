arr = []
for _ in range(9):
    arr.append(int(input()))

def Check():
    for i in range(9):
        for j in range(i+1, 9):
            total = 0
            for k in range(9):
                if(k != i and k!=j):
                    total += arr[k]                
            if(total == 100):
                return i, j

arr.sort()
not1, not2 = Check()
for i in range(9):
    if(i != not1 and i !=not2):
        print(arr[i])