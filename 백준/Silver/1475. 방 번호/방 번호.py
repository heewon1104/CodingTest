arr = [0,1 ,2 ,3 ,4 ,5, 6,7 ,8 ,9]
count = list([0] * 10)

n = input()

for i in range(len(n)):
    count[int(n[i])] += 1

count[6] = int((count[9] + count[6] + 1)/2)
count[9] = count[6]

print(max(count))