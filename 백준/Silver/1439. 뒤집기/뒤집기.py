import sys
import heapq

str = list(sys.stdin.readline().rstrip('\n'))
str2 = str[:]
countZero = 0
countOne = 0

while('0' in str):
    firstZero = -1
    lastZero = -1
    countZero += 1

    for i in range(len(str)):
        if(str[i] == '0'):
            if(firstZero == -1):
                firstZero = i
            lastZero = i

    for i in range(firstZero, lastZero+1):
        if(str[i] == '0'):
            str[i] = '1'
        else:
            str[i] = '0'

while('1' in str2):
    firstOne = -1
    lastOne = -1
    countOne += 1

    for i in range(len(str2)):
        if(str2[i] == '1'):
            if(firstOne == -1):
                firstOne = i
            lastOne = i

    for i in range(firstOne, lastOne+1):
        if(str2[i] == '1'):
            str2[i] = '0'
        else:
            str2[i] = '1'

print(min(countZero, countOne))