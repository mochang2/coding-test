"""
211203
실버2 창영이와 점프
url: https://www.acmicpc.net/problem/22114
후기: 투 포인터 알고리즘으로 풀었다. dp 문제이기도 하다고 한다. 점화식은 도저히 생각이 안 나는데, 점화식이 잘 생각날 수 있도록 연습이 필요할 것 같다.
"""

import sys
N, K = map(int, sys.stdin.readline().strip().split())
L_li = list(map(int, sys.stdin.readline().strip().split()))

answer = 2
left = 0
right = 0
greater_than_K = 0 # 투 포인터 알고리즘. 매번 li를 만들고 해당 li에 대해서 세면 시간 초과가 날 것이라고 생각. K보다 큰 수의 개수만 세기로 결정.
if L_li[0] > K:
    greater_than_K += 1

while left < N - 2:
    if greater_than_K == 2 or right == N - 1: # left 움직이는 조건
        left += 1
        #print("move left", left)
        if L_li[left - 1] > K:
            greater_than_K -= 1
    else: # right 움직이는 조건(기본적으로, N이 아니라면)
        right += 1
        #print("move right", right)
        if right != N - 1 and L_li[right] > K:
            greater_than_K += 1
    answer = max(answer, right - left + 1)

print(answer)
