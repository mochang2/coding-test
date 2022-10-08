"""
20221008
골드4 집합의 표현
url: https://www.acmicpc.net/problem/1717
후기: 너무 명백한 union-find 문제였다.
한 가지 주의할 점은 O(n) = 1,000,000이기 때문에 recursion error가 날 수 있다는 점이다.
"""

import sys

sys.setrecursionlimit(10 ** 7)
input_ = sys.stdin.readline

def find(x):
    global parents

    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    global parents
    
    parent_x = find(x)
    parent_y = find(y)

    if parent_x > parent_y:
        parents[parent_x] = parent_y
    else:
        parents[parent_y] = parent_x

n, m = map(int, input_().strip().split())
parents = [i for i in range(n + 1)]

for _ in range(m):
    command, x, y = map(int, input_().strip().split())

    if command == 0:
        union(x, y)
    else:
        parent_x = find(x)
        parent_y = find(y)

        if parent_x == parent_y:
            print('YES')
        else:
            print('NO')
