"""
20220104
골드5 강의실 배정
url: https://www.acmicpc.net/problem/11000
후기: 12/27에 푼 19598번(최소 회의실 개수)와 똑같은 문제였다.
다행히 이번에는 답을 보지 않고 해결했다.
"""

import sys
import heapq as h

N = int(input())
classes = []
for i in range(N):
    classes.append(list(map(int, sys.stdin.readline().strip().split())))
classes.sort()  # 시작 시간 -> 끝나는 시간 기준으로 정렬

answer = 0
heap = [classes[0][1]]  # 끝나는 시간을 힙에 넣음
h.heapify(heap)
for class_ in classes[1:]:
    # 힙에 넣을지 판단은 class_의 시작 시간과 힙에 있는 끝나는 시간을 비교함으로써
    if heap[0] > class_[0]:
        h.heappush(heap, class_[1])
    else:
        h.heapreplace(heap, class_[1])
    answer = max(answer, len(heap))
print(answer)
