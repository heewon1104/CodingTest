N = int(input())
arr = list()
for _ in range(N):
    arr.append(int(input()))
count = 0
maxHeight = 0

for i in range(N):
    num = arr.pop()
    if(num > maxHeight):
        maxHeight = num
        count += 1

print(count)
