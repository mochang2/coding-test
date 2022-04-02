"""
20220402
골드1 마법사 상어와 블리자드
url: https://www.acmicpc.net/problem/21611
후기: 딱 2시간 정도 걸린 빡구현 문제였다.
생각보다 짧게 걸린 이유는 접근 방법이 좋았던 것 같다.
모든 과정에서 공통적으로 필요한 것이기 때문에 중앙의 상어 위치부터 (0, 0) [문제에서는 (1, 1)이라고 설명]까지의 routes 즉, 좌표들의 list를 갖고 있어야 한다고 판단했다.
이를 InitRoutes()로 만들어서 전역변수로서 거의 모든 함수에서 사용했다.
또한 O(N^2) = 2401 이므로 모든 위치를 순회해도, matrix를 몇 개 더 만들어도 크게 효율성에 문제 있는 정도는 아니라고 생각했다.
"""
# 0: 구슬 없음, 1~3: 구슬 종류.

import sys
input_ = sys.stdin.readline
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def InitRoutes():
    global N, Saxis
    axis_li = []
    dy = (-1, 0, 1, 0)    # direction: 0: ↑, 1: →, 2: ↓, 3: ←
    dx = (0, 1, 0, -1)
    direct = 0
    current_y, current_x = Saxis, Saxis
    
    for distance in range(1, N): # 한 방향으로 이동할 거리,
        for _ in range(2): # 해당 거리 만큼 두 방향으로 이동. 좌 -> 하 -> 우 -> 상 순서.
            direct = (direct - 1) % 4
            movement = 0
            while movement != distance:
                current_y, current_x = current_y + dy[direct], current_x + dx[direct]
                axis_li.append((current_y, current_x))
                movement += 1
    for x in range(N - 2, -1, -1): # 마지막에 왼쪽 방향으로 N - 1개
        direct = 3
        current_y, current_x = current_y + dy[direct], current_x + dx[direct]
        axis_li.append((current_y, current_x))
            
    return axis_li

def PullBeads():
    global matrix, routes, N
    beads = []

    for y, x in routes:
        if matrix[y][x] != 0:
            beads.append(matrix[y][x])
    beads.extend([0 for _ in range((N ** 2 - 1) - len(beads))])

    for index, bead in enumerate(beads):
        y, x = routes[index][0], routes[index][1]
        matrix[y][x] = bead

def Explode():
    global N, answer
    while True:
        flag = False  # 구슬 폭발이 이루어졌는지 여부

        to_be_deleted = []
        index = 0
        routes_len = N ** 2 - 1
        while index < routes_len - 1:
            group = [] # 같은 구슬이 연속되어 있으면 그룹
            curr_bead = matrix[routes[index][0]][routes[index][1]]
            next_bead = matrix[routes[index + 1][0]][routes[index + 1][1]]
            if curr_bead == next_bead and curr_bead != 0:
                group.append(index)
                index += 1
                while curr_bead == matrix[routes[index][0]][routes[index][1]]:
                    group.append(index)
                    index += 1
                index -= 1
            index += 1
            if len(group) >= 4: # 그룹의 길이가 4이상이라면
                flag = True
                to_be_deleted.append(group)
                answer += len(group) * curr_bead

        for group in to_be_deleted:
            for index in group:
                y, x = routes[index][0], routes[index][1]
                matrix[y][x] = 0
                
        PullBeads()
        if not flag:
            break

def ChangeBeads():
    global N, answer
    beads = []

    index = 0
    routes_len = N ** 2 - 1
    while index < routes_len - 1:
        group = [] # 같은 구슬이 연속되어 있으면 그룹
        curr_bead = matrix[routes[index][0]][routes[index][1]]
        next_bead = matrix[routes[index + 1][0]][routes[index + 1][1]]
        if curr_bead == 0:
            index += 1
            continue

        group.append(index)
        if curr_bead == next_bead:
            index += 1
            while curr_bead == matrix[routes[index][0]][routes[index][1]]:
                group.append(index)
                index += 1
            index -= 1
        beads.append(len(group))
        beads.append(curr_bead)
        index += 1

    return beads

def MakeNewMatrix(beads):
    global matrix, N, routes

    max_len = N ** 2 - 2
    for index, bead in enumerate(beads):
        if index > max_len:
            return
        y, x = routes[index][0], routes[index][1]
        matrix[y][x] = bead
    

# initialization
answer = 0
N, M = map(int, input_().strip().split())
Saxis = (N - 1) // 2 # 상어 위치
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input_().strip().split())))
blizards = []
for _ in range(M):
    blizards.append(tuple(map(int, input_().strip().split())))
routes = InitRoutes() # 상어위치부터 (0, 0)까지 가는 길의 좌표

for d, s in blizards:
    # 1. 블라자드 마법 시전
    while s > 0:
        new_y, new_x = Saxis + dy[d - 1] * s, Saxis + dx[d - 1] * s
        matrix[new_y][new_x] = 0 # s 입력 범위 때문에 new_y, new_x가 N을 넘어가는지 검사 안 해도 됨
        s -= 1
    PullBeads()

    # 2. 구슬 폭발
    Explode()

    # 3. 구슬 변화
    beads = ChangeBeads()
    MakeNewMatrix(beads)

print(answer)
