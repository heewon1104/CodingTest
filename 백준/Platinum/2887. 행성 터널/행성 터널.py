import sys
import heapq

# 입력 처리
N = int(sys.stdin.readline())
nodeX = []
nodeY = []
nodeZ = []

# 좌표 입력 및 저장
for i in range(1, N+1):
    X, Y, Z = map(int, sys.stdin.readline().split())
    nodeX.append([X, i])
    nodeY.append([Y, i])
    nodeZ.append([Z, i])

# 간선 리스트 초기화
edge = []

# 각 좌표축(x, y, z)별로 정렬한 후 인접한 노드 간의 거리 계산
nodeX.sort()
nodeY.sort()
nodeZ.sort()

for i in range(N-1):
    distance = abs(nodeX[i][0]-nodeX[i+1][0])
    heapq.heappush(edge, [distance, nodeX[i][1], nodeX[i+1][1]])

    distance = abs(nodeY[i][0]-nodeY[i+1][0])
    heapq.heappush(edge, [distance, nodeY[i][1], nodeY[i+1][1]])

    distance = abs(nodeZ[i][0]-nodeZ[i+1][0])
    heapq.heappush(edge, [distance, nodeZ[i][1], nodeZ[i+1][1]])

# 부모 배열과 랭크 배열 초기화
parent = [i for i in range(N+1)]
rank = [0] * (N+1)
res = 0

# 경로 압축을 사용하는 Find 함수
def FindRoot(node):
    if node != parent[node]:
        parent[node] = FindRoot(parent[node])  # 경로 압축 적용
    return parent[node]

# 랭크를 사용하는 Union 함수
def CompareRoot(Node1, Node2):
    root1 = FindRoot(Node1)
    root2 = FindRoot(Node2)

    if root1 == root2:
        return True
    
    # 랭크를 비교하여 트리 병합
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    elif rank[root2] > rank[root1]:
        parent[root1] = root2
    else:
        parent[root1] = root2
        rank[root2] += 1  # 랭크 증가 수정
    return False

# 간선 선택 및 MST 구성
count = 0  # MST에서 간선 개수 카운트
while edge:
    if count == N - 1:  # MST는 N-1개의 간선으로 완성됨
        break
    cost, poppedNode1, poppedNode2 = heapq.heappop(edge)
    if not CompareRoot(poppedNode1, poppedNode2):  # 사이클이 생기지 않았다면
        res += cost
        count += 1

# 결과 출력
print(res)
