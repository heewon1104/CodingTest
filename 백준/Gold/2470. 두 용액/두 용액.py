import sys 

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = N - 1
res = 9876543210
num1, num2 = arr[0], arr[N-1]


arr.sort()

while(end > start):
  total = arr[start] + arr[end]

  if(abs(total) < abs(res)):
    res = total
    num1 = arr[start]
    num2 = arr[end]
  
  if(total < 0):
    start += 1

  elif(total > 0):
    end -= 1

  else:
    break

print(num1, num2)
    