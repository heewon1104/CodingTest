import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
value = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
minnum = sys.maxsize
maxnum = -sys.maxsize

def Dfs(valueIdx, add, sub, mul, div, total):
    global minnum, maxnum
    if(valueIdx == N):
        maxnum = max(total, maxnum)
        minnum = min(total, minnum)
        return
    
    if(add > 0):
        Dfs(valueIdx+1, add-1, sub, mul, div, total + value[valueIdx])
    if(sub > 0):
        Dfs(valueIdx+1, add, sub-1, mul, div, total - value[valueIdx])
    if(mul > 0):
        Dfs(valueIdx+1, add, sub, mul-1, div,  total * value[valueIdx])
    if(div > 0):
        if(total < 0):
            Dfs(valueIdx+1, add, sub, mul, div-1,  -(abs(total) // value[valueIdx]))
        else:
            Dfs(valueIdx+1, add, sub, mul, div-1, total //value[valueIdx])

total = value[0]
Dfs(1, add, sub, mul, div, total)
print(maxnum)
print(minnum)