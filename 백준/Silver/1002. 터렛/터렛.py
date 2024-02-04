import math

chance = int(input())

for i in range (chance):
    inputarr = list(map(int , input().split(' ')))

    distance = math.sqrt(pow(inputarr[0]-inputarr[3],2) +pow(inputarr[1]- inputarr[4],2))
    add_radius = inputarr[5] + inputarr[2]
    sub_radius = abs(inputarr[5] - inputarr[2])

    # 두 원이 같은 경우
    if(distance == 0 and sub_radius == 0):
        print(-1)
        continue

    # 두 원이 두점에서 만나는 경우
    if(sub_radius < distance and distance < add_radius):
        print(2)
    
    # 두 원이 내접 혹은 외전하는 경우
    elif(sub_radius == distance or distance == add_radius):
        print(1)
    
    else:
        print(0)