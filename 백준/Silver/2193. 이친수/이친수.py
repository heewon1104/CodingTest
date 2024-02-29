n = int(input())
d = [[0, 0] for _ in range(n+1)]

d[1] = list([0, 1])

for i in range(2, n+1):
    d[i][0] = d[i-1][1] + d[i-1][0]
    d[i][1] = d[i-1][0]

print(sum(d[n]))