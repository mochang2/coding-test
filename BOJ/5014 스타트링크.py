"""
20220611
골드5 스타트링크
url: https://www.acmicpc.net/problem/5014
후기: bfs를 통한 완탐 문제였다.
이번 문제는 bfs임을 알고 풀어서 금방 풀었지만
1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000 라는 조건만 봤을 때 이게 완탐으로 풀릴까? 라는 의문이 들었다.
아직도 완탐인지 아닌지 판단하는 기준이 미숙한 것 같다.
"""

# 완탐하면 O(F) = 1,000,000
# BFS로 완탐 가능. DFS는 recursion limit 걸릴듯

from collections import deque
import sys
input_ = sys.stdin.readline

def bfs(F, S, G, U, D):
    global directs
    queue = deque([(S, 0)])

    while len(queue): # != 0
        floor, step = queue.popleft()
        if floor == G:
            return step

        for direct in directs:
            new_floor = floor + direct
            if not 1 <= new_floor <= F or visited[new_floor]:
                continue

            visited[new_floor] = True
            queue.append((new_floor, step + 1))

    return 'use the stairs'
    

F, S, G, U, D = map(int, input_().strip().split())
directs = (U, -D)
visited = [False for _ in range(F + 1)]
visited[S] = True
print(bfs(F, S, G, U, D))
