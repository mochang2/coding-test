"""
211227
실버1 컨베이어 벨트 위의 로봇
url: https://www.acmicpc.net/problem/20055
후기: 빡구현. 문제가 이해하기 어려워서 어려운 문제였다. 중간에 실수한 게 있어서 틀리기도 했다. 빡구현 가끔 풀 필요는 있다.
"""

import sys
from collections import deque

def init_input(num):
    # 처음부터 내구도가 이상한 벨트가 들어올 수도 있으니까
    global count
    num = int(num)
    if num <= 0:
        count += 1
    return num

def rotate():
    global N, belt, count
    belt.rotate(1)
    for i in range(len(robots)):
        robots[i] += 1
    if len(robots) != 0 and robots[0] == N - 1:
        robots.popleft()

    for index, robot in enumerate(robots):
        if belt[robot + 1] != 0 and robots[index - 1] != robot + 1:
            # 이동할 수 있다면
            robots[index] += 1 # == robot
            belt[robots[index]] -= 1
            if belt[robots[index]] == 0:
                count += 1
    if len(robots) != 0 and robots[0] == N - 1: # len은 index error를 막기 위해 넣은 조건
        robots.popleft()

N, K = map(int, sys.stdin.readline().strip().split())
count = 0
belt = deque(list(map(init_input, sys.stdin.readline().strip().split())))
robots = deque()

result = 0
while count < K: # 4단계
    # 1, 2단계
    rotate()
    
    # 3단계
    if belt[0] != 0:
        robots.append(0)
        belt[0] -= 1
        if belt[0] == 0:
            count += 1

    result += 1

print(result)
