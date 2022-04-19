"""
20220313
골드5 행복 유치원
url: https://www.acmicpc.net/problem/13164
후기: 골드5 문제 같지가 않았다. 처음에는 문제가 너무 짧아서 dp인가 고민을 하다가, 부분합, 키 간의 차이 등을 고민했다.
키 간의 차이로 문제를 풀고, 틀릴줄 알고 일단 냅다 제출했는데 통과했다.
결국 풀고 보니 그리디 문제였다.
"""

import sys

N, K = map(int, sys.stdin.readline().strip().split())
heights = list(map(int, sys.stdin.readline().strip().split())) # 기본적으로 오름차순으로 정렬되어서 들어옴
d_heights = [0 for _ in range(N - 1)] # height 간의 차이
for i in range(N - 1):
    d_heights[i] = heights[i + 1] - heights[i]
d_heights.sort(reverse=True)

print(sum(d_heights[K - 1:]))
