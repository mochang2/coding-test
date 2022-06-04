"""
20220604
실버1 RGB거리
url: https://www.acmicpc.net/problem/1149
후기: 17404의 기본 버전이며 DP 문제이다.
cost의 최솟값을 구하는 기존 DP와 비슷하면서 다른 것이, 시작점이 3개여야 한다는 것이다.
DP는 풀어도 풀어도 답을 보지 않으면 모르겠다...
"""

import sys
input_ = sys.stdin.readline

N = int(input_().strip())
costs = []
answer = 1000001
MAX = 1000001
for _ in range(N):
    costs.append(tuple(map(int, input_().strip().split())))

for color in range(3): # RGB로 각각 start
    dp = [[MAX for _ in range(3)] for __ in range(N)]
    dp[0][color] = costs[0][color] # start color를 제외한 나머지는 MAX cost

    for i in range(1, N):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    answer = min(answer, min(dp[-1]))

print(answer)
