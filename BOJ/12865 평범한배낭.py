"""
211112
골드4 평범한 배낭
url: https://www.acmicpc.net/problem/12865
후기: DP가 도저히 이해가 안 되어서 답을 봤다. 블로그, 유튜브, 지인 설명 다 찾아봤지만
https://www.youtube.com/watch?v=uggO0uzGboY
여기가 제일 잘 나와있다.
https://claude-u.tistory.com/208 여기 그래프도 보면 이해가 된다.
"""
import sys

# 입력
N, K = map(int, sys.stdin.readline().split())
li = []
for i in range(N):
    li.append(tuple(map(int, sys.stdin.readline().split())))

# dp 테이블 초기화. dp는 가치를 저장하는 곳
dp = [[0 for _ in range(K + 1)] for __ in range(N)]

for i in range(N): # y축, 가방에 싸는 짐의 종류
    w,v = li[i]
    for j in range(1, K + 1): # x축, 무게
        dp[i][j] = dp[i - 1][j]  # 이전 행의 내용을 그대로 가져옴, i == 0일 때는 마지막 행의 내용을 참조하므로 상관없음.
        if (w <= j):  # 현재 보고 있는 짐을 가방에 넣을 수 있는 상태면(K보다 작은 값까지 확인)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v) # 넣는 것과 넣지 않는 것 중 어떤 것의 "가치"가  더 클지 고민한다.

print(dp[N-1][K])  # dp 테이블에서 가장 큰 값 출력
