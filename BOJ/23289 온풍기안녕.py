"""
20220320
골드1 온풍기 안녕
url: https://www.acmicpc.net/problem/23289
후기: 개빡구현이었다. 답이 100이 넘어가면 중단하고 101을 출력하라는 것을 못 봐서 한참 해맸다.
1은 위쪽, 2는 오른쪽, 3은 아래쪽, 4는 왼쪽을 의미한다.
air_heaters = dict({1: [], 2: [], 3: [], 4: []})는 각 방향으로 뿜는 히터의 위치를 담고 있다.
check_points = []는 answer가 1이 증가할 때마다 온도가 넘는지를 확인하면 되는 위치를 담고 있다.
house = [[[0, 0] for _ in range(C)] for __ in range(R)]는 3차원 배열로 가장 안에 있는 배열은 (온도, 벽의 방향의 합)을 담고 있다.
벽의 방향의 합이라는 말은 위는 0b0001, 오른쪽은 0b0010, 아래쪽은 0b0100, 왼쪽은 0b1000의 값을 가지고 있다. 즉, 비트 연산을 씀으로써 막혔는지 아닌지를 확인했다.
"""

import sys
input_ = sys.stdin
# O(R * C) = 400 이므로 입력을 내 입맛대로 바꾸는 것은 성능에 영향 x
# 온풍기가 house 밖을 쏴도, 벽이 house 외곽에 지어져도 에러 없는 것 확인

# 디버깅 함수
"""
def PrintD(num = 2):
    global house, R, C
    if num == 2:
        for i in range(R):
            for j in range(C):
                print(house[i][j], end=" ")
            print()
        print()
    else:
        for i in range(R):
            for j in range(C):
                print(house[i][j][num], end=" ")
            print()
        print()

def PrintC():
    for i in range(R):
        for j in range(C):
            print(changes_to_house[i][j], end=' ')
        print()
    print()
"""

def InitInput(x):
    return int(x) - 1

def SpreadTemperature(start_pos, direction):
    global house, visited, R, C
    result = []
    
    for y, x in start_pos:
        #조건: house를 넘지 않고, 벽에 막히지 않으며, 이미 계산되지 않았어야 함
        if direction == 1 and y - 1 >= 0:
            if x - 1 >= 0 and house[y][x - 1][1] & up == 0 and house[y][x - 1][1] & right == 0 and not visited[y - 1][x - 1]:
                visited[y - 1][x - 1] = True
                result.append((y - 1, x - 1))
            if house[y][x][1] & up == 0 and not visited[y - 1][x]:
                visited[y - 1][x] = True
                result.append((y - 1, x))
            if x + 1 < C and house[y][x + 1][1] & up == 0 and house[y][x + 1][1] & left == 0 and not visited[y - 1][x + 1]:
                visited[y - 1][x + 1] = True
                result.append((y - 1, x + 1))
                
        elif direction == 2 and x + 1 < C:
            if y - 1 >= 0 and house[y - 1][x][1] & right == 0 and house[y - 1][x][1] & down == 0 and not visited[y - 1][x + 1]:
                visited[y - 1][x + 1] = True
                result.append((y - 1, x + 1))
            if house[y][x][1] & right == 0 and not visited[y][x + 1]:
                visited[y][x + 1] = True
                result.append((y, x + 1))
            if y + 1 < R and house[y + 1][x][1] & right == 0 and house[y + 1][x][1] & up == 0 and not visited[y + 1][x + 1]:
                visited[y + 1][x + 1] = True
                result.append((y + 1, x + 1))
                
        elif direction == 3 and y + 1 < R:
            if x - 1 >= 0 and house[y][x - 1][1] & right == 0 and house[y][x - 1][1] & down == 0 and not visited[y + 1][x - 1]:
                visited[y + 1][x - 1] = True
                result.append((y + 1, x - 1))
            if house[y][x][1] & down == 0 and not visited[y + 1][x]:
                visited[y + 1][x] = True
                result.append((y + 1, x))
            if x + 1 < C and house[y][x + 1][1] & left == 0 and house[y][x + 1][1] & down == 0 and not visited[y + 1][x + 1]:
                visited[y + 1][x + 1] = True
                result.append((y + 1, x + 1))
        
        elif direction == 4 and x - 1 >= 0:
            if y - 1 >= 0 and house[y - 1][x][1] & left == 0 and house[y - 1][x][1] & down == 0 and not visited[y - 1][x - 1]:
                visited[y - 1][x - 1] = True
                result.append((y - 1, x - 1))
            if house[y][x][1] & left == 0 and not visited[y][x - 1]:
                visited[y][x - 1] = True
                result.append((y, x - 1))
            if y + 1 < R and house[y + 1][x][1] & left == 0 and house[y + 1][x][1] & up == 0 and not visited[y + 1][x - 1]:
                visited[y + 1][x - 1] = True
                result.append((y + 1, x - 1))
        
    return result

