from collections import deque

n,k = map(int, input().split())
arr = deque()
res = deque()
count = 0

for i in range(1,n+1):
    arr.append(i)

while(arr):
    num = arr.popleft()
    count += 1
    if(count == k):
        res.append(num)
        count = 0
    else:
        arr.append(num)

print("<", end="")
while(res):
    num = res.popleft()
    if(res):
        print(num, end=", ")
    else:
        print(num, end=">\n")