"""
20220630
골드5 치킨배달
url: https://www.acmicpc.net/problem/15686
후기: matrix가 나오길래 처음에는 dfs/bfs인줄 알았으나 완탐인 점만 같고 다른 문제였다.
M의 숫자가 작은 것을 보고 완탐임을 직감하고 조합을 돌려보니까 해결됐다.
"""

import sys
from itertools import combinations

input_ = sys.stdin.readline
MAX_VALUE = (50 + 50) * 13 * 2 # 2 <= N <= 50, 1 <= M < 13
answer = MAX_VALUE

def CalcDistance(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

# initialization
N, M = map(int, input_().strip().split())
matrix = [tuple(map(int, input_().strip().split())) for _ in range(N)]
houses = []
chickens = []

# 집과 치킨집 위치 확인
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            houses.append((i, j))
        elif matrix[i][j] == 2:
            chickens.append((i, j))

# 최소가 되는 
for chicken_candidates in combinations(chickens, M):
    result = 0
    for h_y, h_x in houses:
        min_distance = MAX_VALUE
        for c_y, c_x in chicken_candidates:
            distance = CalcDistance(h_y, h_x, c_y, c_x)
            min_distance = min(min_distance, distance)
        result += min_distance
    answer = min(answer, result)

# print
print(answer)
