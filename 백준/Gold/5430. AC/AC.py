import sys 
from collections import deque

chance = int(input())

for i in range (chance):
    check_err = False
    command = list(sys.stdin.readline())
    arr_size = int(sys.stdin.readline())

    input_arr = list(sys.stdin.readline().strip('[]\n').split(","))
    queue = deque(input_arr)
    count_reverse = False

    for j in range(len(command)):
        if(command[j] == 'R'):
            if(count_reverse == False):
                count_reverse = True
            else:
                count_reverse = False

        elif(command[j] == 'D'):
            if(arr_size == 0):
                 check_err = True
                 print("error")
                 break
            
            if(count_reverse == False):
                queue.popleft()
            else:
                queue.pop()
            
            arr_size -= 1

    if(check_err == False):
        print("[", end="")

        if(count_reverse == True):
            while(queue):
                print(queue.pop(), end="")

                if(queue):
                    print(",", end="")
                
        else:
            while(queue):
                print(queue.popleft(), end="")

                if(queue):
                    print(",", end="")
        
        print("]")