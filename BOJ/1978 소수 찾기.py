"""
실버4 소수 찾기
url: https://www.acmicpc.net/problem/1978
후기: 에라토스테네스의 체가 진짜 짱이다. 별 수학 공식 필요 없어서 좋았다.
"""

import sys

N = int(input())
num_set = set(map(int, sys.stdin.readline().strip().split()))
num_set -= set({1})
Max = 1000

for i in range(2, Max + 1):
    num_set -= set(range(2 * i, Max + 1, i)) # i의 2배부터 n + 1까지의 수 중 i의 배수를 모두 num_set에서 제외
print(len(num_set))


        
