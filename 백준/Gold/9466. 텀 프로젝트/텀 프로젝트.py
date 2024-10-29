import sys
sys.setrecursionlimit(10**5)

def DFS(start, next):
    global count
    res = False
    if(start == next):
        return True

    if(not visited[next]):
        visited[next] = True
        count += 1
        res = DFS(start, students[next]-1)
        visited[next] = False
    return res

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    visited = [False] * N
    in_cycle = [False] * N  # Cycle에 포함된 노드 기록
    res = N

    for i in range(N):
        if not visited[i]:  # 이미 탐색한 학생은 건너뜁니다.
            path = []
            while not visited[i]:
                visited[i] = True
                path.append(i)
                i = students[i] - 1

            # Cycle을 발견했을 때 처리
            if i in path:
                cycle_start = path.index(i)
                for j in path[cycle_start:]:
                    in_cycle[j] = True
                res -= len(path) - cycle_start

    print(res)
