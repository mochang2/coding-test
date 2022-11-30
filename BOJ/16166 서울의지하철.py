"""
20221130
실버1 서울의 지하철
url: https://www.acmicpc.net/problem/16166
후기: heap을 이용하지 않았지만 다익스트라'처럼' 풀었다.
지속적으로 최소 환승 가능한지만 확인해주면 되기 때문이다.
(bfs로 못 풀거 같았는데 다 풀고 다시 생각해보니까 bfs로도 될 거 같긴 하다)

코드 흐름은 다음과 같다.
1. 출발역이 어느 호선인지 / 도착역이 어느 호선인지 확인한다.
2. 각 호선 간 어떻게 연결되어 있는지 파악한다.
3. 출발 호선부터 도착 호선까지 몇 번 환승해야 하는지 계산한다.
4. 최소 환승 횟수를 구한다.

+) 수정
initializeTransferCounts 에서 adjacent_lines를 인자로 받았었는데, 사용하지 않아서 (제출은 다시 안 해봤지만)
length를 인자로 받게 바꿨다.
"""

import sys
from collections import deque

input_ = sys.stdin.readline
MAX_TRANSFER_COUNT = 10

def initializeInputs():
    number_of_lines = int(input_().strip())
    stations_in_lines = [set(list(map(int, input_().strip().split()))[1:]) for _ in range(number_of_lines)]
    start_station = 0
    end_station = int(input_().strip())

    return stations_in_lines, start_station, end_station

def getTargetLines(stations_in_lines, start_station, end_station):
    start_lines = []
    end_lines = []

    for line, stations in enumerate(stations_in_lines):
        if start_station in stations:
            start_lines.append(line + 1)

        if end_station in stations:
            end_lines.append(line + 1)

    return start_lines, end_lines

def connectLines(stations_in_lines):
    def hasIntersection(set1, set2):
        return len(set1 & set2) != 0
    
    number_of_lines = len(stations_in_lines)
    adjacent_lines = [set() for _ in range(number_of_lines)]

    for line1 in range(number_of_lines):
        for line2 in range(line1 + 1, number_of_lines):
            stations1 = stations_in_lines[line1]
            stations2 = stations_in_lines[line2]
            
            if hasIntersection(stations1, stations2):
                adjacent_lines[line1].add(line2 + 1)
                adjacent_lines[line2].add(line1 + 1)

    return adjacent_lines

def initializeTransferCounts(length, start_lines):
    global MAX_TRANSFER_COUNT
    
    transfer_counts = [MAX_TRANSFER_COUNT for _ in range(length)]

    for start_line in start_lines:
        transfer_counts[start_line] = 0

    return transfer_counts

def calculateTransfers(adjacent_lines, start_lines):
    transfers = initializeTransferCounts(len(adjacent_lines) + 1, start_lines) # 각 호선으로 가기 위한 환승 횟수
    reachable_lines = deque(map(lambda line:(0, line), start_lines)) # deque, (cost, line)[]

    while len(reachable_lines) != 0:
        transfer_count, line = reachable_lines.popleft()

        for adjacent_line in adjacent_lines[line - 1]:
            cannot_reach_with_lower_transfer_count = transfer_count + 1 >= transfers[adjacent_line]
            
            if cannot_reach_with_lower_transfer_count:
                continue

            # 더 적게 환승할 수 있는 길 발견
            new_transfer_count = transfer_count + 1
            reachable_lines.append((new_transfer_count, adjacent_line))
            transfers[adjacent_line] = new_transfer_count

    return transfers

def getSmallestTransferCount(transfers, end_lines):
    global MAX_TRANSFER_COUNT

    smallest_transfer_count = min(map(lambda line:transfers[line], end_lines))

    return smallest_transfer_count if smallest_transfer_count != MAX_TRANSFER_COUNT else -1

# main
stations_in_lines, start_station, end_station = initializeInputs()
start_lines, end_lines = getTargetLines(stations_in_lines, start_station, end_station)

adjacent_lines = connectLines(stations_in_lines)
transfers = calculateTransfers(adjacent_lines, start_lines)
smallest_transfer_count = getSmallestTransferCount(transfers, end_lines)

# print answer
print(smallest_transfer_count)
