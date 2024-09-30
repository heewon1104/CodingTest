import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    score = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    score.sort(key=lambda x: x[1])

    count = 1
    startScore = score[0][0]
    for i in range(1, N):
        if(score[i][0] < startScore):
            startScore = score[i][0]
            count += 1
        
    print(count)