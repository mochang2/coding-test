"""
골드1 마법사 상어와 복제
url: https://www.acmicpc.net/problem/23290
후기: 이번에도 빡구현이다.
물고기는 갈 방향이 없으면 시계 반대 방향으로 돌면서 찾기 때문에 방향에 대한 숫자 재설정 필요했다.
dead_fish_cnt = 0으로 초기화해 줄 때, 만약 상어가 아무리 움직여도 물고기의 냄새가 나타날 수 없으면 오동작한다.
따라서 -1로 초기화해야 한다.

"""

import sys
from copy import deepcopy

# ↑ ↖ ← ↙ ↓ ↘ → ↗
# 0  1  2  3   4 5  6  7
# 질문. axis_li.pop()을 왜 해줘야 되는지.

""" 디버깅
def PrintBowl():
    global fish_bowl
    for i in range(4):
        for j in range(4):
            print(fish_bowl[i][j])
        print()
    print()
"""

def InitInput(string):
    return int(string) - 1

def CountFish(y, x):
    global fish_bowl
    return sum(fish_bowl[y][x].values())

def MoveFish():
    global fish_bowl, new_fish_smells, dy, dx
    result = [[dict({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}) for _ in range(4)] for __ in range(4)]
    for y in range(4):
        for x in range(4):
            for d in range(8): # fish_bowl의 dict.keys()
                flag = False
                for index in range(8):
                    direction = (d + index) % 8
                    new_y = y + dy[direction]
                    new_x = x + dx[direction]
                    if not 0 <= new_y < 4 or not 0 <= new_x < 4 or (new_y, new_x) in new_fish_smells \
                       or (new_y, new_x) in old_fish_smells or (new_y, new_x) == (Sy, Sx):
                        continue # 어항을 벗어나거나 물고기 냄새가 있는 위치거나 상어 위치면
                    result[new_y][new_x][direction] += fish_bowl[y][x][d]

                    flag = True
                    break
                if not flag:
                    result[y][x][d] += fish_bowl[y][x][d]

    return result

def MoveShark(depth, y, x, axis_li = []):
    global new_fish_smells, dead_fish_cnt, Sx, Sy
    if not 0 <= y < 4 or not 0 <= x < 4:
        return

    if depth != 0:
        axis_li.append((y, x))
    if depth == 3:
        cnt = 0
        for yy, xx in set(axis_li): # 겹치게 셀 수 있으므로 set 사용
            cnt += CountFish(yy, xx)
        if dead_fish_cnt < cnt:
            new_fish_smells = list(filter(lambda axis: CountFish(axis[0], axis[1]) > 0, axis_li))
            Sy, Sx = y, x
            dead_fish_cnt = cnt
        axis_li.pop()
        return

    MoveShark(depth + 1, y - 1, x, axis_li) # ↑
    MoveShark(depth + 1, y, x - 1, axis_li) # ←
    MoveShark(depth + 1, y + 1, x, axis_li) # ↓
    MoveShark(depth + 1, y, x + 1, axis_li) # →
    if len(axis_li) != 0:
        axis_li.pop()

input_ = sys.stdin.readline

# initialization
fish_bowl = [[dict({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}) for _ in range(4)] for __ in range(4)]
new_fish_smells = []
old_fish_smells = []
num_fish = 0
dead_fish_cnt = -1
dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, -1, -1, -1, 0, 1, 1, 1)
M, S = map(int, input_().strip().split())
for i in range(M):
    Fy, Fx, d = map(InitInput, input_().strip().split())
    if d == 0:
        fish_bowl[Fy][Fx][2] += 1
    elif d == 1:
        fish_bowl[Fy][Fx][1] += 1
    elif d == 2:
        fish_bowl[Fy][Fx][0] += 1
    elif d == 3:
        fish_bowl[Fy][Fx][7] += 1
    elif d == 4:
        fish_bowl[Fy][Fx][6] += 1
    elif d == 5:
        fish_bowl[Fy][Fx][5] += 1
    elif d == 6:
        fish_bowl[Fy][Fx][4] += 1
    elif d == 7:
        fish_bowl[Fy][Fx][3] += 1
Sy, Sx = map(InitInput, input_().strip().split())

while S > 0:
    # 1. 복제 마법 시전
    copyed_bowl = deepcopy(fish_bowl)
    origin_fish_cnt = 0
    for y in range(4):
        for x in range(4):
            origin_fish_cnt += CountFish(y, x)
    num_fish = origin_fish_cnt
    
    # 2. 물고기가 한 칸씩 이동
    fish_bowl = MoveFish()

    # 3. 상어 3칸 이동(new_fish_smells update)
    old_fish_smells = deepcopy(new_fish_smells)
    MoveShark(0, Sy, Sx)
    for y, x in new_fish_smells:
        for d in range(8):
            fish_bowl[y][x][d] = 0
    dead_fish_cnt = -1

    # 4. 두 번 전 연습에서 생긴 물고기의 냄새가 사라짐
    
    # 5. 복제 마법 완료
    for y in range(4):
        for x in range(4):
            num_fish += CountFish(y, x)
            for d in range(8):
                fish_bowl[y][x][d] += copyed_bowl[y][x][d]

    # 6. 마법 1회 사용
    S-=1

print(num_fish)
