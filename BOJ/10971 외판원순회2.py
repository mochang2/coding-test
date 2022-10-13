"""
20221013
실버2 외판원 순회2
url: https://www.acmicpc.net/problem/10971
후기: 2089 외판원 순회을 풀고 나서 푸니까 너무 쉬웠다.
자세한 설명은 해당 문제에 있다.

2089와 달리 dp를 쓰지 않아도 충분한 n의 크기라서 사용하지 않았다.
"""

# 완탐

import sys

input_ = sys.stdin.readline

def dfs(current, visited):
    global costs, ALL_VISITED, INF
    
    if visited == ALL_VISITED:
        return costs[current][0] or INF # 이어져 있다면 or 이어져 있지 않다면

    min_cost = INF
    
    for next_vertex in range(1, n):
        if visited & (1 << next_vertex) != 0 or costs[current][next_vertex] == 0 :# 이미 방문했거나 current와 next_vertex가 이어져있지 않다면
            continue

        min_cost = min(min_cost, costs[current][next_vertex] + dfs(next_vertex, visited + (1 << next_vertex)))

    return min_cost

# initializiation
n = int(input_().strip()) # cities
costs = [list(map(int, input_().strip().split())) for _ in range(n)]
INF = sys.maxsize
ALL_VISITED = 2 ** n - 1
print(dfs(0, 1))
