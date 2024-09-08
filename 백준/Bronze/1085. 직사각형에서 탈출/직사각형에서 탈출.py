X, Y, W, H = map(int, input().split())


print(min(H-Y, W-X, X, Y))