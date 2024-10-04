import sys

N = int(sys.stdin.readline())
strarr = []
dic = {}

for i in range(N):
    inputStr = sys.stdin.readline().rstrip('\n')
    strarr.append(inputStr)

    for j in range(len(strarr[i])):
        if(strarr[i][j] not in dic):
            dic[strarr[i][j]] = 10**(len(strarr[i])-j-1)
        else:
            dic[strarr[i][j]] += 10**(len(strarr[i])-j-1)


res = list(dic.items())
res.sort(key=lambda x: x[1], reverse=True)

num = 9
result = 0

for i in range(len(res)):
    result += res[i][1] * num
    num -= 1

print(result)