"""
220303
골드3 앱
url: https://www.acmicpc.net/problem/7579
후기: 답을 확인한 후에 풀 수 있었다(https://velog.io/@uoayop/BOJ-7579-%EC%95%B1Python).
배낭 문제는 봐도봐도 문제가 새롭다... 풀이를 전부 이해한 후에야 작성할 수 있었다.

# 배낭 문제 응용. 배낭 문제에서는
# weight: 최소화, value: 최대화 였다면
# cost: 최소화, memory: M 이상이고,
# N * M 최대 10억이므로 cost가 행 또는 열에 가는 것이 맞음. 나머지 열 또는 행은 N(앱의 종류)이다.
# total cost <= 10000이므로 time complexity가 O(1,000,000) 안에 가능.
"""

import sys

N, M = map(int, sys.stdin.readline().strip().split())
if M == 0:
    print(0)
memories = list(map(int, sys.stdin.readline().strip().split()))
costs = list(map(int, sys.stdin.readline().strip().split()))
total_cost = sum(costs)  # <= 10000
answer = total_cost + 1

dp = [[0 for _ in range(total_cost + 1)] for __ in range(N)]

for i in range(N):
    for j in range(total_cost + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= costs[i]:  # 배낭 문제 dp
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i]] + memories[i])

        if dp[i][j] >= M:  # 조건에 부합하는지 확인한 후 최소 비용을 선택
            answer = min(answer, j)
        
print(answer)
