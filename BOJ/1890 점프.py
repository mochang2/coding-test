"""
20220423
실버2 점프
url: https://www.acmicpc.net/problem/1890
후기: 처음에는 단순 bfs로 풀려고 했다. 지날 수 있는 모든 경로를 구하고 해당 경로를 지날 때마다 queue에 넣고,
그 경로의 마지막에 목적지에 도달하면 answer += 1 하려고 했었다.
그런데 https://blog.naver.com/wusonjae/221450459264 에 따르면 100 by 100이 전부 입력값이 1이라면 1억이 훨씬 넘는 수가 answer이 된다(심지어 문제에서 2^63 - 1까지가 답이라고 함)

따라서 다른 방법을 생각했다. 일반적으로 '격자 구조의 최단 경로의 수'에서 생각하는 방법이었다.
0행, 0열 중 갈 수 있는 길을 전부 1로 초기화한 뒤, (1,1)~(N-1,N-1) 각각의 격자에 대해 갈 수 있는 경로의 합을 저장해둔 뒤
마지막에 dp[N - 1][N - 1]을 출력하면 될 것이라고 생각했다.

다른 사람들의 풀이를 보니까 dfs로 memoization을 사용했다. 정답이 아니라 질문이긴 하지만 대충 https://www.acmicpc.net/board/view/49256 느낌이다.
"""

# 격자 구조의 최단 경로의 수를 구할 때의 방법대로 구현
import sys
input_ = sys.stdin.readline

# initialization
N = int(input_().strip())
board = []
for _ in range(N):
    board.append(tuple(map(int, input_().strip().split())))
dp = [[0 for _ in range(N)] for __ in range(N)]
i, j = board[0][0], board[0][0]

# 0행 또는 0열 중 밟을 수 있는 경로를 1로 초기화
while i <= N - 1:
    dp[i][0] = 1
    if board[i][0] == 0: # 이 조건문이 없어서 시간 초과가 났음1
        break
    i += board[i][0]

while j <= N - 1:
    dp[0][j] = 1
    if board[0][j] == 0: # 이 조건문이 없어서 시간 초과가 났음2
        break
    j += board[0][j]

# (1,1) ~ (N - 1, N - 1) 발판까지 밟힐 수 있는 횟수를 계산
for i in range(1, N):
    for j in range(1, N):
        y, x = i - 1, j - 1
        while y >= 0:
            if y + board[y][j] == i:
                dp[i][j] += dp[y][j]
            y -= 1
        while x >= 0:
            if x + board[i][x] == j:
                dp[i][j] += dp[i][x]
            x -= 1
print(dp[N - 1][N - 1])
