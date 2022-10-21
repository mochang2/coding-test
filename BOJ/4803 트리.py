"""
20221021
골드4 트리
url: https://www.acmicpc.net/problem/4803
후기: 오랜만에 기분 좋게 한 번에 통과했다.
트리가 무엇인가 고민하다가 생각해보니 MST도 트리의 일부였다.
문제에 나온 설명을 참고해보니 n개의 vertex에서 n - 1개의 edge만 있으면 트리가 된다는 결론을 얻었다.

다음과 같이 풀었다.
1번부터 n번까지의 vertex까지 방문되지 않은 지점을 start 지점(변수명: vertex)을 정한다.
인접한 vertex 중 방문하지 않은 vertex을 bfs로 방문한 뒤 해당 vertex에게 연결된 edge의 개수를 파악한다.
해당 순회를 통해 찾은 vertex의 개수와 edge의 개수가 트리의 조건에 맞는지 확인한다.
맞으면 tree += 1한다.
"""

import sys
from collections import deque

input_ = sys.stdin.readline

def initVisited(n):
    return [False for _ in range(n + 1)]

def getAdjacents(n, edges):
    adjacents = [[] for _ in range(n + 1)]

    for vertex1, vertex2 in edges:
        adjacents[vertex1].append(vertex2)
        adjacents[vertex2].append(vertex1)

    return adjacents

def countTree(n, edges):
    tree = 0
    visited = initVisited(n)
    adjacents = getAdjacents(n, edges) # 인접한 vertex 정보를 나타내기 위해 input 변환
    
    for vertex in range(1, n + 1): # vertex: bfs 시작 지점
        if visited[vertex]:
            continue

        queue = deque([vertex])
        visited[vertex] = True
        num_of_edges = len(adjacents[vertex])
        num_of_vertexes = 1
        
        while queue: # 붙어 있는 모든 vertex를 확인할 때까지
            next_vertex = queue.popleft()

            for adjacent in adjacents[next_vertex]:
                if visited[adjacent]:
                    continue

                visited[adjacent] = True
                num_of_edges += len(adjacents[adjacent])
                num_of_vertexes += 1
                queue.append(adjacent)

        if 2 * (num_of_vertexes - 1) == num_of_edges: # tree의 조건인지 확인
            tree += 1

    return tree

case = 1

while True:
    n, m = map(int, input_().strip().split())

    if n == 0 and m == 0: # 프로그램 종료 조건
        sys.exit(0)

    edges = [tuple(map(int, input_().strip().split())) for _ in range(m)]
    tree = countTree(n, edges) # 해당 그래프에서의 트리 개수

    if tree == 0:
        print('Case {}: No trees.'.format(case))
    elif tree == 1:
        print('Case {}: There is one tree.'.format(case))
    elif tree >= 2:
        print('Case {}: A forest of {} trees.'.format(case, tree))

    case += 1
