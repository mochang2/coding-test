"""
20220417
골드4 마법사 상어와 파이어스톰
url: https://www.acmicpc.net/problem/20058
후기: 효율적인 방법을 고민해보려다가 삽질을 좀 했다.
90도 회전하는 부분에서 회전한 결과를 임시 변수에 저장하지 않고 제자리에서 회전하는 방법을 사용하면, 시간복잡도도, 공간복잡도도 감소할 것이라고 생각했다.
하지만 90도 회전을 임시변수 없이 제자리에서 하면 사라지는 데이터가 생긴다(이를 간과해서 삽질함..)
어쨌든 회전한 결과를 저장하기 위한 임시 변수가 필요했고 그냥 속편히 grid와 같은 크기의 변수를 선언했다(더 효율적인 방법이 있었겠지만 index 계산이 귀찮았다).
"""

import sys
from collections import deque
input_ = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

N, Q = map(int, input_().strip().split())
grid = []
grid_length = 2 ** N # grid 한 변의 길이
for _ in range(grid_length):
    grid.append(list(map(int, input_().strip().split())))
L_li = list(map(int, input_().strip().split()))
temp_grid = [[0 for _ in range(grid_length)] for __ in range(grid_length)]
                                                        
for L in L_li: #O(2^2N * L) <= O(2^2N * N)
    level_length = 2 ** L
    # 1. 90도 회전
    for i in range(0, grid_length, level_length):
        for j in range(0, grid_length, level_length):
            x = j + level_length - 1
            for k in range(i, i + level_length):
                y = i
                for m in range(j, j + level_length):
                    temp_grid[y][x] = grid[k][m]
                    y += 1
                x -= 1

            for k in range(i, i + level_length):
                for m in range(j, j + level_length):
                    grid[k][m] = temp_grid[k][m]

    # 2. 얼음의 양이 줄어듦
    to_be_reduced = []
    for i in range(grid_length):
        for j in range(grid_length):
            count = 0
            for direct in range(4):
                new_y, new_x = i + dy[direct], j + dx[direct]
                if not 0 <= new_y < grid_length or not 0 <= new_x < grid_length:
                    continue
                if grid[new_y][new_x] > 0:
                    count += 1
            if count < 3:
                to_be_reduced.append((i, j))

    for y, x in to_be_reduced:
        if grid[y][x] > 0:
            grid[y][x] -= 1
            
# 남아있는 얼음의 합
answer1 = 0
for i in range(grid_length):
    answer1 += sum(grid[i])
    
# 가장 큰 덩어리가 차지하는 칸의 개수
visited = [[False for _ in range(grid_length)] for __ in range(grid_length)]
answer2 = 0
for i in range(grid_length):
    for j in range(grid_length):
        if visited[i][j] or grid[i][j] == 0:
            continue

        count = 0
        queue = deque([(i, j)])
        while len(queue) != 0:
            y, x = queue.popleft()
            for direct in range(4):
                new_y, new_x = y + dy[direct], x + dx[direct]
                if not 0 <= new_y < grid_length or not 0 <= new_x < grid_length:
                    continue

                if not visited[new_y][new_x] and grid[new_y][new_x] != 0:
                    count += 1
                    visited[new_y][new_x] = True
                    queue.append((new_y, new_x))
        answer2 = max(answer2, count)
            
print(answer1)
print(answer2)
