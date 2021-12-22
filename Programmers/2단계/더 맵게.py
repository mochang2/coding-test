"""
211111
힙(Heap)
url: https://programmers.co.kr/learn/courses/30/lessons/42626
후기: 힙 모듈을 익힐 수 있었음
"""


# 예전 코드
import heapq as h

def solution(scoville, K):
    answer = 0
    
    h.heapify(scoville)

    while True:
        small_1 = h.heappop(scoville)

        if small_1 >= K:
            break
        else:
            if len(scoville) == 0:
                return -1
            small_2 = h.heappop(scoville)
            new_one = small_1 + 2 * small_2
            h.heappush(scoville, new_one)
            answer+=1
        
    return answer


import heapq as h

def solution(scoville, K):
    h.heapify(scoville)
    count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            count = -1
            break
        
        lowest = h.heappop(scoville)
        next_lowest = h.heappop(scoville)
        new = lowest + next_lowest * 2
        h.heappush(scoville, new)
        count += 1
    
    return count
