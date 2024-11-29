# 회문
import sys
N = int(sys.stdin.readline())
strArr = [sys.stdin.readline().rstrip() for _ in range(N)]

def is_palindrome(s, left, right, chance_used):
    while(left < right):
        if(s[left] != s[right]):
            if(chance_used):
                return 2
            skip_left = is_palindrome(s, left + 1, right, True)
            skip_right = is_palindrome(s, left, right - 1, True)
            return min(skip_left, skip_right)
        left += 1
        right -= 1
    if(chance_used):
        return 1 
    else:
        return 0

for string in strArr:
    print(is_palindrome(string, 0, len(string) - 1, False))
