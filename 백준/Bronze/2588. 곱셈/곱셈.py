num1 = int(input())
num2 = int(input())

result1 = num1 * (num2%10)
result2 = (num1 * (int(num2/10) % 10))
result3 = (num1 * (int(num2/100) % 10))

print(result1)
print(result2)
print(result3)

print(result1 + result2*10 + result3*100)

