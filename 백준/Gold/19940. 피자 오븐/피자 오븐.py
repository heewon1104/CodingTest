from collections import deque
import copy
T = int(input()) 
time = [60, 10, -10, 1, -1]

for _ in range(T):
    visit = [[0,0,0,0,0] for _ in range(61)]
    N = int(input())
    res = N//60
    N = N%60 

    queue = deque()

    queue.append(0)
    

    while(queue):
        popped = queue.popleft()
        if(popped < 0 or popped > 60):
            continue
        if(popped == N):
            break

        for i in range(4, -1, -1):
            if(popped+time[i] < 0 or popped+time[i] > 60):
                continue
            if(sum(visit[popped+time[i]]) != 0):
                continue
            visit[popped+time[i]] = copy.deepcopy(visit[popped])
            visit[popped+time[i]][i] += 1

            # print(popped+time[i])
            # print(visit[popped+time[i]])
            queue.append(popped+time[i])
    
    fin = copy.deepcopy(visit[N])
    fin[0] += res

    for i in range(5):
        print(fin[i], end=" ")
    print()
