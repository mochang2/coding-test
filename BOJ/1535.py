"""
211214
실버2 안녕
url: https://www.acmicpc.net/problem/1535
후기: 11/12일 배낭문제에서 풀었던 거하고 똑같이 풀었는데, dp를 넉넉히 선언 안 하면 틀린다.. combination 써도 풀 수 있는 문제긴 하다.
"""

# dp 넉넉히 선언 안 하니까 틀림...
## 이유 찾았다! 1의 체력을 소모하는 애가 있을 경우 예외가 있음.
import sys
N = int(input())
minus = list(map(int, sys.stdin.readline().strip().split()))
plus = list(map(int, sys.stdin.readline().strip().split()))

dp = [[0 for _ in range(99)] for _ in range(N)]

for i in range(N):
    for j in range(99):
        dp[i][j] = dp[i - 1][j]
        if j - minus[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - minus[i]] + plus[i])

print(dp[N - 1][98])


# dp 넉넉히 선언하니까 맞음...
import sys
N = int(input())
minus = list(map(int, sys.stdin.readline().strip().split()))
plus = list(map(int, sys.stdin.readline().strip().split()))

dp = [[0 for _ in range(101)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(100):
        dp[i][j] = dp[i - 1][j]
        if j - minus[i - 1] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - minus[i - 1]] + plus[i - 1])

print(dp[N][99])
