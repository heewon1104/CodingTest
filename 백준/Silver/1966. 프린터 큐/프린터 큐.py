from collections import deque

chance = int(input())

for _ in range(chance):
    n,k = map(int, input().split())
    queue = deque(list(map(int, input().split(" "))))
    index = deque()
    for i in range(n):
        index.append(i)

    count = 0

    while(True):
        check_biggernum = False

        num = queue.popleft()
        idx = index.popleft()

        for i in range(len(queue)):
            if(num < queue[i]):
                check_biggernum = True
                break
        
        if(check_biggernum == True):
            queue.append(num)
            index.append(idx)
        
        else:
            count += 1
            if(idx == k):
                print(count)
                break
