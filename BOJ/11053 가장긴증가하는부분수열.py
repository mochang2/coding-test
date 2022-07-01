"""
20220701
실버2 가장 큰 증가 부분 수열
url: https://www.acmicpc.net/problem/11053
후기: 이제 well-known DP 중에서 가장 자신 있다.
result라는 변수를 선언하지 않고 직접 dp에서 값을 변경했으면 더 간결해졌을 수는 있지만 이해하기 힘든 코드일 것 같다.
"""

# 1 <= N <= 1000 이므로 O(N^2) 내에서 해결 가능
import sys

input_ = sys.stdin.readline

# initialization
N = int(input_().strip())
sequence = tuple(map(int, input_().strip().split()))

dp = [0 for _ in range(N)]
dp[0] = 1

for curr_index in range(1, N):
    # 본인(curr_index)보다 작은 수들의 수열 중 본인을 포함할 때 가장 길게 되는 길이를 저장
    # 자기 자신만 포함되어도 길이가 1이므로 1로 초기화
    result = 1
    for prev_index in range(curr_index):
        if sequence[curr_index] > sequence[prev_index]:
            result = max(result, dp[prev_index] + 1)
    dp[curr_index] = result

print(max(dp))
