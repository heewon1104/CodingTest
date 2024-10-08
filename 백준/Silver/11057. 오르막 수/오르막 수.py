import sys

N = int(sys.stdin.readline().strip())

dp = [[0] * 10 for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(j+1):  # j 이하의 모든 k에 대해
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= 10007  # 여기서 모듈로 연산

result = sum(dp[N]) % 10007  # 최종 결과도 모듈로 연산
print(result)
