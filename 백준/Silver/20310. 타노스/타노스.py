inputStr = list(input())
zero = inputStr.count('0')
one = inputStr.count('1')

count = 0
for i in inputStr:
    if(i == '1'):
        count += 1
        inputStr.remove(i)
    if(count == one//2):
        break

count = 0
for i in range(len(inputStr)-1, -1, -1):
    if(inputStr[i] == '0'):
        count += 1
        del inputStr[i]
    if(count == zero//2):
        break

for i in range(len(inputStr)):
    print(inputStr[i], end='')