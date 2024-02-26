import sys
from collections import deque

while(True):
    inputStr = sys.stdin.readline().rstrip("\n")
    queue = deque()

    if(inputStr == '.'):
        break

    else:
        check = True
        for i in range(len(inputStr)):
            if(inputStr[i] == '('):
                queue.append('(')

            if(inputStr[i] == ')'):
                if(len(queue) == 0):
                    check = False
                    break
                popedStr = queue.pop()
                if(popedStr != '('):
                    check = False
                    break
    
            if(inputStr[i] == '['):
                queue.append('[')
                
            if(inputStr[i] == ']'):
                if(len(queue) == 0):
                    check = False
                    break
                popedStr = queue.pop()
                if(popedStr != '['):
                    check = False
                    break

        if(len(queue) != 0 or check == False):
            print("no")
        else:
            print("yes")
