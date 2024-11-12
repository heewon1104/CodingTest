# 비슷한 단어
import sys
N  = int(sys.stdin.readline())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip('\n'))

appendixArr = [[] for _ in range(N)]
def calculateAppendix(idx, str):
    tmp = ''
    for i in range(len(str)):
        tmp += str[i]
        appendixArr[idx].append(tmp)

for i in range(N):
    calculateAppendix(i, words[i])


def compareStr(idx1, idx2):
    count = 0
    if(words[idx1] != words[idx2]):
        length = min(len(appendixArr[idx1]), len(appendixArr[idx2]))
        for i in range(length):
            if(appendixArr[idx1][i] == appendixArr[idx2][i]):
                count += 1
            else:
                break
    return count

samecount = 0

for i in range(N):
    for j in range(i+1, N):
        value = compareStr(i, j)
        if(samecount < value):
            samecount = value
            resWord1 = words[i]
            resWord2 = words[j]

print(resWord1)
print(resWord2)
