N = int(input())
count = 0

if(len(str(N)) < 3):
    print(N)
else:
    count += 99
    for gap in range(0, 10):
        for i in range(1, 10):
            x = i
            y = i+gap
            z = i+gap*2

            total = x*100 + y*10+ z
            if(y and z < 10 and total <= N):
                count += 1

        for i in range(1, 10):
            x = i
            y = i-gap
            z = i-gap*2

            total = x*100 + y*10+ z
            if(y and z >= 0 and x != y and total <= N):
                count += 1
    print(count)