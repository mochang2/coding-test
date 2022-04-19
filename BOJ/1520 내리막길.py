"""
211227
골드4 내리막 길
url: https://www.acmicpc.net/problem/1520
후기: dfs + dp문제였다. 처음에는 시간을 단축하기 위해 이상한 논리로 접근하다가 틀렸고,
두 번째는 정석적인 dfs를 돌리다가 시간초과가 났다. dfs + dp라는 힌트도 들었지만, 결국 답을 봐서 풀 수 있었다.
"""

# 첫 번째 시도
# 논리가 틀림
import sys
from collections import deque

def up(i, j):
    global queue, visited
    if grid[i][j] > grid[i - 1][j]:
        if not visited[i - 1][j]:
            queue.append([i - 1, j])
            visited[i - 1][j] = True
        return True
    return False

def down(i, j):
    global queue, visited
    if grid[i][j] > grid[i + 1][j]:
        if not visited[i + 1][j]:
            queue.append([i + 1, j])
            visited[i + 1][j] = True
        return True
    return False

def left(i, j):
    global queue, visited
    if grid[i][j] > grid[i][j - 1]:
        if not visited[i][j - 1]:
            queue.append([i, j - 1])
            visited[i][j - 1] = True
        return True
    return False

def right(i, j):
    global queue, visited
    if grid[i][j] > grid[i][j + 1]:
        if not visited[i][j + 1]:
            queue.append([i, j + 1])
            visited[i][j + 1] = True
        return True
    return False

def check(i, j):
    global M, N
    count = 0
    if i == 0:
        if j == 0:
            if right(i, j):
                count += 1
            if down(i, j):
                count += 1
        elif j == N - 1:
            if left(i, j):
                count += 1
            if down(i, j):
                count += 1
        else:
            if left(i, j):
                count += 1
            if right(i, j):
                count += 1
            if down(i, j):
                count += 1
    elif i == M - 1:
        if j == 0:
            if up(i, j):
                count += 1
            if right(i, j):
                count += 1
        elif j == N - 1:  # 목적지점이므로 알 필요가 없음.
            pass
        else:
            if left(i, j):
                count += 1
            if right(i, j):
                count += 1
            if up(i, j):
                count += 1
    else:
        if j == 0:
            if up(i, j):
                count += 1
            if right(i, j):
                count += 1
            if down(i, j):
                count += 1
        elif j == N - 1:
            if up(i, j):
                count += 1
            if left(i, j):
                count += 1
            if down(i, j):
                count += 1
        else:
            if up(i, j):
                count += 1
            if down(i, j):
                count += 1
            if right(i, j):
                count += 1
            if left(i, j):
                count += 1
    return count

M, N = map(int, sys.stdin.readline().strip().split())
grid = []
for i in range(M):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))
result = [[0 for _ in range(N)] for __ in range(M)]
visited = [[False for _ in range(N)] for __ in range(M)]

# 시작지점: 0,0 목표지점: M-1, N-1
queue = deque([[0, 0]])
visited[0][0] = True
while len(queue) != 0:
    first = queue.popleft()
    if first == [M - 1, N - 1]:
        continue
    result[first[0]][first[1]] = check(first[0], first[1]) # check(y axis, x axis)

answer = 0
for i in range(M):
    for j in range(N):
        r = result[i][j]
        if r != 1 and r != 0:
            answer += (r - 1)
            
print(answer + 1 if answer != 0 else 0)


# 두 번째 시도
# 단순 dfs로 풀면? => 시간 초과
import sys

def dfs(i, j):
    global M, N, grid, count
    
    if (i, j) == (M - 1, N - 1):
        count += 1
        return

    for direction in range(4):
        # grid를 넘어가면 continue
        if (i == 0 and direction == 0) or (i == M - 1 and direction == 2) or \
        (j == 0 and direction == 3) or (j == N - 1 and direction == 1) :
            continue
        
        next_y = i + dy[direction]
        next_x = j + dx[direction]
        if grid[i][j] > grid[next_y][next_x]:
            dfs(next_y, next_x)
    
sys.setrecursionlimit(10 ** 8)
M, N = map(int, sys.stdin.readline().strip().split())
grid = []
for i in range(M):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))

# 위, 오른, 아래, 왼
dx = [0, 1, 0 ,-1]
dy = [-1, 0, 1, 0]

# 시작지점: 0,0 목표지점: M-1, N-1
count = 0
dfs(0, 0)
print(count)


# 세 번째 시도. dfs + dp
import sys

def dfs(y, x):
    global dp, dx, dy
    if dp[y][x] != -1:
        return dp[y][x]

    temp = 0
    for direction in range(4):
        new_y, new_x = y + dy[direction], x + dx[direction]
        if 0 <= new_y < M and 0 <= new_x < N and li[y][x] > li[new_y][new_x]:
            temp += dfs(new_y, new_x)
    dp[y][x] = temp
    # return 안 해서 고생함. 호출한 애는 return 값을 받아야 정상적으로 dfs + dp 값을 받음.
    return temp

# 목적지를 제외하고 dp를 처음에 -1로 초기화함.
# dfs를 돌면서 dp를 수정하고, -1이 아닌 값을 마주하면 그 길은 더이상 탐색하지 않음.
# 이를 통해 시간을 단축할 수 있음.
sys.setrecursionlimit(10 ** 8)
M, N = map(int, sys.stdin.readline().strip().split())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for __ in range(M)]
dp[M - 1][N - 1] = 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

dfs(0, 0)
print(dp[0][0])
