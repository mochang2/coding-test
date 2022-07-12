"""
20220712
골드2 보석 도둑
url: https://www.acmicpc.net/problem/1202
후기: 처음에는 가방 + 보석? 아차.. 이거 DP다 문제 잘못 골랐다 싶었는데
가방에 보석을 하나밖에 못 담는다는 조건 때문에 DP가 아님을 확신했다.
일단 냅다 비싼 보석부터 담는 문제인가 싶어서 풀어봤는데, 그리디 문제가 맞았다.

하지만 처음 제출했을 때 시간 초과가 발생해서 오랜만에 답을 봤다.
아래 1번이 처음에 제출하기 전에 생각했던 방법이고 4번이 답을 보고 생각해낸 방법이다.

1. 비싼 보석 순으로, 가능한 최대 용량의 가방에 담는다. 최대 용량의 가방은 upper bound binary search를 이용한다.
  다만 어떤 가방에 보석을 담았는지 체크하기 위해서 한 번 더 선형탐색이 이루어진다. => O(NK)
  Linked List를 쓰면 insert, delete는 쉽지만 find가 느리다(binary search가 안됨)
2. 아무 보석이나 담는다? 완탐이므로 절대 안됨
3. 싼 보석 순으로 담는다? 보석 가치가 최대화 되지 않음
4. 용량이 작은 가방에 해당 가방에 담을 수 있는 가장 비싼 보석을 하나씩 담는다. => O(N + K)
"""

# 시간 초과 실패
import sys

input_ = sys.stdin.readline

def upperBound(li: list, value: int) -> int:
    left = 0
    right = len(li)
    
    while left < right:
        mid = (left + right) // 2
        if value > li[mid][0]:
            left = mid + 1
        else:
            right = mid
    
    return left

# initialization
answer = 0
N, K = map(int, input_().strip().split())
jewers = [tuple(map(int, input_().strip().split())) for _ in range(N)] # (보석 무게, 보석 가치)
knapsacks = [[int(input_().strip()), False] for _ in range(K)] # (감당 가능한 무게, 보석이 있는지 여부)
jewers.sort(key=lambda x: (-x[1]))
knapsacks.sort() # 오름차순 정렬

for index in range(N): # 비싼 보석부터, 보석을 기준으로 담을 수 있는 가방을 선택
    bound = upperBound(knapsacks, jewers[index][0])

    # bound를 1개씩 증가시켜서 K보다 클지 확인
    while bound < K and knapsacks[bound][1]:
        bound += 1
    
    if bound >= K: #담을 수 없는 무게
        continue
        
    answer += jewers[index][1]
    knapsacks[bound][1] = True

print(answer)


# 성공
import sys
from collections import deque
import heapq as h

input_ = sys.stdin.readline

# initialization
answer = 0
N, K = map(int, input_().strip().split())
jewers = [tuple(map(int, input_().strip().split())) for _ in range(N)] # (보석 무게, 보석 가치)
knapsacks = [int(input_().strip()) for _ in range(K)] # 감당 가능한 무게
heap = []

jewers.sort() # 무게 -> 가치 순으로 오름차순
knapsacks.sort() # 오름차순
jewers = deque(jewers)

for knapsack in knapsacks:
    while jewers and jewers[0][0] <= knapsack: # 보석 무게가 가방이 감당 가능한 무게보다 작을 때까지
        weight, value = jewers.popleft()
        h.heappush(heap, (-value, weight, value)) # 최소 힙이므로 -value를 추가

    if heap:
        _, weight, value = h.heappop(heap)
        answer += value

print(answer)
