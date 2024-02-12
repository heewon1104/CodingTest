from collections import deque

n = int(input())
node = int(input())
arr = []
for _ in range(n):
    inputlist = list([0] * n)
    arr.append(inputlist)

visit = [False] * n
count = 0

for i in range(node):
    a, b = map(int,input().split())
    a-=1
    b-=1
    arr[a][b] = 1
    arr[b][a] = 1

def dfs(index):
    visit[index] = True
    for i in range(n):
        if(not visit[i] and arr[index][i] == 1):
            dfs(i)

dfs(0)

for i in range(n):
    if(visit[i] == True):
        count+=1

print(count-1)