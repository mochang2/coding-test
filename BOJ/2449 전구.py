"""
20221101
플레4 전구
url: https://www.acmicpc.net/problem/2449
후기: 
"""

# 오답
# 그리디
"""
반례

6 3
1 2 1 3 2 3
답: 3
"""

import sys
from copy import deepcopy

input_ = sys.stdin.readline

def removeSequentDuplicates(list_):
    if len(list_) < 2:
        return list_
    
    uniques = []
    left = 0
    right = 0

    while left < len(list_):
        while right < len(list_) and list_[left] == list_[right]:
            right += 1

        uniques.append(list_[left])

        left = right
        right = left + 1

    return uniques

def changeLight(index, bulbs):
    change_count = 0
    temp_bulbs = deepcopy(bulbs)
    left = index
    right = index

    while left != 0 or right != len(temp_bulbs) - 1:
        if left == 0:
            right += 1
            next_color = temp_bulbs[right]
        else:
            left -= 1
            next_color = temp_bulbs[left]
            
        temp_bulbs = temp_bulbs[:left] + [next_color] * (right - left + 1) + temp_bulbs[right + 1:]
        change_count += 1

        # 합쳐졌는데 같은 색이라서 left, right를 더 이동해야 하는 경우
        while left >= 1 and temp_bulbs[left - 1] == next_color:
            left -= 1
        while right < len(temp_bulbs) - 1 and temp_bulbs[right + 1] == next_color:
            right += 1

    return change_count

# initialization
answer = 200
n, k = map(int, input_().strip().split())
bulbs = list(map(int, input_().strip().split()))
bulbs = removeSequentDuplicates(bulbs)

for index in range(len(bulbs)): # 각 위치를 바꿀 전구의 시작점으로 지정
    change_count = changeLight(index, bulbs)
    answer = min(answer, change_count)

print(answer)


# 정답


