N = int(input())
arr = [int(input()) for _ in range(N)]
isPrimeArr = [True] * max(arr)

for i in range(2, len(isPrimeArr)):
    for j in range(2, i):
        if(i % j == 0):
            isPrimeArr[i] = False
            break

for num in arr:
    for num1 in range(num // 2, -1, -1):
        num2 = num - num1
        if(isPrimeArr[num1] and isPrimeArr[num2]):
            print(min(num1, num2), max(num1, num2))
            break