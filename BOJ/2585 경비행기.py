"""
20220826
골드2 경비행기
url: https://www.acmicpc.net/problem/2585
후기: 처음에는 단순히 parametric search(+ greedy)인 줄 알고 풀었으나 아니었고, 틀렸다.
예시를 든 것은 아니지만 아래 첫 번째 코드에서 틀릴만한 부분이 생각났다.

이후 이분탐색 + 그래프 탐색으로 푸는 문제라는 것을 알고 '치즈' 문제처럼 deepcopy를 이용한 bfs로 풀었더니 해결됐다.
"""

# 오답 코드

"""
while 문 안에 for문이 잘못됨

current_pos에서 갈 수 있는 가장 먼 위치가 반드시 옳은 길이 아닐 수도 있음
A -> B(거리 100)
A -> C(거리 1000) 이어서 C를 골랐는데 C에서 end로 더이상 갈 길이 없는 반면
A -> B -> D -> ... -> end를 통해서, k + 1번 이내로 end에 도달할 수도 있음
"""

import sys
from math import ceil

input_ = sys.stdin.readline

def calcDistance(pos1: tuple, pos2: tuple) -> float:
    y1, x1 = pos1
    y2, x2 = pos2
    
    return ((y1 - y2) ** 2 + (x1 - x2) ** 2) ** 0.5

def calcFuel(distance: float) -> int:
    return ceil(distance / 10)

def upperBound(list_: list, target: int) -> int: # 정렬된 배열에서 찾고자 하는 값(target)보다 큰 값이 처음 나타나는 위치
    left = 0
    right = len(list_)

    while left < right:
        mid = (left + right) // 2
        if target >= list_[mid]:
            left = mid + 1
        else:
            right = mid

    return right

# initialization
answer = 1500 # 15000km를 갈 수 있는 연료통. start -> end를 한 번에 갈 수 있는 양
start = (0, 0)
end = (10000, 10000)
n, k = map(int, input_().strip().split()) # 비행장 수, 허용 중간급유 횟수
positions = [tuple(map(int, input_().strip().split())) for _ in range(n)]
positions.append(start)
positions.append(end)
positions.sort()

# parametric search
min_fuel = 1
max_fuel = answer

while min_fuel <= max_fuel:
    current_pos_index = 0
    current_pos = positions[current_pos_index]
    fuel = (min_fuel + max_fuel) // 2
    flag = False

    for _ in range(k + 1): # 해당 fuel로 몇 번 만에 목적지에 도착하는지. 목적지 도착 횟수 포함
        next_possible_positions = positions[current_pos_index:]
        distances = [calcDistance(current_pos, pos) for pos in next_possible_positions]
        fuels = sorted([calcFuel(distance) for distance in distances])
        
        index = upperBound(fuels, fuel) - 1 # find upper bound. 해당 연료로 갈 수 있는 가장 먼 위치
        if index == 0: # 해당 연료통 용량으로는 갈 수 있는 다음 위치가 없음
            break
        current_pos_index += index
        current_pos = positions[current_pos_index]
        if current_pos == end:
            flag = True
            break # 도착
        
    if flag: # k번 이내에 목적지 도착 가능
        answer = min(answer, fuel)
        max_fuel = fuel - 1
    else:
        min_fuel = fuel + 1
    
# print
print(answer)


# 정답 코드

import sys
from math import ceil
from copy import deepcopy

input_ = sys.stdin.readline

def calcDistance(pos1: tuple, pos2: tuple) -> float:
    y1, x1 = pos1
    y2, x2 = pos2
    
    return ((y1 - y2) ** 2 + (x1 - x2) ** 2) ** 0.5

def calcFuel(distance: float) -> int:
    return ceil(distance / 10)

def initVisited(length: int) -> list:
    return [False for _ in range(length)]

def bfs(start_index: int, fuel: int) -> int:
    global costs, n, k
    
    count = 0
    queue = [start_index] # 굳이 deque이 필요 없음
    visited = initVisited(n + 2)
    visited[start_index] = True

    while queue:
        next_queue = []
        
        while queue:
            index = queue.pop()

            for i in range(n + 2):
                if not visited[i] and costs[index][i] <= fuel:
                    if i == n + 1:
                        return count
                    visited[i] = True
                    next_queue.append(i)

        queue = deepcopy(next_queue)
        count += 1

    return k + 1 # 도달 불가능

# initialization
MAX_ = 1500 # 15000km를 갈 수 있는 연료통. start -> end를 한 번에 갈 수 있는 양
answer = MAX_

n, k = map(int, input_().strip().split()) # 비행장 수, 허용 중간급유 횟수
positions = [(0, 0)] # 그래프 탐색 출발점
positions.extend([tuple(map(int, input_().strip().split())) for _ in range(n)])
positions.extend([(10000, 10000)]) # 그래프 탐색 도착점

costs = [[MAX_ for _ in range(n + 2)] for __ in range(n + 2)]
for i in range(n + 2):
    for j in range(i + 1, n + 2):
        distance = calcDistance(positions[i], positions[j])
        fuel = calcFuel(distance)
        costs[i][j] = fuel
        costs[j][i] = fuel

# binary search
min_fuel = 1
max_fuel = answer

while min_fuel <= max_fuel:
    current_pos_index = 0
    current_pos = positions[current_pos_index]
    fuel = (min_fuel + max_fuel) // 2

    count = bfs(0, fuel)
        
    if count <= k: # k번 이내에 목적지 도착 가능
        answer = min(answer, fuel)
        max_fuel = fuel - 1
    else:
        min_fuel = fuel + 1
    
# print
print(answer)

