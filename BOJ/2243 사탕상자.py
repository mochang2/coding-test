"""
20221220
플레5 사탕상자
url: https://www.acmicpc.net/problem/2243
후기: 자료구조 문제이다.

사탕 맛이 1,000,000가지, 쿼리 개수가 100,000개, 사탕의 총 개수가 2,000,000,000인데,
k번째 맛을 가진 사탕(1)과 m이라는 맛을 가진 사탕(2)에 대한 다양한 쿼리가 존재하므로
완탐으로는 절대 해결이 안되는 문제이다.

첫 번째 시도는 heap과 list를 같이 사용했지만 시간 초과로 실패했다.
단순히 heap만 사용하면 사탕의 총 개수가 문제이므로 해당 맛을 가진 사탕의 개수를 list로 저장한다.
heap에는 오직 unique한 사탕 맛만 넣어둔다.
(1)에 대해서는 heap에서 차례로 뺀 다음에 list의 개수를 확인한다.
(2)에 대해서는 list에 개수를 변화시킨 뒤 만약 처음 들어가는 맛이나, 개수가 0개가 되는 맛이면 heap에 추가하거나 삭제한다.

두 번째 시도는 답을 본 끝에 펜윅 트리(또는 세그먼트 트리도 가능)와 이분 탐색을 이용했다.
펜윅 트리에 저장하는 것은 맛에 따른, 구간합에 포함된 사탕 개수이다.
펜윅 트리는 구간합을 나타내는 자료 구조이므로 (2)에 대해서는 O(log 1,000,000)안에 해결이 가능하다.
(1)에 대해서도 부분합과 이분 탐색을 활용해 k번째를 O(2 * log 1,000,000)안에 해결이 가능하다.

+) 참고로 구간합은 a ~ b까지의 합이고, 부분합은 1 ~ b까지의 합이다.
"""

# 첫 번재 시도
# 

from sys import stdin
import heapq as h

MAX_TASTE = 1000000

def getInput():
    option = {
        'TAKE': 1,
        'PUT': 2,
    }
    input_ = stdin.readline
    
    number_of_touches = int(input_().strip())
    for _ in range(number_of_touches):
        command = tuple(map(int, input_().strip().split()))

        if command[0] == option['TAKE']:
            rank = command[1]
            takeKthTaste(rank)
        
        elif command[0] == option['PUT']:
            taste, count = command[1], command[2]
            
            put_command = command[2] >= 0
            if put_command:
                putCandy(taste, count)
            else:
                takeCandy(taste, count)

def takeKthTaste(rank): # heap에서 rank번째 taste를 꺼냄
    global candy_counts, tastes
    
    temporarily_removed_tastes = []

    while rank > 0:
        taste = tastes[0]
        
        if candy_counts[taste] == 0:
            h.heappop(tastes)
            continue

        difference = min(rank, candy_counts[taste])
        rank -= difference

        temporarily_removed_tastes.append(h.heappop(tastes))

    print(temporarily_removed_tastes[-1])

    taken_taste = temporarily_removed_tastes[-1]
    candy_counts[taken_taste] -= 1
    if candy_counts[taken_taste] == 0:
        temporarily_removed_tastes.pop()

    for taste in temporarily_removed_tastes:
        h.heappush(tastes, taste)

def putCandy(taste, count):
    global candy_counts, tastes

    if candy_counts[taste] == 0:
        h.heappush(tastes, taste)

    candy_counts[taste] += count

def takeCandy(taste, count):
    global candy_counts

    candy_counts[taste] -= count

candy_counts = [0 for _ in range(MAX_TASTE + 1)]
tastes = [] # heap

getInput()


# 두 번째 시도
# 정답

from sys import stdin

MAX_TASTE = 1000000

def getInput():
    option = {
        'TAKE': 1,
        'PUT': 2,
    }
    input_ = stdin.readline
    
    number_of_touches = int(input_().strip())
    for _ in range(number_of_touches):
        command = tuple(map(int, input_().strip().split()))

        if command[0] == option['TAKE']:
            rank = command[1]
            taste = getKthTaste(rank)           
            changeCandyCount(taste, -1)
            
            print(taste)
        
        elif command[0] == option['PUT']:
            taste, count = command[1], command[2]
            changeCandyCount(taste, count)

def getKthTaste(rank): 
    global candy_count_prefix_sum, MAX_TASTE

    left = 1
    right = MAX_TASTE

    while left < right:
        mid = left + (right - left) // 2

        partial_sum = getPartialSum(mid)
        if partial_sum >= rank:
            right = mid
        else:
            left = mid + 1

    return left

def getPartialSum(taste):
    global candy_count_prefix_sum
    
    sum_ = 0

    while taste > 0:
        sum_ += candy_count_prefix_sum[taste]
        taste -= getLeastOneBit(taste)

    return sum_

def changeCandyCount(taste, difference):
    global candy_count_prefix_sum

    while taste < len(candy_count_prefix_sum):
        candy_count_prefix_sum[taste] += difference
        taste += getLeastOneBit(taste)

def getLeastOneBit(number):
    return number & -number

candy_count_prefix_sum = [0 for _ in range(MAX_TASTE + 1)] # 펜윅 트리
getInput()

