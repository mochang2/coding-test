"""
20230406
골드3 성곽
url: https://www.acmicpc.net/problem/2234
후기: 약간 응용만 하면 되는 dfs/bfs 완전탐색이다.

다음과 같은 방법으로 풀었다.
1. 입력을 받고, visited를 초기화한다.
2. castle[y][x]가 visited되지 않았다면 해당 위치를 시작점으로 dfs를 돈다.
3. dfs로 방문하는 location(y, x)를 list로 반환한다.
4. rooms에 location들을 저장한다.
5. rooms에서 combinations를 돌며 임의의 2개 room을 선택한다.
6. 그 두 개의 방이 벽 하나를 뚫으면 연결되었는지 확인한다.
   이때 각각의 room에 대해 location을 이중 for문으로 돌며 인접한지 확인하는 방식으로 진행한다.
   다만 두 room size의 합이 기존에 구한 값보다 작으면 인접한지 확인하지 않는다.
   두 room size의 합이 기존에 구한 값보다 크고, 두 room이 인접했다면 두 room size를 더한다.
7. 답을 출력한다.
   방의 개수는 len(rooms),
   가장 큰 방은 rooms의 각 room['size'] 중 가장 큰 값,
   하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기은 6에서 구한 값이다.
"""

from sys import stdin, setrecursionlimit
from itertools import combinations

setrecursionlimit(50 ** 2)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
walls = [2, 4, 8, 1]

def initializeVisited():
    return [[False for _ in range(number_of_column)] for __ in range(number_of_row)]

def getRoomInformation():
    rooms = []
    
    for y in range(number_of_row):
        for x in range(number_of_column):
            if visited[y][x]:
                continue

            visited[y][x] = True
            location = searchLocationOfRoom(y, x, [(y, x)])
            rooms.append({
                'location': location,
                'size': len(location)
            })

    return rooms

def searchLocationOfRoom(y, x, location):
    for direction in range(4):
        new_y, new_x = y + dy[direction], x + dx[direction]

        if isBlocked(y, x, direction) or visited[new_y][new_x]:
            continue
        
        visited[new_y][new_x] = True
        location.append((new_y, new_x))
        searchLocationOfRoom(new_y, new_x, location)

    return location

def isBlocked(y, x, direction):
    return castle[y][x] & walls[direction]

def calculateMaxRoomSizeWithoutOneWall():
    max_room_size_without_one_wall = 0

    for room1, room2 in combinations(rooms, 2):
        if max_room_size_without_one_wall >= room1['size'] + room2['size']: # 하나의 벽을 제거하여 가장 큰 방이 될 수 있는지 계산할 필요 없음
            continue

        if isNearbyRooms(room1['location'], room2['location']):
            max_room_size_without_one_wall = room1['size'] + room2['size']

    return max_room_size_without_one_wall

def isNearbyRooms(location1, location2):
    for y1, x1 in location1:
        for y2, x2 in location2:
            if abs(y1 - y2) + abs(x1 - x2) == 1:
                return True

    return False

number_of_column, number_of_row = map(int, stdin.readline().strip().split())
castle = [list(map(int, stdin.readline().strip().split())) for _ in range(number_of_row)]
visited = initializeVisited()
rooms = getRoomInformation()
max_room_size_without_one_wall = calculateMaxRoomSizeWithoutOneWall()

print(len(rooms))
print(max(map(lambda room: room['size'], rooms)))
print(max_room_size_without_one_wall)

