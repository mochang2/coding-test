"""
20230410
실버2 유기농 배추
url: https://www.acmicpc.net/problem/1012
후기: 어려울 것도, 고민할 것도 없는 dfs/bfs 완탐 문제다.
서로 연결된 배추들의 그룹이 몇 개인지 파악하면 되는 문제다.
처음 제출 때 recursion error가 났는데 2500이 아니라 2501 이상으로 해야 됐나 보다.
"""

from sys import stdin, setrecursionlimit

setrecursionlimit(50 ** 2)

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def getInput():
    number_of_column, number_of_row, cabage_count = map(int, stdin.readline().strip().split())
    visited = initializeMatrix(number_of_row, number_of_column)
    ground = initializeMatrix(number_of_row, number_of_column)

    for _ in range(cabage_count):
        column, row = map(int, stdin.readline().strip().split())
        ground[row][column] = 1

    return visited, ground

def initializeMatrix(number_of_row, number_of_column):
    return [[0 for _ in range(number_of_column)] for __ in range(number_of_row)]

def findAdjacentCabages(visited, ground, row, column):
    for direction in range(4):
        new_row, new_column = row + dy[direction], column + dx[direction]

        if isOutOfRange(new_row, new_column, len(visited), len(visited[0])) or \
           visited[new_row][new_column] == 1 or \
           ground[new_row][new_column] == 0:
            continue

        visited[new_row][new_column] = 1
        findAdjacentCabages(visited, ground, new_row, new_column)

def isOutOfRange(row, column, number_of_row, number_of_column):
    return not 0 <= row < number_of_row or not 0 <= column < number_of_column

case_count = int(stdin.readline().strip())
for _ in range(case_count):
    visited, ground = getInput()
    earthworm_count = 0

    for row in range(len(visited)):
        for column in range(len(visited[0])):
            if visited[row][column] == 1 or ground[row][column] == 0:
                continue

            earthworm_count += 1
            findAdjacentCabages(visited, ground, row, column)

    print(earthworm_count)