def InitVisited():
    global visited, R, C
    for i in range(R):
        for j in range(C):
            if visited[i][j]:
                visited[i][j] = False

def CalcChange():
    global house, R, C, dy, dx
    result = [[0 for _ in range(C)] for __ in range(R)]
    
    for y in range(R):
        for x in range(C):
            curr_temperature = house[y][x][0]
            for i in range(2):
                new_y, new_x = y + dy[i], x + dx[i]
                if not new_y < R or not new_x < C:
                    continue
                if i == 0 and house[y][x][1] & right != 0: # 벽에 막힘1
                    continue
                if i == 1 and house[y][x][1] & down != 0: # 벽에 막힘2
                    continue

                compared_temperature = house[new_y][new_x][0]
                adjust_amount = abs(curr_temperature - compared_temperature) // 4
                if curr_temperature > compared_temperature:
                    result[y][x] -= adjust_amount
                    result[new_y][new_x] += adjust_amount
                elif curr_temperature < compared_temperature:
                    result[y][x] += adjust_amount
                    result[new_y][new_x] -= adjust_amount

    return result

def AdjustTemperature(changes_to_house):
    global house, R, C
    for i in range(R):
        for j in range(C):
            house[i][j][0] = max(0, house[i][j][0] + changes_to_house[i][j])

def IsFinished():
    global check_points, house, K
    for y, x in check_points:
        if house[y][x][0] < K:
            return False
    return True


# 입력과 상관 없는 변수들
## direction 1: 위, 2: 오른, 3: 아래, 4: 왼
up, right, down, left = 0b0001, 0b0010, 0b0100, 0b1000
dy = [0, 1] # (0, 0)부터 (R - 1, C - 1)까지 본인의 오른쪽 / 아래와 비교하면 됨.
dx = [1, 0]

# 초기화
answer = 0
R, C, K = map(int, input_.readline().strip().split()) # 입력1
air_heaters = dict({1: [], 2: [], 3: [], 4: []})
check_points = []
tmp_matrix = []
for _ in range(R): # 입력2
    tmp_matrix.append(list(map(int, input_.readline().strip().split())))
house = [[[0, 0] for _ in range(C)] for __ in range(R)] # (온도, 벽의 방향의 합). 0이면 벽 존재 x 
W = int(input_.readline().strip()) #입력3
for _ in range(W): # 입력4
    y, x, t = map(InitInput, input_.readline().strip().split())
    if t == -1 and y - 1 >= 0: # y, x는 위쪽으로 벽이. y - 1, x는 아래쪽으로 벽이 있는 것.
        house[y][x][1] += up
        house[y - 1][x][1] += down
    elif t == 0 and x + 1 < C: # t == 0 # y, x는 오른쪽으로 벽이. y, x + 1은 왼쪽으로 벽이 있는 것.
        house[y][x][1] += right
        house[y][x + 1][1] += left
        
for i in range(R):
    for j in range(C): # 히터로 인해 5가 되는 위치를 넣음
        if tmp_matrix[i][j] == 1 and j + 1 < C and house[i][j][1] & right == 0: # house를 넘거나, 히터가 벽에 막히면 처음부터 히터 위치를 빼고 계산.
            air_heaters[2].append((i, j + 1))
        elif tmp_matrix[i][j] == 2 and j - 1 >= 0 and house[i][j][1] & left == 0:
            air_heaters[4].append((i, j - 1))
        elif tmp_matrix[i][j] == 3 and i - 1 >= 0 and house[i][j][1] & up == 0:
            air_heaters[1].append((i - 1, j))
        elif tmp_matrix[i][j] == 4 and i + 1 < R and house[i][j][1] & down == 0:
            air_heaters[3].append((i + 1, j))
        elif tmp_matrix[i][j] == 5:
            check_points.append((i, j))

answer = 0
while True:
    # 1. 온풍기 바람
    visited = [[False for _ in range(C)] for __ in range(R)]
    for direction, heater_pos_li in air_heaters.items():
        for heater_pos in heater_pos_li:
            start_pos = [heater_pos] # 온풍기 바람이 닿는 위치

            near_point = 5 # 증가할 온도
            while near_point > 0 and start_pos != []:
                for y, x in start_pos:
                    house[y][x][0] += near_point
                start_pos = SpreadTemperature(start_pos, direction)
                near_point -= 1
                
            InitVisited()
    
    # 2. 온도 조절
    changes_to_house = CalcChange()
    AdjustTemperature(changes_to_house)

    # 3. 가장자리 온도 감소
    for i in range(R):
        for j in range(C):
            if i != 0 and j != 0 and i != R - 1 and j != C - 1:
                continue
            house[i][j][0] = max(0, house[i][j][0] - 1)

    # 4. 초콜릿 먹음
    answer += 1
    if answer > 100:
        print(101)
        sys.exit(0)

    # 5. 끝났는지 확인
    if IsFinished():
        break

# 출력
print(answer)
