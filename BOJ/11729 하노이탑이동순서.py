"""
20220315
실버1 하노이 탑 이동순서
url: https://www.acmicpc.net/problem/11729
후기: n이 20 밖에 되지 않아서 recursion limit을 설정할 필요가 없었다.
한 가지 실수했던 것은 재귀인데 재귀 종료 조건(n == 1)을 안 걸었어서 틀렸었다.
"""

import sys

input_ = sys.stdin.readline

def hanoi(n, from_, by, to):
    global answer

    if n == 1:
        answer.append((from_, to))
    else:
        hanoi(n - 1, from_, to, by) # n번째를 옮기기 전 n - 1개는 from에서 by로 옮겨야 함
        answer.append((from_, to))
        hanoi(n - 1, by, from_, to) # n번재를 옮긴 후 n - 1개는 by에서 to로 옮겨야 함

# initialization
n = int(input_().strip())
answer = []

hanoi(n, 1, 2, 3)
print(len(answer))
for from_, to in answer:
    print(from_, to)
