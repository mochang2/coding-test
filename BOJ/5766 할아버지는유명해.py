"""
20220313
실버4 할아버지는 유명해!
url: https://www.acmicpc.net/problem/5766
후기: 구현 문제였다. 값이 unique할 때 list에서 최댓값, 두 번째로 큰 값을 찾는 것은 아주 간단하지만(파이썬 내장 함수 이용)
unique하지 않다고 가정하면 직접 순회하는 것밖에 방법이 없는 것 같다.
어렵지는 않은 문제였다.
"""

import sys

player_cnt = 10001

while True:
    # input
    N, M = map(int, sys.stdin.readline().strip().split())
    if (N, M) == (0, 0):
        sys.exit(0)
    scores = [0 for _ in range(player_cnt)]
    ranks = []
    for i in range(N):
        ranks.append(list(map(int, sys.stdin.readline().strip().split())))

    # add score
    for i in range(N):
        for j in range(M):
            scores[ranks[i][j]] += 1

    # find second's score
    max_ = max(scores)
    second_max_ = 0
    for i in range(player_cnt):
        if scores[i] == max_:
            continue
        second_max_ = max(second_max_, scores[i])

    # find answer
    answer = []
    for i in range(player_cnt):
        if scores[i] == second_max_:
            answer.append(i)
    answer.sort()
    for num in answer:
        print(num, end=" ")
    print()
