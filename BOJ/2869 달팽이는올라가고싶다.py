"""
20220604
브론즈1 달팽이는 올라가고 싶다.
url: https://www.acmicpc.net/problem/2869
후기: 쉬운 수학 문제였다.
"""

import math
A, B, V = map(int, input().strip().split())
print(math.ceil((V - A) / (A - B)) + 1)
