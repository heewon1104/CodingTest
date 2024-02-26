import sys

n = int(input())
m = int(input())
arr = input()
checkarr = []

for i in range(n+1):
    checkarr.append('I')
    if(i != n):
        checkarr.append('O')

res = 0
for i in range(0, m-(2*n)):
    slicedStr = list(arr[i:i+(2*n+1)])
    if(slicedStr == checkarr):
        res+=1
print(res)