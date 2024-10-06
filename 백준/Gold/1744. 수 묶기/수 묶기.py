import sys
import heapq

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    heapq.heappush(arr, -int(sys.stdin.readline()))

res = 0
checkIndex = 0

while(arr):
    num1 = -heapq.heappop(arr)
    if(len(arr) == 0):
        res += num1
        break
    
    num2 = -heapq.heappop(arr)
    if(len(arr) % 2 ==0):
        res += max(num1*num2, num1+num2)
    else:
        if(len(arr) > 0 and max(num1*num2, num1+num2) < max(num2*-(arr[0]), num2-(arr[0]))):
            res += num1
            heapq.heappush(arr, -num2)
        else:
            if(num2 == 0):
                res += num1
                heapq.heappush(arr, -num2)
            else:
                res += max(num1*num2, num1+num2)
        
print(res)