"""
20220608
골드4 벽 부수고 이동하기
url: https://www.acmicpc.net/problem/2206
후기: bfs를 이용한 완탐문제였다.
처음에는 answer과 new_queue를 선언하고 bfs 돌 때마다 새롭게 도착한 지점을 다시 queue로 사용해었다.
이 방법은 시간초과나 메모리초과가 났다.
해결방법은 visited를 3차원 배열로 선언하고 queue에 move(이동한 횟수)도 같이 저장하는 것이었다.
"""

## O(N * M) = 1,000,000
## 오답(시간초과)
from copy import deepcopy
from collections import deque
import sys
input_ = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

# initialization
N, M = map(int, input_().strip().split())
matrix = [input_().strip() for _ in range(N)]
visited = [[[False, False] for _ in range(M)] for __ in range(N)] # visited, 벽을 부숴야지만 도달할 수 있는지 여부
visited[0][0][0] = True
queue = deque([(0, 0, False)]) # y, x, if breaked
answer = 0
reached = False

# bfs
while queue and not reached:
    new_queue = deque([])
    while queue: # O(N * M)
        y, x, breaked = queue.popleft()
        if (y, x) == (N - 1, M - 1):
            reached = True
            break

        for direct in range(4): # O(4)
            new_y, new_x = y + dy[direct], x + dx[direct]
            if not 0 <= new_y < N or not 0 <= new_x < M: # out of range
                continue
            if visited[new_y][new_x][0] and breaked: # already visited
                # 방문되었지만 break 하지 않고 도달할 수 있을 경우는 continue하지 않음
                continue
            if matrix[new_y][new_x] == '1' and breaked: # already breaked the wall
                continue

            visited[new_y][new_x][0] = True
            if matrix[new_y][new_x] == '1':
                new_queue.append((new_y, new_x, True))
            else:
                new_queue.append((new_y, new_x, breaked))

    queue = deepcopy(new_queue)
    answer += 1

if reached:
    print(answer)
else:
    print(-1)

    
    
## O(N * M) = 1,000,000
## 정답
from collections import deque
import sys
input_ = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

# initialization
N, M = map(int, input_().strip().split())
matrix = [input_().strip() for _ in range(N)]
visited = [[[False, True] for _ in range(M)] for __ in range(N)] # visited, 벽을 부숴야지만 도달할 수 있는지 여부
visited[0][0][0] = True
queue = deque([(0, 0, False, 1)]) # y, x, if breaked, move
reached = False

# bfs
while queue: # O(N * M)
    y, x, breaked, move = queue.popleft()
    if (y, x) == (N - 1, M - 1):
        reached = True
        answer = move
        break

    for direct in range(4): # O(4)
        new_y, new_x = y + dy[direct], x + dx[direct]
        if not 0 <= new_y < N or not 0 <= new_x < M: # out of range
            continue
        if matrix[new_y][new_x] == '1' and breaked: # already breaked the wall
            continue
        if not visited[new_y][new_x][1] or (visited[new_y][new_x][0] and breaked):
            # 벽을 부수지 않고 도달할 수 있는 경우가 이미 존재 or already visited + already breaked
            continue

        visited[new_y][new_x][0] = True
        if matrix[new_y][new_x] == '1':
            queue.append((new_y, new_x, True, move + 1))
        else:
            visited[new_y][new_x][1] = breaked
            queue.append((new_y, new_x, breaked, move + 1))

if reached:
    print(answer)
else:
    print(-1)

    
    
## 다른 사람 풀이(나보다 3000ms 정도 빠름)
## 풀이 로직 자체는 같은데 조건문을 더 효율적으로 짠 것 같음
import sys
from collections import deque
input = sys.stdin.readline
x_points = [1, 0, -1, 0]
y_points = [0, 1, 0, -1]

def is_vaild_coord(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs(y, x):
    count = 1
    dq = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited_through_breaking_wall = [[False for _ in range(m)] for _ in range(n)]
    dq.append((y, x, count, False))
    visited[y][x] = True
    
    while dq:
        y, x, count, did_break_wall = dq.popleft()
        if y == n - 1 and x == m - 1:
            return count

        for i in range(4):
            nx = x + x_points[i]
            ny = y + y_points[i]

            if is_vaild_coord(ny, nx):
                if not visited[ny][nx]:  # 방문 안한 경우
                    if board[ny][nx] == "0":  # 그냥 지나갈 수 있는 경우
                        visited[ny][nx] = True
                        dq.append((ny, nx, count + 1, did_break_wall))
                        visited_through_breaking_wall[ny][nx] = did_break_wall

                    elif board[ny][nx] == "1" and not did_break_wall:   # 벽이 있는데 부술 수 있는 경우
                        visited[ny][nx] = True
                        dq.append((ny, nx, count + 1, True))
                        visited_through_breaking_wall[ny][nx] = did_break_wall

                elif board[ny][nx] == "0" and visited_through_breaking_wall[ny][nx] and not did_break_wall:  # 벽을 부수면서 방문했는데 지금은 벽은 안부신 경우
                    visited[ny][nx] = True 
                    dq.append((ny, nx, count + 1, False))
                    visited_through_breaking_wall[ny][nx] = did_break_wall

    return -1
        

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input().strip())

min = bfs(0, 0)
print(min)
