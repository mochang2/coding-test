"""
20221104
골드4 불!
url: https://www.acmicpc.net/problem/4179
후기: 간단한 bfs 문제다.
새롭게 읽기 쉬운 코드를 시도해봤다.

1. 함수에 인자가 2개 이하로
2. 함수는 하나의 역할만

다만 이렇게 하니까 입력받는 maze, row_count, column_count가 거의 모든 함수에서 전역적으로 사용되는 단점이 있었다.
또 다른 방법이 있나 계속해서 고민해봐야겠다.


문제는 다음과 같이 풀었다.

1. 이동할 수 있는 위치가 maze의 가장자리면 time + 1을 return한다.
2. 매 시간마다 새롭게 번지는 불의 위치를 구하고, 해당 위치를 maze에 표시한다.
3. 매 시간마다 진수가 이동할 수 있는 위치를 구한다.
4. 만약 진수가 이동할 수 있는 위치가 없다면 IMPOSSIBLE를 return한다.

위 풀이에서 2, 3번 순서를 바꿔서 했더니 처음에는 틀렸다.
다음과 같은 반례가 있었기 때문이다.

4 6
######
......
#.J###
#F####

답은 5지만, 불이 먼저 번지지 않고 진수가 먼저 이동하면 4라는 오답이 나온다.
"""

import sys

input_ = sys.stdin.readline

def getPositions(target):
    global maze, row_count, column_count
    
    positions = []

    for y in range(row_count):
        for x in range(column_count):
            if maze[y][x] == target:
                positions.append((y, x))

    return positions

def initializeVisited():
    global row_count, column_count
    
    return [[False for _ in range(column_count)] for __ in range(row_count)]

def reachedBorder(positions):
    global row_count, column_count
    
    for y, x in positions:
        if y == 0 or y == row_count - 1 or x == 0 or x == column_count - 1:
            return True

    return False

def isOutOfRange(y, x):
    global row_count, column_count
    
    return not 0 <= y < row_count or not 0 <= x < column_count

def getMovablePositions(positions, visited):
    global dy, dx, maze
    
    new_positions = []

    for y, x in positions:
        for direction in range(4):
            new_y, new_x = y + dy[direction], x + dx[direction]

            if isOutOfRange(new_y, new_x) or \
               visited[new_y][new_x] or \
               maze[new_y][new_x] in ('F', '#'): # 미로를 벗어나거나 이미 방문했거나 불이 났거나 벽이면
                continue

            visited[new_y][new_x] = True

            new_positions.append((new_y, new_x))

    return new_positions

def getFiredPositions(positions):
    global dy, dx, maze
    
    new_positions = []

    for y, x in positions:
        for direction in range(4):
            new_y, new_x = y + dy[direction], x + dx[direction]

            if isOutOfRange(new_y, new_x) or \
               maze[new_y][new_x] in ('F', '#'): # 미로를 벗어나거나 이미 방문했거나 불이 났거나 벽이면
                continue

            new_positions.append((new_y, new_x))
            maze[new_y][new_x] = 'F'

    return new_positions

def getShortestEscapeTime():    
    movable_positions = getPositions('J')
    fired_positions = getPositions('F')
    visited = initializeVisited()
    time = 0

    while len(movable_positions) != 0:
        if reachedBorder(movable_positions):
            return time + 1

        fired_positions =  getFiredPositions(fired_positions)
        movable_positions = getMovablePositions(movable_positions, visited)
    
        time += 1

    return 'IMPOSSIBLE'

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

row_count, column_count = map(int, input_().strip().split())
maze = [list(input_().strip()) for _ in range(row_count)]
shortest_escape_time = getShortestEscapeTime()

print(shortest_escape_time)

