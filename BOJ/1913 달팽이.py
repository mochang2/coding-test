"""
211215
실버5 달팽이
url: https://www.acmicpc.net/problem/1913
후기: 빡구현. direction이란 변수 덕분에 쉽게 할 수 있었다.
"""

N = int(input())
target = int(input())

grid = [[0 for _ in range(N)] for __ in range(N)]
answer = (-1, -1)
x, y = 0, 0
direction = 2 # 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
for i in range(N ** 2, 0, -1):
    if i == target:
        answer = (y + 1, x + 1)
    grid[y][x] = i

    if direction == 0:
        if y - 1 >= 0  and grid[y - 1][x] == 0:
            y -= 1
        else: # 방향 전환
            direction = 3
            x -= 1
    elif direction == 1:
        if x + 1 < N and grid[y][x + 1] == 0:
            x += 1
        else: # 방향 전환
            direction = 0
            y -= 1
    elif direction == 2:
        if y + 1 < N and grid[y + 1][x] == 0:
            y += 1
        else: # 방향 전환
            direction = 1
            x += 1
    else: # direciton == 3:
        if x - 1 >= 0 and grid[y][x - 1] == 0:
            x -= 1
        else: # 방향 전환
            direction = 2
            y += 1

    
for i in range(N):
    for j in range(N):
        print(grid[i][j], end=" ")
    print()
print(answer[0], answer[1])
