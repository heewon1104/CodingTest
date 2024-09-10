import sys

N = int(input())
inputarr = []
locationArr = []

for i in range(N):
    x, d = map(int, sys.stdin.readline().split())
    locationArr.append([x-d, '(', False])
    locationArr.append([x+d, ')', False])

locationArr.sort(key =  lambda x : (x[0], -ord(x[1])))
# print(locationArr)

Stack = []
count = 1
for i in range(len(locationArr)):
    if(len(Stack) == 0):
        Stack.append(locationArr[i])
        continue

    else:
        if(locationArr[i][1] == '('):
            if(Stack[-1][0] == locationArr[i][0]):
                Stack[-1][2] = True
            Stack.append(locationArr[i])

        elif(locationArr[i][1] == ')'):
            if(Stack[-1][2]):
                count += 2
            else:
                count += 1
            Stack.pop()

            if(i != N*2-1):
                if(Stack and locationArr[i][0] != locationArr[i+1][0]):
                    Stack[-1][2] = False
print(count)
