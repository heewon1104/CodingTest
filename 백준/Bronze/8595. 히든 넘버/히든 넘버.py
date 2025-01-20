N = int(input())
str = list(input())
countDigit = 1
res = 0

for i in range(N-1, -1, -1):
    try:
        res += int(str[i]) * countDigit
        countDigit *= 10
    except:
        countDigit = 1

print(res)