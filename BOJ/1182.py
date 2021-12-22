"""
211206
실버2 부분수열의 합
url: https://www.acmicpc.net/problem/1182
후기: 파이썬 itertools 진짜 너무 좋다. N의 최대값이 20이므로 최대 가능한 combinations 개수는 2 ^ 20 - 1 즉, 100만 정도이다.
따라서 combinations을 이용한 풀이가 가능하다고 판단했다.
"""

import sys
from itertools import combinations
N, S = map(int, sys.stdin.readline().strip().split())  # N은 입력되는 수열의 개수, S는 부분수열의 합으로 만들어야 되는 수
li = list(map(int, sys.stdin.readline().strip().split()))

count = 0
for i in range(1, N + 1):
    for comb in list(combinations(li, i)):
        if sum(comb) == S:
            count+=1
print(count)
