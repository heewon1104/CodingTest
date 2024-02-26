import sys

n = int(input())
m = int(input())
arr = input()

cursor, count, result = 0, 0, 0

while cursor < (m - 1):
    if arr[cursor:cursor + 3] == 'IOI':
        count += 1
        cursor += 2
        if count == n:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(result)