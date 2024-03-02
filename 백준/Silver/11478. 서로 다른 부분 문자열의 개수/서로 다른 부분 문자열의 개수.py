inputStr = input()
idxArr = []
arr = set()

arr.add(inputStr)
for i in range(len(inputStr)):
    for j in range(1, len(inputStr)):
        arr.add(inputStr[i:i+j])

print(len(arr))