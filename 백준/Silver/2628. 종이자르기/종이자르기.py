import heapq

Width, Height = map(int, input().split())
cuttingWidth = [0,Width]
cuttingHeight = [0,Height]

maxWidth = 0
maxHeight = 0

N = int(input())

for i in range(N):
    cmd, idx = map(int, input().split())
    if(cmd == 0):
        heapq.heappush(cuttingHeight, idx)
    else:
        heapq.heappush(cuttingWidth, idx)

for i in range(len(cuttingHeight)-1):
    num = heapq.heappop(cuttingHeight)
    maxHeight= max(maxHeight, cuttingHeight[0] - num)

for i in range(len(cuttingWidth)-1):
    num = heapq.heappop(cuttingWidth)
    maxWidth=max(maxWidth, cuttingWidth[0] - num)

print(maxHeight*maxWidth)