import sys
sys.setrecursionlimit(10**7)

inputarr = []
graph = []

while(1):
    inputStr = sys.stdin.readline().rstrip('\n')
    if(inputStr == ''):
        break
    inputarr.append(int(inputStr))

N = len(inputarr)

def FindIdx(value):
    for i in range(len(graph)):
        if(graph[i][0] == value):
            return i
    return -1

def Setgraph():
    if(not graph):
        node = inputarr[0]
        left = -1
        right = -1
        graph.append([node, left, right])
    
    for i in range(1, N):
        parentnode = graph[0]
        while(1):
            if(inputarr[i] < parentnode[0]):
                if(parentnode[1] == -1):
                    node = inputarr[i]
                    parentnode[1] = len(graph)
                    left = -1
                    right = -1
                    graph.append([node, left, right])
                    break
                else:
                    parentnode = graph[parentnode[1]]
            else:
                if(parentnode[2] == -1):
                    node = inputarr[i]
                    parentnode[2] = len(graph)
                    left = -1
                    right = -1
                    graph.append([node, left, right])
                    break
                else:
                    parentnode = graph[parentnode[2]]


def PostOrder(nodeIdx):
    node = graph[nodeIdx][0]
    left = graph[nodeIdx][1]
    right = graph[nodeIdx][2]

    if(graph[nodeIdx][1] != -1):
        PostOrder(left)
    if(graph[nodeIdx][2] != -1):
        PostOrder(right)
    print(node)

Setgraph()
PostOrder(0)
