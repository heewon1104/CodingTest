import math
N =  int(input())
arr = []
prime_arr = []

for _ in range(N):
    arr.append(int(input()))

def checkPrime():
    for i in range(2, max(arr)+1):
        check_break = False
        for j in range(2, int(math.sqrt(i))+1):
            if(i % j == 0):
                check_break = True
                break
        if(not check_break):
            prime_arr.append(i)

checkPrime()

for i in arr:
    num1 = 0
    num2 = i
    for j in prime_arr:
        if(i-j in prime_arr and abs((i-j)-j) < num2 - num1):
            num1 = j
            num2 = i-j

    print(num1, num2)