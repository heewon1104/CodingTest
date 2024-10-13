# 후위 표기식
import sys

inputStr = list(sys.stdin.readline().rstrip('\n'))
stack = []
operator = {'+' : 1, '-': 1, '*':2, '/':2, '(':3, ')':3}

for i in range(len(inputStr)):
    if(inputStr[i] not in operator):
        print(inputStr[i], end='')
        continue

    if(inputStr[i] == '('):
        stack.append(inputStr[i])
        continue

    if(len(stack) == 0):
        stack.append(inputStr[i])
    else:
        if(inputStr[i] != ')'):
            if(operator[inputStr[i]] > operator[stack[len(stack)-1]]):
                stack.append(inputStr[i])
            else:
                while(len(stack) != 0 and operator[inputStr[i]] <= operator[stack[len(stack)-1]] and stack[len(stack)-1] != '('):
                    print(stack.pop(), end='')
                stack.append(inputStr[i])
        else:
            while(len(stack) != 0):
                    current = stack.pop()
                    if(current == '('):
                        break
                    print(current, end='')

while(len(stack) != 0):
    print(stack.pop(), end='')

print()