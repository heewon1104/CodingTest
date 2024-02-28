from collections import deque

N, M, K, X = map(int, input().split())

arr = []
for i in range(N+1):
    arr.append(list([] * (N+1)))

for i in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)

visit = [-1] * (N+1)

queue = deque()
queue.append([X, 0])

while(queue):
    tmp = queue.popleft()
    
    if(visit[tmp[0]] != -1):
        continue

    visit[tmp[0]] = tmp[1]

    for i in range(len(arr[tmp[0]])):
        queue.append([arr[tmp[0]][i], tmp[1]+1])

checknone = True
for i in range(1, N+1):
    if(K == visit[i]):
        checknone = False
        print(i)

if(checknone):
    print(-1)