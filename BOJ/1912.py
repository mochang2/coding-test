"""
20220419
실버2 연속합
url: https://www.acmicpc.net/problem/1912
후기: dp인거 알고 풀었는데도 못 풀어서 답을 봤다.
처음에 생각한 방법은 포인터 두 개를 만들어서, 부호가 같은 숫자끼리 연속되어 있으면 더한 뒤 새로운 list(sums)에 저장한다.
그 뒤에 지지고 볶고 하려고 했는데 같은 부호로만 이루어진 수열이 주어질 수도 있고, sums[0]이 음수일수도, 양수일수도 등등등 너무 많은 예외가 존재해서 포기했다.
답이 너무 간단해서 오히려 화도 안 났다.

비슷한 느낌인 LIS: leetcode 334과 boj 12015, boj 11055을 참고
"""

import sys
input_ = sys.stdin.readline

n = int(input_().strip())
sequence = list(map(int, input_().strip().split()))
dp = [0 for _ in range(n)] # answer = max(dp)
for i in range(n): # 다른 언어 같은 경우 dp[0] = sequence[0]으로 한 뒤 range(1,n)으로 선언해야 함
    dp[i] = max(sequence[i], dp[i - 1] + sequence[i]) # 본인이 가진 수를 이전합과 합쳐서 더 커지는지 아닌지를 확인하며 저장

print(max(dp))
