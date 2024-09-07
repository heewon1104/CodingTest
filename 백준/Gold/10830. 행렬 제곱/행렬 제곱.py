import sys

N, B = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def matrix_multiply(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def matrix_pow(matrix, power, N):
    # 항등 행렬
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, matrix, N)
        matrix = matrix_multiply(matrix, matrix, N)
        power //= 2
    
    return result

result = matrix_pow(matrix, B, N)

for row in result:
    print(' '.join(map(str, row)))
