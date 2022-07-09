"""
20220709
골드2 가운데를 말해요
url: https://www.acmicpc.net/problem/1655
후기: 제한 시간이 0.1초(파이썬은 0.6초)인 문제였다.
무조건 O(N log N) 또는 O(N)으로만 풀 수 있는 문제라 직감해서 DP와 heap 중에 고민하다가
heap을 반드시 한 개만 써야 되나? 라는 생각이 드는 순간 풀 수 있는 방법이 떠올랐다.
max heap과 min heap을 동시에 선언한 뒤, 중위값을 무조건 max heap의 [0] 번째 값으로 설정해두면 조건문 분기는 많지만 풀릴 것 같았다.
"""

# 꽤 더러워 보이지만 100줄 넘는 코드도 많았던 것을 보니 깔끔한 풀이 같다.
# +) index >= 3 중에서 if elif else 조건이 같은 애들을 합치면 더 깔끔한 풀이가 됐을 듯

import sys
import heapq as h

input_ = sys.stdin.readline

def answer():
    global max_heap
    print(-max_heap[0])

N = int(input_().strip())
min_heap = [] # 기본 힙
max_heap = [] # - 붙여야 함

for index in range(1, N + 1):
    num = int(input_().strip())
    
    if index == 1:
        h.heappush(max_heap, -num)
        
    elif index == 2:
        if -max_heap[0] < num:
            h.heappush(min_heap, num)
        else:
            h.heappush(min_heap, -h.heappop(max_heap))
            h.heappush(max_heap, -num)
            
    else: # index >= 3:
        if len(max_heap) == len(min_heap): # max_heap에 추가
            if -max_heap[0] < num < min_heap[0]:
                h.heappush(max_heap, -num)
            elif num <= -max_heap[0]:
                h.heappush(max_heap, -num)
            else: # min_heap[0] <= num:
                h.heappush(max_heap, -h.heappop(min_heap))
                h.heappush(min_heap, num)
                
        else: # len(max_heap) == len(min_heap) + 1: min_heap에 추가
            if -max_heap[0] < num < min_heap[0]:
                h.heappush(min_heap, num)
            elif num <= -max_heap[0]:
                h.heappush(min_heap, -h.heappop(max_heap))
                h.heappush(max_heap, -num)
            else: # min_heap[0] <= num:
                h.heappush(min_heap, num)
                
    answer()
