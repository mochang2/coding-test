"""
20220412
실버2 가장 큰 증가 부분 수열
url: https://www.acmicpc.net/problem/11055
후기: well-known 문제로 DP가 나오면 문제를 버릴 순 없으므로 감만 익히기 위해 풀었다.
처음에 dp를 0으로 초기화했을 시에는 li[i] <= li[j]인 경우에 dp 값이 갱신되지 않았다.
이로 인해 그 아래줄에서 dp를 갱신하는데 dp[j]가 0이었다면 잘못된 답이 나올 수 있다.

반례:
5
5 1 2 3 10
답 dp: 5 1 2 6 16
내 dp: 5 0 2 5 15
답: 16, 내 오답: 15

leetcode 334과 boj 12015을 참고
LIS 알고리즘 설명: https://rebro.kr/33
"""

## 오답
import sys
input_ = sys.stdin.readline

N = int(input_())
li = list(map(int, input_().strip().split()))
dp = [0 for _ in range(N)]
dp[0] = li[0]

for i in range(1, N):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j] + li[i])
print(max(dp))


## 정답
# LIS 응용. O(N^2) <= 1,000,000 이므로 가능
import sys
from copy import deepcopy
input_ = sys.stdin.readline

N = int(input_())
li = list(map(int, input_().strip().split()))
dp = deepcopy(li) # dp 초기화는 li로. 길이가 1인 수열이 존재할 수도 있으므로

for i in range(1, N):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j] + li[i])
print(max(dp))
