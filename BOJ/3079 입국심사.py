"""
20220315
골드5 입국심사
url: https://www.acmicpc.net/problem/3079
후기: 넓은 범위, 해당 범위 안에 몇 명이 통과했는지만 알면 되는 문제.
전형적인 parametric search 문제 같았고 실제로 맞아서 금방 풀 수 있었다.
"""

# log(10 ** 18) = O(60) 이므로 시간 초과 없이 parametric search 가능

import sys

input_ = sys.stdin.readline

def calcImmigrants(time): # 해당 시간 동안 몇 명이 입국자 처리를 '완료'했는지
    global mid

    return mid // time

# initialization
min_ = 1
max_ = 10 ** 18
answer = max_
n, m = map(int, input_().strip().split()) # 입국 심사대 수, 여행자 수
times = [int(input_().strip()) for _ in range(n)] # 입국자 처리하는데 걸리는 시간

# parametric search
while min_ <= max_:
    mid = min_ + (max_ - min_) // 2

    counts = map(calcImmigrants, times)

    if sum(counts) >= m:
        answer = min(answer, mid)
        max_ = mid - 1
    else:
        min_ = mid + 1

# print
print(answer)
