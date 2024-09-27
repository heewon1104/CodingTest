import sys

calculate = list(sys.stdin.readline().rstrip('\n').split('-'))
total = sys.maxsize

if(len(calculate[0]) == 0):
     calculate[0] = '0'

for i in range(len(calculate)):
    calculate[i] = sum(list(map(int, calculate[i].split('+'))))


if(len(calculate) == 1):
    print(calculate[0])

else:
    for length in range(1, len(calculate)):
        for i in range(1, len(calculate)+1):
            tmpsum = calculate[0]
            for j in range(1, len(calculate)):
                if(i<=j<=i+length):
                    tmpsum -= calculate[j]
                else:
                    tmpsum += calculate[j]
            total = min(total, tmpsum)
        
    print(total)