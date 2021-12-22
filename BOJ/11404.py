"""
211125
골드4 플로이드
url: https://www.acmicpc.net/problem/11404
후기: 플로이드 와샬 알고리즘. 출발지 -> 목적지 쌍이 동일한 버스가 여러 개 입력될 수 있어서 입력받을 때 고려해야 함.
그리고 입력될 수 있는 cost가 100000이하일 뿐 INF는 그것보다 훨씬 크게 잡아야 했음.
"""

import sys

INF = 100000000
n = int(input()) # 도시 개수
cost = [[INF for _ in range(n)] for __ in range(n)] # 비용 초기화
for i in range(n): # 출발지 == 목적지일 경우
    cost[i][i] = 0
    
m = int(input()) # 버스 개수
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    cost[a - 1][b - 1] = min(c, cost[a - 1][b - 1])

# floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(n):
    for j in range(n):
        if cost[i][j] == INF:
            print(0, end=" ")
        else:
            print(cost[i][j], end=" ")
    print()
