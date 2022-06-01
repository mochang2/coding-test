"""
20220601
골드5 토마토
url: https://www.acmicpc.net/problem/7576
후기: 전형적인 bfs이다.
다만 deepcopy가 필요했던 이유는 몇 번째 단계에(answer += 1) 해당 위치에 존재하는 토마토가 익었는지 파악하기 위함이다.
오랜만에 기분 좋게 시도 한 번만에 통과했다.
"""

from collections import deque
from copy import deepcopy
import sys
input_ = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def Check(): # 모든 토마토가 익을 수 있는지 확인(0이 존재하는지 확인)
    global M, N, box # global 없어도 됨
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return False
    return True

def Bfs(ripen_tomatos):
    global M, N, box, answer # M, N은 global 없어도 됨

    to_be_ripen = []
    while True:
        while len(ripen_tomatos) != 0:
            y, x = ripen_tomatos.popleft()
            for direct in range(4):
                new_y, new_x = y + dy[direct], x + dx[direct]
                if not 0 <= new_y < N or not 0 <= new_x < M: # out of range
                    continue
                if box[new_y][new_x] != 0: # 이미 bfs를 지남
                    continue

                box[new_y][new_x] = 1
                to_be_ripen.append((new_y, new_x))

        if len(to_be_ripen) == 0:
            break
        answer += 1
        ripen_tomatos = deque(deepcopy(to_be_ripen))
        to_be_ripen.clear()

# initialization
answer = 0
M, N = map(int, input_().strip().split())
box = []
for _ in range(N):
    box.append(list(map(int, input_().strip().split())))
ripen_tomatos = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripen_tomatos.append((i, j))

# bfs
Bfs(deque(ripen_tomatos))

# answer
if Check():
    print(answer)
else:
    print(-1)
