"""
211206
실버2 소수 구하기
url: https://www.acmicpc.net/problem/1929
후기: 에라토스테네스 체를 소수 개수 구하는 방식 외에도 사용할 수 있다는 것을 알았다. 그리고 set은 순서를 보장해주지 않기 때문에 15줄에 sorted가 반드시 필요하다.
"""

import sys
M, N = map(int, sys.stdin.readline().strip().split())
if M == 1:
    M += 1
num_set = set(range(M, N + 1))
for num in range(2, (N + 1) // 2 + 1):
    num_set -= set(range(2 * num, N + 1, num))

for i in sorted(list(num_set)):
    print(i)
