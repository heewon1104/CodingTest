import sys
n = int(input())

for i in range(n):
    str = sys.stdin.readline()
    count = 0
    checkstr = True
    for i in range(len(str)):
        if(str[i] == '('):
            count += 1
        if(str[i] == ')'):
            count -= 1
        if(count < 0):
            checkstr = False
            break
    if(count != 0):
        checkstr = False

    if(checkstr):
        print("YES")
    else:
        print("NO")