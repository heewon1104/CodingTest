import sys

N = int(sys.stdin.readline())
time = []
for i in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key=lambda x: (x[1], x[0]))

result = 0
endTime = 0

for i in range(N):
    if(time[i][0] >= endTime): 
        result += 1
        endTime = time[i][1] 

print(result)
