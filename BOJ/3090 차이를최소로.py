"""
20220901
플래3 차이를 최소로
url: https://www.acmicpc.net/problem/3090
후기: 의도치 않았지만 요근래 parametric search 문제가 골라서 풀게 되었고, 이 문제도 그래서 접근이 쉬웠다.
다만 엣지케이스를 잡지 못해서 많이 틀린 것 같은데, 해당 엣지케이스가 뭔지 잘 모르겠다.

100점을 맞지 못한 풀이는 다음과 같이 생각했다.
0. mid는 이분탐색의 중앙값이다.
1. sequence에서 가장 작은 수들의 index를 기억한다.
2. 해당 index들을 기준점으로 sequence들의 차이를 mid로 만들기 위해 다음과 같은 일을 한다.
  2-1. 가장 작은 index의 왼쪽에서 인접하는 수들의 차이가 mid 이하가 되도록 만든다.
  2-2. 가장 큰 index의 오른쪽에 인접하는 수들의 차이가 mid 이하가 되도록 만든다.
  2-3. 가장 작은 index와 가장 큰 index의 사이값들을 -> 방향과, <-방향 두 번 순회하면서 인접하는 수들의 차이가 mid 이하가 되도록 만든다.
3. 해당 mid값이 가능한지 판단하고 가능하면 answer를 update한다.
  
이 풀이가 먹히지 않아서 결국 답을 봤고 훨씬 간단했다.
위 과정에서 2를 다른 방식으로 바꿨다.
2-1. sequence를 -> 방향으로 순회하면서 부분적으로(2개의 인접한 수가) 오름차순일 때 해당 차이가 mid 이하가 되도록 만든다.
2-2. sequence를 <- 방향으로 순회하면서 부분적으로(2개의 인접한 수가) 오름차순일 때 해당 차이가 mid 이하가 되도록 만든다.


+) 문제에서 list를 출력하라고 했는데 채점 기준을 보면 제한된 t를 전부 사용하지 않아도 되고, 한 input에 대해서 다양한 output이 가능하다는 것이 힌트였다.
"""

## 오답

import sys
from copy import deepcopy

input_ = sys.stdin.readline

def initParameters() -> tuple:
    global sequence
    
    max_ = 0
    
    for index in range(len(sequence) - 1):
        difference = abs(sequence[index] - sequence[index + 1])
        max_ = max(max_, difference)

    return 0, max_

def getMinNumberIndexes() -> list:
    global sequence
    
    min_num = min(sequence)
    indexes = []

    for index in range(len(sequence)):
        if sequence[index] == min_num:
            indexes.append(index)

    return indexes

def reverseSearch(start: int, end: int, sequence: list) -> int:
    minus_count = 0

    for index in range(start, end, -1):
        difference = sequence[index] - sequence[index - 1]
        if -difference > mid: # 기준점이 더 작은 수
            minus_count -= difference + mid
            sequence[index - 1] += difference + mid
        elif difference > mid: # 기준점이 더 큰 수
            minus_count += difference - mid
            sequence[index] -= difference - mid

    return minus_count

def forwardSearch(start: int, end: int, sequence: list) -> int:
    minus_count = 0

    for index in range(start, end):
        difference = sequence[index] - sequence[index + 1]
        if -difference > mid: # 기준점이 더 작은 수
            minus_count -= difference + mid
            sequence[index + 1] += difference + mid
        elif difference > mid: # 기준점이 더 큰 수
            minus_count += difference - mid
            sequence[index] -= difference - mid

    return minus_count

def calcMinusCount() -> tuple:
    global mid, sequence, min_num_indexes

    minus_count = 0
    new_sequence = deepcopy(sequence)

    minus_count += reverseSearch(min_num_indexes[0], 0, new_sequence)
    minus_count += forwardSearch(min_num_indexes[-1], len(sequence) - 1, new_sequence)
    minus_count += forwardSearch(min_num_indexes[0], min_num_indexes[-1] - 1, new_sequence)
    minus_count += reverseSearch(min_num_indexes[-1], min_num_indexes[0], new_sequence)

    return minus_count, new_sequence

# initialization
MAX = 10 ** 9
n, t = map(int, input_().strip().split())
sequence = list(map(int, input_().strip().split()))
min_, max_ = initParameters() # parametric search를 위한 현재 수열에서 인접한 수와의 차이
min_num_indexes = getMinNumberIndexes()
max_difference = MAX
answer = sequence

while min_ <= max_:
    mid = min_ + (max_ - min_) // 2

    current_minus_count, new_sequence = calcMinusCount()

    if current_minus_count <= t:
        if max_difference > mid:
            max_difference = mid
            answer = new_sequence
        max_ = mid - 1
    else:
        min_ = mid + 1

# print
for num in answer:
    print(num, end=" ")
    
    
## 정답

import sys
from copy import deepcopy

input_ = sys.stdin.readline

def initParameters() -> tuple:
    global sequence
    
    max_ = 0
    
    for index in range(len(sequence) - 1):
        difference = abs(sequence[index] - sequence[index + 1])
        max_ = max(max_, difference)

    return 0, max_

def calcMinusCount() -> tuple:
    global mid, sequence, t

    minus_count = 0
    new_sequence = deepcopy(sequence)

    for index in range(0, len(sequence) - 1): # 정방향 오름차순일 때만 mid만큼의 차이 만들기
        difference = new_sequence[index] - new_sequence[index + 1]
        if -difference > mid:
            minus_count -= difference + mid
            new_sequence[index + 1] += difference + mid

    for index in range(len(sequence) - 1, 0, -1): # 역방향 오름차순일 때만 mid만큼의 차이 만들기
        difference = new_sequence[index] - new_sequence[index - 1]
        if -difference > mid:
            minus_count -= difference + mid
            new_sequence[index - 1] += difference + mid
            
    return minus_count <= t, new_sequence

# initialization
MAX = 10 ** 9
n, t = map(int, input_().strip().split())
sequence = list(map(int, input_().strip().split()))
min_, max_ = initParameters() # parametric search를 위한 현재 수열에서 인접한 수와의 차이
max_difference = MAX
answer = sequence

while min_ <= max_:
    mid = min_ + (max_ - min_) // 2

    result, new_sequence = calcMinusCount()

    if result:
        if max_difference > mid:
            max_difference = mid
            answer = new_sequence
        max_ = mid - 1
    else:
        min_ = mid + 1

# print
for num in answer:
    print(num, end=" ")
