import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화
dp = [[-sys.maxsize] * M for _ in range(N)]

# 첫 행 초기화
dp[0][0] = area[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j - 1] + area[0][j]

# DP 계산
for i in range(1, N):
    # 왼쪽에서 오른쪽으로
    left = [-sys.maxsize] * M
    left[0] = dp[i - 1][0] + area[i][0]
    for j in range(1, M):
        left[j] = max(left[j - 1], dp[i - 1][j]) + area[i][j]

    # 오른쪽에서 왼쪽으로
    right = [-sys.maxsize] * M
    right[M - 1] = dp[i - 1][M - 1] + area[i][M - 1]
    for j in range(M - 2, -1, -1):
        right[j] = max(right[j + 1], dp[i - 1][j]) + area[i][j]

    # 현재 행의 dp 계산
    for j in range(M):
        dp[i][j] = max(left[j], right[j])

# 결과 출력
print(dp[N - 1][M - 1])
