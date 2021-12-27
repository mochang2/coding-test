"""
211227
골드5 최소 회의실 개수
url: https://www.acmicpc.net/problem/19598
후기: 처음에 사고한 방법은 2차원 배열에 차례로 넣어두고 부족하면 2번째 차원의 배열 수를 늘리는 방법을 생각했다.
그랬더니 O(nC2)가 나와서 N == 100,000일 때는 시간 초과가 날 것 같아 새로운 방법을 고민해야 했다.
답을 본 결과 heap을 쓰는 방법이 있었다. 그리디 문제여서 그런지 코드는 간결하지만 사고가 어려운 문제였다.
"""

import sys
import heapq as h
times = []
N = int(input())
for i in range(N):
    times.append(list(map(int, sys.stdin.readline().strip().split())))

# (시작 시간, 끝 시간) 기준으로 오름차순 정렬
times.sort()
heap = []
h.heappush(heap, times[0][1])  # 가장 먼저 끝나는 작업을 최소힙에 넣음
for time in times[1:]:
    if heap[0] > time[0]:  # 지금 보는 작업(time)의 시작 시각과 최소힙 루트의 끝나는 시각을 비교
        h.heappush(heap, time[1])
    else:
        h.heapreplace(heap, time[1])
"""
# help(heapq.heapreplace) 설명
heapreplace(heap, item, /)
    Pop and return the current smallest value, and add the new item.
    
    This is more efficient than heappop() followed by heappush(), and can be
    more appropriate when using a fixed-size heap.  Note that the value
    returned may be larger than item!  That constrains reasonable uses of
    this routine unless written as part of a conditional replacement:
    
        if item > heap[0]:
            item = heapreplace(heap, item)
"""

print(len(heap))
