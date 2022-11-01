"""
20221101
플레4 전구
url: https://www.acmicpc.net/problem/2449
후기: 다이나믹 프로그래밍 문제였다.
문제의 핵심은 K(불빛 종류의 개수)를 사용하지 않는다는 것이다.
궁금해서 검색을 해보니 K를 사용하면 시간 초과가 난다고 한다. ㄴㅇㄱ

처음에는 그리디로 풀었었다.
그래서 되게 쉬운 문제로 착각했다(N도 작으니까).
그리디는 다음과 같이 풀었다.

1. bulbs에서 연속으로 중복된 숫자를 지운다.
2. 새로운 bulbs에서 각 위치를 시작점으로 하여 전구를 같은 색깔로 바꿔간다.
    이때 바꿀 색깔은 본인 그룹(같은 색의 전구들)을 기준으로 왼쪽 전구의 색으로,
    만약 왼쪽 전구가 없다면 오른쪽 전구의 색으로 바꾼다.
3. 모든 전구의 색이 같아질 때까지 2를 반복하고 그 중 최소를 구한다.

이렇게 풀면 반례가 존재한다.

6 3
1 2 1 3 2 3
답: 3(111323 -> 111333 -> 111111)
그리디 사용 시 답: 4(111323 -> 333323 -> 222223 -> 333333)

그때서야 문제 종류를 보니 DP라는 것이다.
여러 블로그들을 보며 어떻게 풀었는지 참고하니 min_costs[i][j]에 i번째 전구부터 j번째 전구까지 같은 색으로 만드는데 걸리는 최소 변환 횟수를 저장했다.
(만약 해당 계산을 저장하지 않으면 시간 초과가 난다. 합치는 순서가 중요하니 완탐을 하면 O(N!) 정도 걸렸을 것이다.)
해당 아이디어를 얻고 나는 다음과 같이 풀었다.

1. bulbs에서 연속으로 중복된 숫자를 지운다(안 지워도 풀 수 있지만 내가 개념상 와닿지 않아서 그냥 속편히 지웠다).
2. min_costs[i][i] = 0, min_costs[i][i + 1] = 1 으로 초기화한다.
3. 두 개의 그룹을 합치는 비용을 최소로 하는 비용을 찾는다.
    min_costs[i][j] 즉, i ~ j를 하나의 같은 색의 그룹으로 만드는 비용은
    i < k <= j에 대해 min_costs[i][k - 1] + min_costs[k][j] + 0 or 1이다.
    이때 최소 비용은 min(min_costs[i][k - 1] + min_costs[k][j] + 0 or 1)으로 구할 수 있다.
    위 식에서 0은 두 그룹의 색이 같을 때, 1은 두 그룹의 색이 다를 때를 의미한다.
    그룹의 색은 가장 왼쪽에 위치한 전구로 통일했는데, 어떤 위치의 전구로 색을 통일해도 최소값을 구하는데는 지장이 없다.
    (간단하게 3개의 전구 1 2 3, 1 1 1, 1 2 2 등을 합치는 최소 비용을 생각해보면 된다)
"""

# 오답
# 그리디

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
# DP

import sys

input_ = sys.stdin.readline
MAX = 200

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

def initializeMinCosts(length):
    global MAX
    
    min_costs = [[MAX for _ in range(length)] for __ in range(length)]

    for index in range(length):
        min_costs[index][index] = 0

    for index in range(length - 1):
        min_costs[index][index + 1] = 1

    return min_costs

def calculateMinCosts(bulbs, min_costs):
    for length in range(2, len(min_costs)):
        for start in range(0, len(min_costs) - length):
            end = start + length
            
            for intermediate in range(start + 1, start + length + 1):
                is_same_color = bulbs[start] == bulbs[intermediate] # 왼쪽 기준으로 색을 통일
                combination_cost = min_costs[start][intermediate - 1] + min_costs[intermediate][end]

                min_costs[start][end] = min(
                    min_costs[start][end],
                    combination_cost if is_same_color else combination_cost + 1 # 같은 색이면 그룹을 합치는데 비용이 0, 다른 색이면 비용이 1
                )

    return min_costs

n, k = map(int, input_().strip().split())
bulbs = list(map(int, input_().strip().split()))
bulbs = removeSequentDuplicates(bulbs)
min_costs = initializeMinCosts(len(bulbs))
min_costs = calculateMinCosts(bulbs, min_costs[:])

# answer
print(min_costs[0][-1])

