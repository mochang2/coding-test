"""
20220719
골드5 토마토
url: https://www.acmicpc.net/problem/7569
후기: bfs를 이용한 완전탐색인데, 그동안 했던 bfs랑 다른 점은 3차원이라는 것이다.
하지만 기존 방식과 푸는 방법이 크게 다르진 않았다.
z축만 추가한 뒤 기존에 dy, dx로 선언해서 진행 방향을 조정하던 부분이 directions로 한 번에 선언했을 뿐이다.

O(H * N * M) = 1,000,000이니 충분히 완탐이 가능하다.
"""

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않음

import sys
from collections import deque

input_ = sys.stdin.readline

def print3DArray(tomato_storage): # 디버깅용
    global M, N, H
    
    for z in range(H):
        for y in range(N):
            for x in range(M):
                print(tomato_storage[z][y][x], end=" ")
            print()
        print()

def isAllRipen(tomato_storage):
    global M, N, H

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato_storage[z][y][x] == 0: # 안 익은 토마토 존재
                    return False
                
    return True

def getRipenTomatos(tomato_storage):
    global M, N, H

    result = deque([])

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato_storage[z][y][x] == 1: # 입력값에서부터 익은 토마토
                    result.append((z, y, x))

    return result

# initialization
answer = -1 # 토마토가 다 익운 뒤에 한 번 더 bfs를 돔
directions = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)) # 토마토 익는게 전염되는 방향
M, N, H = map(int, input_().strip().split())
tomato_storage = []
for _ in range(H):
    matrix = [list(map(int, input_().strip().split())) for __ in range(N)]
    tomato_storage.append(matrix)

# 익은, 익을 토마토의 좌표 저장
ripen_tomatos = getRipenTomatos(tomato_storage)

# bfs
while ripen_tomatos:
    new_ripen_tomatos = deque([])
    
    while ripen_tomatos:
        z, y, x = ripen_tomatos.popleft()

        for dz, dy, dx in directions:
            new_z, new_y, new_x = z + dz, y + dy, x + dx

            if not 0 <= new_z < H or not 0 <= new_y < N or not 0 <= new_x < M: # 범위를 벗어남
                continue
            if tomato_storage[new_z][new_y][new_x] != 0: # 익을 토마토가 없음
                continue

            tomato_storage[new_z][new_y][new_x] = 1 # 토마토가 익음
            new_ripen_tomatos.append((new_z, new_y, new_x))
            
    ripen_tomatos = new_ripen_tomatos
    answer += 1

# print
if isAllRipen(tomato_storage):
    print(answer)
else:
    print(-1)
