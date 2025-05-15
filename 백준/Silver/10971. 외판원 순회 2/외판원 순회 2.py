import sys

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = sys.maxsize

def DFS(visit, startNode, currentNode, cost):
    global result
    if(arr[currentNode][startNode] != 0 and not False in visit):
        result = min(result, cost + arr[currentNode][startNode])
        return
    
    for i in range(0, N):
        if(arr[currentNode][i] > 0 and visit[i] == False and cost + arr[currentNode][i] < result):
            visit[i] = True
            DFS(visit, startNode,  i, cost + arr[currentNode][i])
            visit[i] = False


visit = [False] * N
visit[0] = True
DFS(visit, 0, 0, 0)

print(result)
