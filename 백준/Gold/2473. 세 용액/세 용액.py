# 세 용액
import sys

N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

res = [sys.maxsize, sys.maxsize, sys.maxsize]

for start in range(N-1):
    mid = start + 1
    end = N-1
    while(mid != end):
        if(abs(sum(res)) > abs(liquid[start]+liquid[mid]+liquid[end])):
            res = [liquid[start], liquid[mid], liquid[end]]
        
        if(liquid[start]+liquid[mid]+liquid[end] > 0):
            end -= 1
        elif(liquid[start]+liquid[mid]+liquid[end]  < 0):
            mid += 1
        else:
            break

print(' '.join(map(str, res)))
  