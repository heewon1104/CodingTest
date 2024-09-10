import sys
input = sys.stdin.readline


def calc(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2


n = int(input())
graph = sorted([tuple(map(int, input().split())) for _ in range(n)])


def dq(left, right):
    if left == right:
        return float('inf')
    elif right - left == 1:
        return calc(graph[left], graph[right])

    mid = (left + right) // 2
    ans = min(dq(left, mid), dq(mid + 1, right))

    coor = []
    for i in range(left, right + 1):
        d = graph[i][0] - graph[mid][0]
        if d ** 2 < ans:
            coor.append(graph[i])

    coor.sort(key=lambda x: x[1])

    for i in range(len(coor) - 1):
        for j in range(i + 1, len(coor)):
            d = coor[i][1] - coor[j][1]
            if d ** 2 < ans:
                ans = min(ans, calc(coor[i], coor[j]))
            else:
                break

    return ans


print(dq(0, n - 1))
