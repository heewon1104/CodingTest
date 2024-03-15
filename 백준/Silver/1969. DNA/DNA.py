import sys

N, M = map(int, input().split())

arr = []
res = [0] * N
for i in range(N):
    arr.append(sys.stdin.readline().rstrip('\n'))

letter = ['A', 'C', 'G', 'T']
letteridx = [[0, 0, 0, 0] for _ in range(M)]
for i in range(M):
    # A, C, G, T
    for j in range(N):
        for k in range(4):
            if(arr[j][i] == letter[k]):
                letteridx[i][k] += 1


total = 0
for i in range(M):
    idx = -1
    count = -1
    for j in range(4):
        if(count < letteridx[i][j]):
            count = letteridx[i][j]
            idx = j

    print(letter[idx],end="")
    total += sum(letteridx[i]) - count
print()
print(total)



