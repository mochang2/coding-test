"""
20220410
골드3 주사위 굴리기 2
url: https://www.acmicpc.net/problem/23288
후기: 빡구현이었다. 기존에 풀던 빡구현에 비하면 쉬운 편이었다. N, M, K 값이 작아서 시간 초과는 고려하지 않았었다.
addScore, changeDirection은 너무 쉬웠으나 moveDice가 약간 고민이었다.
dice를 처음에는 dictionary로 선언하고 각각의 번호에 대해 상하좌우 숫자를 고정시켜두려고 했으나, 주사위가 돌아가는 방향에 따라
각각의 번호에 대해 상하좌우 숫자가 바뀌었으므로 이차원 배열을 선언해 매 판마다 주사위를 가변적으로 바꿔주었다.
"""

import sys
from collections import deque
input_ = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
# 각 숫자가 바닥에 있을 때 본인의 상하좌우에 어떤 숫자가 있는지를 저장하기 위한 변수
# 처음 주사위 상태에 따라 초기화함
dice = [
    [-1, 2, -1],
    [4, 6, 3],
    [-1, 5, -1]
]

def moveDice():
    global direct, curr_y, curr_x, dice
    # 위치 설정
    new_y, new_x = curr_y + dy[direct], curr_x + dx[direct]
    if not 0 <= new_y < N or not 0 <= new_x < M:
        direct = (direct + 2) % 4
        new_y, new_x = curr_y + dy[direct], curr_x + dx[direct]
    curr_y, curr_x = new_y, new_x

    # 바닥을 마주한 주사위 설정
    # direct: 0 -> dice 1열 아래로 1칸씩 이동
    # direct: 1 -> dice 1행 오른쪽으로 1칸씩 이동
    # direct: 2 -> dice 1열 위로 1칸씩 이동
    # direct: 3 -> dice 1행 왼쪽으로 1칸씩 이동
    current_top = 7 - dice[1][1] # dice변수에 새로 추가될 수
    if direct == 0:
        for i in range(2, 0, -1):
            dice[i][1] = dice[i - 1][1]
        dice[0][1] = current_top
    elif direct == 1:
        for i in range(2):
            dice[1][i] = dice[1][i + 1]
        dice[1][2] = current_top
    elif direct == 2:
        for i in range(2):
            dice[i][1] = dice[i + 1][1]
        dice[2][1] = current_top
    else: #direct == 0:
        for i in range(2, 0, -1):
            dice[1][i] = dice[1][i - 1]
        dice[1][0] = current_top

def addScore(i, j):
    # bfs
    global answer
    visited = [[False for _ in range(M)] for __ in range(N)]
    visited[i][j] = True
    queue = deque([(i, j)])
    num = matrix[i][j]
    count = 1

    while len(queue) != 0:
        y, x = queue.popleft()
        for direct in range(4):
            new_y, new_x = y + dy[direct], x + dx[direct]
            if not 0 <= new_y < N or not 0 <= new_x < M:
                continue

            if not visited[new_y][new_x] and matrix[new_y][new_x] == num:
                visited[new_y][new_x] = True
                count += 1
                queue.append((new_y, new_x))

    answer += count * num    

def changeDirection(dice_num, matrix_num):
    global direct
    if dice_num > matrix_num:
        direct = (direct + 1) % 4
    elif dice_num < matrix_num:
        direct = (direct - 1) % 4    

# initialization
answer = 0
N, M , K = map(int, input_().strip().split())
matrix = [] # 지도
direct = 1 # 초기 방향: 우
curr_y, curr_x = 0, 0 # 주사위 초기 위치
for _ in range(N):
    matrix.append(tuple(map(int, input_().strip().split())))

for _ in range(K):
    # 1. 주사위가 이동 방향으로 한 칸 굴러간다.
    moveDice()

    # 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    addScore(curr_y, curr_x)

    # 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    changeDirection(dice[1][1], matrix[curr_y][curr_x])
    
print(answer)
