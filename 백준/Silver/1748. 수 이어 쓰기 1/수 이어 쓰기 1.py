import math

n = int(input())
total = 0
count = 0

count = math.floor(math.log10(n)) 

for i in range(0, count):
    total += (pow(10, i) * 9) * (i+1)

total += (n - pow(10, count) + 1) * (count +1)

print(total)

