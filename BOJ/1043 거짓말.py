"""
20220315
골드4 거짓말
url: https://www.acmicpc.net/problem/1043
후기: 진실을 아는 사람이 점차 전염되어 나가는 구조이다.
처음에는 union find라고 생각했는데 만약 처음에 진실을 아는 사람이 1명이 아니면 다수의 조상이 생겨서 다른 방법을 고민했다.
여러 개의 시작점 + 하나의 그룹 => 시작점을 다양하게 하는 dfs/bfs가 문제푸는 방법이라 생각했고 구현하니 문제가 풀렸다.
"""

import sys
from itertools import combinations
from collections import deque

# initialization
N, M = map(int, sys.stdin.readline().strip().split())
truth = list(map(int, sys.stdin.readline().strip().split()))
parties = []
adjacent = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for i in range(M):
    tmp = list(map(int, sys.stdin.readline().strip().split()))[1:]
    parties.append(tmp)
    for meet in combinations(tmp, 2):
        adjacent[meet[0]].append(meet[1])
        adjacent[meet[1]].append(meet[0])

# bfs
for start in truth[1:]:
    visited[start] = True
    queue = deque([start])
    while len(queue) != 0:
        person = queue.popleft()
        for friend in adjacent[person]:
            if visited[friend] == False:
                visited[friend] = True
                queue.append(friend)

# print
cnt = 0
for party in parties:
    flag = True
    for num in party:
        if visited[num] == True:
            flag = False
            break
    if flag:
        cnt+=1

print(cnt)

