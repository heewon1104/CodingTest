n = int(input())
res = 0

s = 0
num = 1
while(1):
    s += num
    num += 1
    res += 1
    if(s > n):
        res -= 1
        break

print(res)