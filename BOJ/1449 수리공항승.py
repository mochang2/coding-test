"""
211209
실버3 수리공 항승
url: https://www.acmicpc.net/problem/1449
후기: 시간초과 걱정은 없어서 쉬웠던 것 같다. 더 간단하게 풀 수 있을 거 같은데 변수가 많은 게 아쉽다.
"""

import sys
N, L = map(int, sys.stdin.readline().strip().split())
li = sorted(list(map(int, sys.stdin.readline().strip().split())))
    
# N = len(li)
index = 0  # li에 대한 인덱스
result = 0  # 출력할 결과물
while index < N:
    placement = li[index]
    result += 1
    tmp_l = 1
    while tmp_l != L: # 테이프를 한 번 붙였을 때 연결된 몇 개의 파이프를 막을 수 있는지 체크
        if index == N - 1:
            break
        if placement + tmp_l == li[index + 1]:
            index += 1
        tmp_l += 1
    index += 1
print(result)
