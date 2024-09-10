inputStr = input()
Stack = []
total = 0
tempInnerCal = 1
for i in range(len(inputStr)):

    if(inputStr[i] == '('):
        Stack.append('(')
        tempInnerCal *= 2

    elif(inputStr[i] == ')'):
        if(len(Stack) == 0  or Stack[-1] != '('):
            total = 0
            break
        popped = Stack.pop()
        if(inputStr[i-1] == '('):
            total += tempInnerCal
        tempInnerCal //= 2

    elif(inputStr[i] == '['):
        Stack.append('[')
        tempInnerCal *= 3

    elif(inputStr[i] == ']'):
        if(len(Stack) == 0 or Stack[-1] != '['):
            total = 0
            break
        popped = Stack.pop()
        if(inputStr[i-1] == '['):
            total += tempInnerCal
        tempInnerCal //= 3

if(len(Stack) != 0):
    total = 0

print(total)