"""
20220315
골드4 녹색 옷 입은 애가 젤다지?
url: https://www.acmicpc.net/problem/4485
후기: 몇 번이나 시간 초과, 메모리 초과가 떴는지 모르겠다.
처음부터 matrix로 입력된 애들을 완탐으로 dfs / bfs로 돌리면 엄청난 시간 초과가 난다는 것을 간과했다.
"""

# 첫 번째 시도. 시간 초과 실패.
# dp를 이용한 완탐.
# O(4 ** (125 ** 2)) 이므로 시간 초과 발생.

import sys

sys.setrecursionlimit(5 ** 6)

input_ = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def initVisited(n):
    return [[False for _ in range(n)] for __ in range(n)]

def initDp(n):
    return [[sys.maxsize for _ in range(n)] for __ in range(n)]

def isOutOfRange(y, x, n):
    return y < 0 or y >= n or x < 0 or x >= n

def dfs(y, x, cost, n, cave, dp, visited):
    global answer, dy, dx

    if cost > dp[y][x]: # 이미 더 싼 값으로 지나갈 수 있음
        return
    dp[y][x] = cost
    
    if y == n - 1 and x == n - 1:
        return cost

    for direction in range(4):
        new_y, new_x = y + dy[direction], x + dx[direction]

        if isOutOfRange(new_y, new_x, n) or \
           visited[new_y][new_x]:
            continue

        visited[new_y][new_x] = True
        result = dfs(new_y, new_x, cost + cave[new_y][new_x], n, cave, dp, visited)
        if result:
            answer = min(answer, result)
        visited[new_y][new_x] = False

problem = 1
        
while True:
    n = int(input_().strip()) # 동굴의 크기
    if n == 0:
        break

    answer = sys.maxsize
    cave = [list(map(int, input_().strip().split())) for _ in range(n)]
    dp = initDp(n)
    visited = initVisited(n)
    
    dfs(0, 0, cave[0][0], n, cave, dp, visited)

    print('Problem {}: {}'.format(problem, answer))
    problem += 1
    

# 정답
# 다익스트라
    
import sys
from collections import deque

input_ = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def isOutOfRange(y, x, n):
    return y < 0 or y >= n or x < 0 or x >= n

def initCost(n):
    return [[sys.maxsize for _ in range(n)] for __ in range(n)]

problem = 1
        
while True:
    n = int(input_().strip()) # 동굴의 크기
    if n == 0:
        break

    cave = [list(map(int, input_().strip().split())) for _ in range(n)]
    cost = initCost(n)
    cost[0][0] = cave[0][0]
    
    queue = deque([(0, 0)])
    while len(queue):
        y, x = queue.popleft()

        for direction in range(4):
            new_y, new_x = y + dy[direction], x + dx[direction]

            if isOutOfRange(new_y, new_x, n) or \
               cost[new_y][new_x] <= cost[y][x] + cave[new_y][new_x]: # 이미 최선의 방법이 있음. < 면 시간 초과, 메모리 초과 발생.
                continue

            cost[new_y][new_x] = cost[y][x] + cave[new_y][new_x]
            queue.append((new_y, new_x))
            
    print('Problem {}: {}'.format(problem, cost[n - 1][n - 1]))
    problem += 1
