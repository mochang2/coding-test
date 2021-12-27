"""
211227
골드4 내리막 길
url: https://www.acmicpc.net/problem/1520
후기: 
"""

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
    # 이거를 return 안 해서 고생함. 호출한 애는 return 값을 받아야 정상적으로 dfs + dp 값을 받음.
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
