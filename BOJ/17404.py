"""
골드4 RGB거리 2
url: https://www.acmicpc.net/problem/17404
후기: 각각 가장 최소의 값을 선택하는 그리디 알고리즘인가 싶었는데, 첫 번째에 무엇을 선택하느냐에 따라 값이 달라졌다.
두 번째로 생각한 방향은 dp인데 dp를 3개나 선언할 생각은 하지 않았다(첫 번째에 선택한 것에 따라)
그래서 결국 답을 봐서 해결했다.
"""

import sys

def min_GB(i, dp):
    return min(dp[i - 1][1], dp[i - 1][2])

def min_RB(i, dp):
    return min(dp[i - 1][0], dp[i - 1][2])

def min_RG(i, dp):
    return min(dp[i - 1][0], dp[i - 1][1])

N = int(input())
costs = []
INF = 1000001  # 가장 큰 값이 1000이랬으니까
R_dp = [[0, 0, 0] for _ in range(N)]  # 처음에 R을 선택
G_dp = [[0, 0, 0] for _ in range(N)]  # 처음에 G을 선택
B_dp = [[0, 0, 0] for _ in range(N)]  # 처음에 B을 선택
for i in range(N): # [0]: R, [1]: G, [2]: B
    costs.append(list(map(int, sys.stdin.readline().strip().split())))

# 초기화
R_dp[0] = [costs[0][0], INF, INF]
G_dp[0] = [INF, costs[0][1], INF]
B_dp[0] = [INF, INF, costs[0][2]]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            R_dp[i][j] = min_GB(i, R_dp) + costs[i][j]
        elif j == 1:
            R_dp[i][j] = min_RB(i, R_dp) + costs[i][j]
        else: # j == 2:
            R_dp[i][j] = min_RG(i, R_dp) + costs[i][j]
        
    for j in range(3):
        if j == 0:
            G_dp[i][j] = min_GB(i, G_dp) + costs[i][j]
        elif j == 1:
            G_dp[i][j] = min_RB(i, G_dp) + costs[i][j]
        else: # j == 2:
            G_dp[i][j] = min_RG(i, G_dp) + costs[i][j]
    
    for j in range(3):
        if j == 0:
            B_dp[i][j] = min_GB(i, B_dp) + costs[i][j]
        elif j == 1:
            B_dp[i][j] = min_RB(i, B_dp) + costs[i][j]
        else: # j == 2:
            B_dp[i][j] = min_RG(i, B_dp) + costs[i][j]

print(min(R_dp[-1][1], R_dp[-1][2], G_dp[-1][0], G_dp[-1][2], B_dp[-1][0], B_dp[-1][1]))
