from collections import deque
# BFS로 풀었을때
n = int(input())
node = int(input())

arr = []
for _ in range(n):
    arr.append(list([0] * n))

for _ in range(node):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    arr[a][b] = 1
    arr[b][a] = 1

visit = [False] * n
count = 0


queue = deque()
queue.append(0)

while(queue):
    num = queue.popleft()
    visit[num] = True
    
    for i in range(n):
        if(not visit[i] and arr[num][i] == 1):
            queue.append(i)

for i in range(n):
     if(visit[i] == True):
         count+=1

print(count-1)
    

# DFS로 풀었을때
# n = int(input())
# node = int(input())
# arr = []
# for _ in range(n):
#     inputlist = list([0] * n)
#     arr.append(inputlist)

# visit = [False] * n
# count = 0

# for i in range(node):
#     a, b = map(int,input().split())
#     a-=1
#     b-=1
#     arr[a][b] = 1
#     arr[b][a] = 1

# def dfs(index):
#     visit[index] = True
#     for i in range(n):
#         if(not visit[i] and arr[index][i] == 1):
#             dfs(i)

# dfs(0)

# for i in range(n):
#     if(visit[i] == True):
#         count+=1

# print(count-1)