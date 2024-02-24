arr = input().split('-')

res = 0
startidx = 0
if(arr[0] == ''):
    tmp = arr[1].split('+')
    for i in range(len(tmp)):
        res -= int(tmp[i])
    startidx = 2
else:
    tmp = arr[0].split('+')
    for i in range(len(tmp)):
        res += int(tmp[i])
    startidx = 1

for i in range(startidx, len(arr)):
    tmp = arr[i].split('+')
    for j in range(len(tmp)):
        res -= int(tmp[j])

print(res)