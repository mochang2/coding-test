"""
골드4 연구소 3
211031
url: https://www.acmicpc.net/problem/17142
후기: 첫 접근은 좋았다. 아래 #로 주석한 부분이 그랬다.
하지만 반례 하나 때문에 정말 오래걸렸다. 바이러스를 퍼뜨리는데 *(78번째 줄에 설명)로 막혀있을 수도 있었는데, 이를 간과했다.
마지막에 퍼진 위치가 *로만 이루어져 있었는지, 0도 포함되어 있었는지를 구분하여 ans를 출력해야했다.
반례:
9 1
0 2 2 2 2 2 2 2 0
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1

# 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수라는 조건 + BFS: O(N^4), N <= 50
# time complexity: O(50^4 * 10C5) => python 1.5초 이내로 브루트포스 가능하다는 결론.
## 끝나지 않을 조건
# 1. 특정 빈칸에서 BFS 또는 DFS를 할 때 2를 만나지 못 함.
# 2. 벽에 의해  분리된 공간의 수 > M
## => 모두 그냥 time이 2500을 넘어가면 break 시켜버림.
"""

import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

def PrintMatrix():
    global matrix, N
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()
    print()

def InitVirus(pos):
    global matrix
    for p in pos:
        matrix[p[0]][p[1]] = 2

def SpreadVirus(old_pos):
    global matrix
    new_pos = []
    for pos in old_pos:
        for direction in range(4):
            new_y = pos[0] + dy[direction]
            new_x = pos[1] + dx[direction]
            if not 0 <= new_y < N or not 0 <= new_x < N:
                continue
            if matrix[new_y][new_x] == 0: 
                matrix[new_y][new_x] = 2
                new_pos.append((new_y, new_x))
            elif matrix[new_y][new_x] == "*":
                new_pos.append((new_y, new_x))
    
    return new_pos

def CheckIfOnlyStar(pos):
    global matrix
    for p in pos:
        if matrix[p[0]][p[1]] == 2:
            return False
    return True
    
def IsFinished():
    global matrix, N
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                return False
    return True

# 0: 빈칸, 1: 벽, *: 바이러스가 가능한 위치, 2: 바이러스 존재
# 초기화
N, M = map(int, sys.stdin.readline().strip().split())
matrix = []
candidates = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = N ** 2 + 1
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            candidates.append((i, j))
            matrix[i][j] = "*"
origin_matrix = deepcopy(matrix)

for virus_pos in combinations(candidates, M):
    InitVirus(virus_pos)  # 바이러스 위치 정함

    # 새로운 바이러스(new_virus_pos)를 기준으로 바이러스가 퍼짐.
    time = 0
    new_virus_pos = virus_pos[:]
    
    while time <= N ** 2:
        new_virus_pos = SpreadVirus(new_virus_pos)
        
        if len(new_virus_pos) == 0:
            break
        elif CheckIfOnlyStar(new_virus_pos) and IsFinished():
            break
        else:
            for pos in new_virus_pos:
                matrix[pos[0]][pos[1]] = 2
                
        time+=1

    if IsFinished():
        ans = min(ans, time)
    matrix = deepcopy(origin_matrix)  # 초기화

# 출력
if ans == N ** 2 + 1:
    print(-1)
    sys.exit(0)
print(ans)
