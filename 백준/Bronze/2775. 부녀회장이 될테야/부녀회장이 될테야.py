T = int(input())

for _ in range(T):  
    floor = int(input())
    room = int(input())
    room0 = [x for x in range(1, room+1)]
    for k in range(floor):  
        for i in range(1, room):  
            room0[i] += room0[i-1] 
    print(room0[-1]) 