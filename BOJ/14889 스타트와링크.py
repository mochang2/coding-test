"""
20220725
실버2 스타트와 링크
url: https://www.acmicpc.net/problem/14889
후기: 조합을 이용한 백트래킹 문제였다.
아마 백트래킹으로 직접 조합을 구하라고 하면 어려운 문제였겠지만
역시 파이썬... 없는 게 없다.

N <= 20이므로 시간복잡도는 O(20C10 * 10 * 10C2) = 80,000,000이다.
"""

import sys
from itertools import combinations

input_ = sys.stdin.readline
MAX = 101

# initialization
answer = MAX
N = int(input_().strip())
matrix = [list(map(int, input_().strip().split())) for _ in range(N)]
numbers = set([i + 1 for i in range(N)]) # 1 ~ N

for start in combinations(numbers, N // 2):
    link = numbers - set(start)
    
    start_score = 0
    for a, b in combinations(start, 2):
        start_score += matrix[a - 1][b - 1]
        start_score += matrix[b - 1][a - 1]

    link_score = 0
    for a, b in combinations(link, 2):
        link_score += matrix[a - 1][b - 1]
        link_score += matrix[b - 1][a - 1]

    answer = min(answer, abs(start_score - link_score))

# print
print(answer)
