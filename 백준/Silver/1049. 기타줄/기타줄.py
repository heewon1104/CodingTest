N, M = map(int, input().split())

minSetPrice = 1001
minLinePrice = 1001
arr = []
for i in range(M):
    lineSet, line = map(int, input().split())
    arr.append([lineSet, line])
    minSetPrice = min(lineSet, minSetPrice)
    minLinePrice = min(minLinePrice, line)

total1 = (N//6) * min(minSetPrice, minLinePrice*6) 
total2 = min(minSetPrice, minLinePrice*(N%6))

print(total1 + total2)

