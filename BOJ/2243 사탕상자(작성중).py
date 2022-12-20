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

두 번째 시도는...
"""

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


