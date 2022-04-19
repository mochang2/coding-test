"""
실버1 경로 찾기
url: https://www.acmicpc.net/problem/11403
후기: 문제를 잘못 읽어서 시작지 == 출발지가 같기 위해서는 cycle이 생겨야 함을 몰라 코드를 잘 못 짜고 있었다.
그래서 처음에 dfs로 해서 틀렸고 플로이드 와샬 알고리즘이라는 것을 보고 구현할 수 있었다.
"""

import sys

INF = 102  # 최대 비용: 100개를 거쳐서 다시 자기 자신에게 돌아올 때
N = int(input())
cost = [[INF for _ in range(N)] for __ in range(N)]
for i in range(N):
    for j, connected  in enumerate(list(map(int, sys.stdin.readline().strip().split()))):
        if connected == 1:
            cost[i][j] = 1
            
# 플로이드-워셜
for k in range(N): # 경유지
    for i in range(N): # 출발지
        for j in range(N): # 도착지
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(N):
    for j in range(N):
        if cost[i][j] != INF:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
