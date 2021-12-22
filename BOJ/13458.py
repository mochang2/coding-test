"""
211110
브론즈2 시험 감독
url: https://www.acmicpc.net/problem/13458
후기: 쉬웠다.
"""

import math
import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

res = N
for i in range(N):
    A[i] -= B

for num in A:
    if num > 0:
        res += math.ceil(num / C)

print(res)
