"""
220227
골드5 회장뽑기
url: https://www.acmicpc.net/problem/2660
후기: 플로이드 와샬을 까먹어서 결국 다시 검색했다. 3중 for문이 k(경유지), i(출발지), j(도착지) 순이다.
처음 문제 읽었을 때 union find 생각했는데, 문제 선정 시 플로이드 와샬이란 거 몰랐으면 좀 헷갈릴 뻔 했다.
"""

import sys

def init_input(x):
    return int(x) - 1

# 초기화
INF = 1000
N = int(input())   # <= 50
friends = [[INF for _ in range(N)] for __ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            friends[i][j] = 0
score = [0 for _ in range(N)]
while True:
    a, b = map(init_input, sys.stdin.readline().strip().split())
    if (a, b) == (-2, -2):
        break
    friends[a][b] = 1
    friends[b][a] = 1

# 플로이드 와샬  O(N^3)
for k in range(N):  # 중간지점
    for i in range(N):  # 출발지점
        for j in range(N):  # 도착지점
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])

# 각 회원별 점수 산출
for i in range(N):
    max_ = -INF
    for j in range(N):
        max_ = max(max_, friends[i][j])
    score[i] = max_

# print answer
res = min(score)
ans = []
cnt = 0
for i in range(N):
    if score[i] == res:
        cnt += 1
        ans.append(i + 1)

print(res, cnt)
for i in range(cnt):
    print(ans[i], end=" ")
