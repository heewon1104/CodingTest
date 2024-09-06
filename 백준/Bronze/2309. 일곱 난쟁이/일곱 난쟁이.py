from itertools import combinations

arr = []
total = 0

for _ in range(9):
    arr.append(int(input()))


answer = list(combinations(arr, 7))

for i in range(len(answer)):
    if(sum(answer[i]) == 100):
        answerList = list(answer[i])
        answerList.sort()

        for i in answerList:
            print(i)
        break