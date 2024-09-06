T = int(input())

for _ in range(T):
    R, str = input().split()

    for i in range(len(str)):
        for _ in range(int(R)):
            print(str[i], end='')
    print()