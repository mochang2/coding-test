"""
골드4 색상환
url: https://www.acmicpc.net/problem/2482
후기: 한동안 C# 공부한다고 리트코드의 데이터 구조 문제만 주구장창 풀었어서 DP가 너무 어려웠다.
답을 보고도 한참 생각한 끝에 원리를 이해할 수 있었다. 역시 코테는 감을 잃지 않게 꾸준함이 중요하구나 싶었다.
"""

import sys
N = int(input())
K = int(input())
if K > (N // 2):
    print(0)
    sys.exit(0)

dp = [[0 for _ in range(K + 1)] for __ in range(N + 1)] # dp[i][j] : i개의 색 중 j개의 색을 선택하는 경우의 수
for i in range(1, N + 1):
    # dp 초기화. nC1 = n
    dp[i][1] = i

for i in range(2, N + 1): # dp[1][j] 는 확인하는 의미가 없음. 2부터 시작
    for j in range(2, K + 1): # dp[i][1]은 이미 초기화해줌. 2부터 시작
        if i == N: # i-1번째 색까지 j개를 모두 선택했거나 / i-2번째 색까지 j-1개만 선택해서 i번째 색을 선택하는 경우. 단 1번째 색은 색칠을 못 함.
            dp[i][j] = dp[i - 1][j] + dp[i - 3][j - 1]
        else:  # i-1번째 색까지 j개를 모두 선택했거나 / i-2번째 색까지 j-1개만 선택해서 i번째 색을 선택하는 경우
            dp[i][j] = dp[i - 1][j] + dp[i - 2][j - 1]
        dp[i][j] %= 1000000003
print(dp[N][K])
