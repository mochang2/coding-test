"""
20220330
골드5 마법사 상어와 비바라기
url: https://www.acmicpc.net/problem/21610
후기: 구현은 쉬웠으나 시간 초과가 발생했다.
new_rain_cloud_pos라는 변수를 1차원 배열로 선언하여 rain_cloud_pos에 있는 좌표인지 검사한 후  rain_cloud_pos에 deepcopy로 복사하니 생긴 문제였다.
구름 생성하는 부분에서 len(rain_cloud_pos) == O(N*2) 일 경우 최대 6억 번의 시간 복잡도가 나온다.
rain_cloud_pos에 비구름 위치를 담을 뿐만 아니라 구름 유무를 가진 2차원 배열을 새롭게 선언함으로써 해결했다.
"""

import sys

# 입력과 상관 없는 initialization
dy = (0, -1, -1, -1, 0, 1, 1, 1) # 구름의 이동방향
dx = (-1 ,-1 , 0, 1, 1, 1, 0, -1)
answer = 0

# initiazliation
input_ = sys.stdin.readline
N, M = map(int, input_().strip().split())
rain_cloud_pos = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
rain_cloud = [[False for _ in range(N)] for __ in range(N)]
water_amount = []
for _ in range(N):
    water_amount.append(list(map(int, input_().strip().split())))
movements = []
for _ in range(M):
    movements.append(tuple(map(int, input_().strip().split())))

for d, s in movements:
    # 1. 모든 구름이 d 방향으로 s칸 이동
    for index, pos in enumerate(rain_cloud_pos):
        new_y = (pos[0] + dy[d - 1] * s) % N
        new_x = (pos[1] + dx[d - 1] * s) % N
        rain_cloud_pos[index] = [new_y, new_x]
        rain_cloud[new_y][new_x] = True
        
    # 2. 비가 내려 물의 양 1만큼 증가
    for y, x in rain_cloud_pos:
        water_amount[y][x] += 1
        
    # 4. 물복사 버그. rain_cloud_pos를 사용해야 하므로 순서 변경.
    changes = []
    for y, x in rain_cloud_pos:
        change = 0
        for i in range(1, 9, 2):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if not 0 <= new_y < N or not 0 <= new_x < N:
                continue

            if water_amount[new_y][new_x] != 0:
                change += 1
        changes.append(change)
        
    for index, change in enumerate(changes):
        water_amount[rain_cloud_pos[index][0]][rain_cloud_pos[index][1]] += change

    # 3. 구름 사라짐
    rain_cloud_pos.clear()   

    # 5. 구름 생성
    for i in range(N):
        for j in range(N):
            if rain_cloud[i][j]:
                rain_cloud[i][j] = False
                continue
            
            if water_amount[i][j] >= 2:
                rain_cloud_pos.append([i, j])
                water_amount[i][j] -= 2
                
for i in range(N):
    answer += sum(water_amount[i])
print(answer)
