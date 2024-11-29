import sys
N = int(sys.stdin.readline())
strArr = [sys.stdin.readline().rstrip() for _ in range(N)]

def is_palindrome(s, left, right, chance_used):
    while left < right:
        if s[left] != s[right]:
            if chance_used:
                return 2
            # 하나 제거해보는 두 가지 경우를 모두 검사
            skip_left = is_palindrome(s, left + 1, right, True)
            skip_right = is_palindrome(s, left, right - 1, True)
            return min(skip_left, skip_right)
        left += 1
        right -= 1
    return 1 if chance_used else 0

def classify_palindrome(s):
    return is_palindrome(s, 0, len(s) - 1, False)

for string in strArr:
    print(classify_palindrome(string))
