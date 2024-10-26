import sys

N, M = map(int, sys.stdin.readline().split())
app = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

# 총 비용의 합 + 1 만큼 dp 배열 생성
max_cost = sum(cost)
dp = [0] * (max_cost + 1)  # dp[cost]는 비용 cost로 얻을 수 있는 최대 메모리

# dp 배열을 갱신
for i in range(N):
    memory = app[i]
    c = cost[i]
    for j in range(max_cost, c - 1, -1):
        dp[j] = max(dp[j], dp[j - c] + memory)

# 최소 비용을 찾기
for c in range(max_cost + 1):
    if dp[c] >= M:
        print(c)
        break
