# https://leetcode.com/problems/reverse-string/
# 리트코드 344. Reverse String

from typing import List

pal = ['h', 'e', 'l', 'l', 'o']


def reverse_string_my(s: List[str]) -> List[str]:  # 내가 작성한 코드
    rev = list()
    while len(s) > 0:
        rev.append(s.pop())
    return rev


def reverse_string_sol1(s: List[str]) -> None:  # using 'two pointer'
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string_sol2(s: List[str]) -> None:  # 'pythonic way'
    s.reverse()


print(reverse_string_my(pal))
