"""
211116
실버3 이친수
url: https://www.acmicpc.net/problem/2193
후기: 처음에는 점화식을 세우려다가, 노가다로 계산하다 보니 피보나치가 나옴.
"""

N = int(input())
# N자리 중에서 1번째 자리는 무조건 1. 두번째 자리는 무조건 0. 나머지는 0 또는 1
# 앞 자리가 1이면 반드시 0만 가능함(x1)
# 앞 자리가 0이면 0 또는 1이 가능함(x2)

dp = [0 for _ in range(N)]
dp[0] = 1

if N > 1:  # N == 1에 대한 에러처리를 안 해서 계속 index out of range 에러가 나옴
    dp[1] = 1

    for i in range(2, N):
        dp[i] = dp[i-1] + dp[i-2]
    
print(dp[-1])
