"""
20220315
골드3 과제
url: https://www.acmicpc.net/problem/13904
후기: N의 최대는 1000, d의 최대는 1000인 것을 보고 permutation이나 combination 등을 쓰는 완전 탐색은 절대 안 될 것이라고 확신이 들었다. 
그렇가면 남은 것은 dp와 같은 것이었는데 문득 예전에 강의실의 최대 수를 풀던 문제가 기억이 났다.
강의가 시작하고 끝나는 시간을 기준으로 최대 강의실을 몇 개 예약해야 하는지 문제였는데
비슷한 느낌이 났다.
기준은 과제 제출까지 d-day인데 최종적으로 구하는 것은 과제의 가치였기 때문이다.
따라서 힙을 쓰는 것이 맞지 않을까 하고 생각했다.

여기서 참고할 점은 (다시 한 번 되짚어보지만) 파이썬 힙은 기본이 최소힙이다.
"""

import sys
import heapq as h

max_d = 1001

N = int(input())
assignments = [[0] for _ in range(max_d)] # 1 <= d <= 1000, 인덱스는 d-day를 표현하고, 해당하는 과제의 value들을 집어넣는다. 그 d-day에 해당하는 인풋이 없으면 기본적으로 0이 각각의 인덱스의 max값이 된다.
for _ in range(N):
    d, w = map(int, sys.stdin.readline().strip().split())
    assignments[d].append(w)
for i in range(max_d): # 가장 큰 값부터 뽑아서 힙에 집어넣을 수 있도록 내림차순 정렬을 한다.
    assignments[i].sort(reverse=True)

heap = []
for i in range(1, max_d):
    h.heappush(heap, assignments[i][0]) # 일단 제일 큰 숫자를 집어넣어
    for w in assignments[i][1:]:
        if heap[0] < w: # 힙의 최솟값보다 d-day에 해당하는 값 중 아직 수행되지 않은 과제가 있다면 힙에 집어넣는다.
            h.heapreplace(heap, w)
        else:
            break
print(sum(heap))
