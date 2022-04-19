"""
211224
골드3 게임 개발
url: https://www.acmicpc.net/problem/1516
후기: 위상 정렬 문제였다. 시간 초과가 엄청 많이 났다. 이 전날 푼거(2056)로 처음 통과했지만, 다시 queue로 풀어서 통과했다.
while내에 있는 first가 종료 신호를 보내기 전에 이미 같은 작업들이 queue에 많이 쌓여있을 수 있기 때문이다.
예시로 입력이
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
들어오는데 현재 코드대로 작업이 진행된다면 0번째 작업이 끝난 이후 2번 작업이 큐에 들어오는데,
1번 작업이 끝난 이후에도 2번 작업이 다시 큐에 들어오게 된다. 이를 막기 위해 continue 조건을 걸어주었다.
"""

import sys
from collections import deque

def minus_one(i):
    return int(i) - 1

N = int(input())
inBound = [] # prerequisite
finished_times = [0 for _ in range(N)]
finished = set()
taken_times = []
for i in range(N):
    temp = list(map(minus_one, sys.stdin.readline().strip().split()))
    taken_times.append(temp[0] + 1)
    inBound.append(set(temp[1:-1]))
    
# queue를 이용한 위상정렬
queue = deque()
for i in range(N):
    if len(inBound[i]) == 0:
        queue.append(i)

while len(queue) != 0:
    first = queue.popleft()
    if first in finished:
        continue
    
    finished.add(first)
    last_finished = 0  # first를 가리키고 있던 것들 중에서 가장 늦게 끝난 놈의 시간을 구하기
    for i in inBound[first]:
        last_finished = max(last_finished, finished_times[i])
    finished_times[first] = taken_times[first] + last_finished

    for i in range(N):
        if i not in finished and inBound[i].issubset(finished):
            # 이미 실행한 작업이 아니면서 실행할 수 있는 작업인 경우
            queue.append(i)
    
for finished_time in finished_times:
    print(finished_time)
