import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 접두합: P[0]=0, P[i]=arr[0..i-1] 합
P = [0] * (N + 1)
for i in range(1, N + 1):
    P[i] = P[i - 1] + arr[i - 1]

# 길이 >= M 최대 구간합
# i를 M..N까지 돌며, j는 0..(i-M) 중 P[j] 최소값을 사용
min_pref = P[0]           # 현재까지의 P[0..i-M] 중 최소값
ans = 0             # 또는 -sys.maxsize-1

for i in range(M, N + 1):
    # i 시점에서 사용할 수 있는 시작 j의 새 후보는 (i-M)
    if P[i - M] < min_pref:
        min_pref = P[i - M]

    # 길이 >= M을 만족하는 최댓값 후보
    cand = P[i] - min_pref
    if cand > ans:
        ans = cand

print(ans)