"""
220227
골드4 치즈
url: https://www.acmicpc.net/problem/2638
후기: 빡구현. checkInnerAir(bfs + inner air 구분하기)에 대해 생각하는 부분이 힘들었다.
matrix에 처음에 0,1,2만 있게끔 진행하려다가 도저히 답이 안 나와서 3을 추가하니까 순식간에 풀렸다.
"""

import sys
from collections import deque

def printMatrix():
    global matrix, N, M
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end=" ")
        print()

def checkInnerAir():
    global matrix, N, M
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 or matrix[i][j] == 2 or matrix[i][j] == 3:  # 내부 공기 아니거나 판단 필요 없음
                continue
            
            # bfs를 하면서 3을 만나면, bfs하면서 지나간 부분은 전부 inner air가 아님
            visited = [[False for _ in range(M)] for __ in range(N)]
            queue = deque([(i, j)])  # bfs용 queue
            temp_store = [(i, j)]       # 지나간 경로 저장
            is_inner = True
            while len(queue) != 0:
                y, x = queue.popleft()
                for direction in range(4):  # 가장자리를 3으로 초기화했기 때문에 new_y, new_x 범위 확인 안 해도 됨
                    new_y = y + dy[direction]
                    new_x = x + dx[direction]
                    if matrix[new_y][new_x] == 3:
                        is_inner = False
                    elif matrix[new_y][new_x] == 0 and visited[new_y][new_x] == False:
                        visited[new_y][new_x] = True
                        queue.append((new_y, new_x))
                        temp_store.append((new_y, new_x))

            if is_inner:
                for pos in temp_store:
                    matrix[pos[0]][pos[1]] = 2
            else:
                for pos in temp_store:
                    matrix[pos[0]][pos[1]] = 3

def isFinished():
    global matrix, N, M
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                return False
    return True

def calcMeltPos():
    global matrix, N, M, dy, dx
    pos = []
    for i in range(N):
        for j in range(M):
            cnt = 0
            if matrix[i][j] == 1:
                for direction in range(4):
                    new_y = i + dy[direction]
                    new_x = j + dx[direction]
                    if matrix[new_y][new_x] == 0 or matrix[new_y][new_x] == 3:
                        cnt += 1
            if cnt >= 2:
                pos.append([i, j])
    return pos

def initInnerAir():
    global matrix, N, M
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                matrix[i][j] = 0
    

## 초기화
# O(N * M) = 500. dfs 등으로 완전탐색 가능한 정도
# 0: 미정인 공기, 1: 치즈, 2: 내부 공기
# 3: 내부 공기가 절대 될 수 없는 공기(한 번 3이 되면 다시 1이나 2가 될 수 없음)
time = 0  # answer
matrix = []
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
N, M = map(int, sys.stdin.readline().strip().split())
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(N):  # 가장자리를 3으로 초기화
    for j in range(M):
        if i == 0 or i == N - 1 or j == 0 or j == M - 1:
            matrix[i][j] = 3

while not isFinished():
    # 1. 내부 공기 표시
    checkInnerAir()

    # 2. 녹을 치즈 위치 표시
    to_be_melted = calcMeltPos()

    # 3. to_be_melted에 있는 위치를 0으로 변경
    for pos in to_be_melted:
        matrix[pos[0]][pos[1]] = 0

    # 4 .내부 공기도 다시 0으로 변경
    initInnerAir()

    # 5. 1시간 경과
    time += 1

# 출력
print(time)
