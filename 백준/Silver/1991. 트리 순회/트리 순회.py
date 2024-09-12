N = int(input())
graph = []

for i in range(N):
    node, left, right = input().split()
    graph.append([node, left, right])

def Preorder(nodeIdx):
    node = graph[nodeIdx][0]    
    left = graph[nodeIdx][1]
    right = graph[nodeIdx][2]

    leftIdx = -1
    rightIdx = -1

    for i in range(N):
        if(graph[i][0] == left):
            leftIdx = i
        if(graph[i][0] == right):
            rightIdx = i

    print(node, end='')
    if(left != '.'):
        Preorder(leftIdx)
    if(right != '.'):
        Preorder(rightIdx)

def Inorder(nodeIdx):
    node = graph[nodeIdx][0]    
    left = graph[nodeIdx][1]
    right = graph[nodeIdx][2]

    leftIdx = -1
    rightIdx = -1

    for i in range(N):
        if(graph[i][0] == left):
            leftIdx = i
        if(graph[i][0] == right):
            rightIdx = i

    if(left != '.'):
        Inorder(leftIdx)
    print(node, end='')
    if(right != '.'):
        Inorder(rightIdx)

def Postorder(nodeIdx):
    node = graph[nodeIdx][0]    
    left = graph[nodeIdx][1]
    right = graph[nodeIdx][2]

    leftIdx = -1
    rightIdx = -1

    for i in range(N):
        if(graph[i][0] == left):
            leftIdx = i
        if(graph[i][0] == right):
            rightIdx = i

    if(left != '.'):
        Postorder(leftIdx)
    if(right != '.'):
        Postorder(rightIdx)
    print(node, end='')

Preorder(0)
print()
Inorder(0)
print()
Postorder(0)
print()