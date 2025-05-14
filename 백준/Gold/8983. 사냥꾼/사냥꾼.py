N, M, L = map(int, input().split())
Hunter = list(map(int, input().split()))
Animals = []
for _ in range(M):
    Animals.append(list(map(int, input().split())))
result = 0

Hunter.sort()

for animal in Animals:
    X, Y = animal[0], animal[1]
    left, right = 0, N

    while(1):
        mid = (left + right)//2

        if(abs(X-Hunter[mid])+Y <= L):
            result += 1
            break
        if(left+1 == right or X == Hunter[mid]):
            break

        if(X > Hunter[mid]):
            left = mid
        else:
            right = mid

print(result)