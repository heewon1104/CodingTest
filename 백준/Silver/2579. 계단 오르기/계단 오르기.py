import sys
input = sys.stdin.readline

N = int(input())
score = [0]
for _ in range(N):
  score.append(int(input()))

Mscore = [0]*(N+1)

def stair(num):
  if num < 1:
    return 0
  if Mscore[num] != 0:
    return Mscore[num]

  Mscore[num] = max(stair(num-3)+score[num-1], stair(num-2)) + score[num]
  return Mscore[num]

print(stair(N))