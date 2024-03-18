inputStr = input()
L = len(inputStr)
zero, one = 0, 0

for i in range(L):
    if(inputStr[i] == '0'):
        zero += 1
    else:
        one+=1

for i in range(zero//2):
    print('0', end='')

for i in range(one//2):
    print('1', end='')
print()