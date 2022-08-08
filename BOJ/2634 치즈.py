"""
20220315
골드4 치즈
url: https://www.acmicpc.net/problem/2636
후기: 녹을 수 있는 치즈를 어떻게 구하는지 생각해내는 것이 관건이었다.
일전에 비슷한 bfs 문제를 푼 기억이 있어서 바로 생각해낼 수 있었다.

1. matrix의 제일 외곽(0행, N - 1행, 0열, M - 1열)을 구한다.
2. 외곽에서 bfs(또는 dfs)를 통해 녹을 수 있는 치즈 위치를 구한다.
3. time과 cheese_count를 센다.

O(NM * 50) = 500,000(50은 외곽을 제외하고 전부 치즈라고 할 때)밖에 되지 않으므로 완탐으로 충분히 해결할 수 있다.
"""

import sys

input_ = sys.stdin.readline

def getVisited():
    global N, M
    
    return [[False for _ in range(M)] for __ in range(N)]

def isOutOfRange(y, x):
    global N, M
    
    return not 0 <= y < N or not 0 <= x < M

def getOuter(): # 사각형 모양 판의 가장자리
    global N,M
    
    li = [(0, j) for j in range(1, M - 1)]
    li.extend([(N - 1, j) for j in range(1, M - 1)])
    li.extend([(i, 0) for i in range(1, N - 1)])
    li.extend([(i, M - 1) for i in range(1, N - 1)])
    return li

def getStarter(queue): # bfs. 가장 외곽의 치즈
    global matrix, N, M

    to_be_melt = []
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)

    visited = getVisited()
    for y, x in queue:
        visited[y][x] = True
        
    while queue:
        y, x = queue.pop()
        for direction in range(4):
            new_y, new_x = y + dy[direction], x + dx[direction]
            if isOutOfRange(new_y, new_x):
                continue

            if not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                if matrix[new_y][new_x] == 0:
                    queue.append((new_y, new_x))
                elif matrix[new_y][new_x] == 1:
                    matrix[new_y][new_x] = 0
                    to_be_melt.append((new_y, new_x))

    return to_be_melt

# initialization
cheese_count = 0
time = 0 
N, M = map(int, input_().strip().split())
matrix = [list(map(int, input_().strip().split())) for _ in range(N)]
outer = getOuter() # matrix 외곽
while True:
    to_be_melted = getStarter(outer[:])
    if not to_be_melted:
        break
    cheese_count = len(to_be_melted)
    time += 1

# print
print(time)
print(cheese_count)
