"""
20230324
골드3 백양로 브레이크
url: https://www.acmicpc.net/problem/11562
후기: 플로이드 와샬이라는 문제를 몰랐으면 평생 못 풀었을 것 같다.
플로이드 와샬의 새로운 해석이라고 생각되는 문제다.
(음... 그리고 모든 점을 시작점으로 다익스트라를 사용하면 문제 해결이 가능할 거 같지만 문제 분류에 없는 거 보니까 안 되겠지싶다)

플로이드 와샬은 기본적으로 모든 점에서 다른 모든 점으로의 비용을 구하는 알고리즘으로 O(N^3)의 시간복잡도를 가진다.
처음 비용 설정을 할 때 A->B를 한 번에 갈 수 있으면 0, 없으면 1로 설정한다.
이 의미는 양방향 도로를 뚫지 않아도 A->B를 갈 수 있으면 0, 양방향 도로를 뚫어야 A->B를 갈 수 있다면 1로 한다는 뜻이다.
이후에 플로이드 와샬 알고리즘을 이용하면, 비용_matrix[from_][to]는 from_에서 to로 가기 위해 필요한 양방향 도로의 개수를 의미하게 된다.
"""

from sys import stdin

BIDIRECTIONAL = 0
UNIDIRECTIONAL = 1
INF = 1000

def initializeCosts():
    number_of_buildings, number_of_roads = map(int, stdin.readline().strip().split())
    costs = [[INF for _ in range(number_of_buildings)] for __ in range(number_of_buildings)]

    for building in range(number_of_buildings):
        costs[building][building] = 0

    for _ in range(number_of_roads):
        from_, to, is_bidirectional = map(int, stdin.readline().strip().split())
        from_ -= 1
        to -= 1

        costs[from_][to] = BIDIRECTIONAL
        if is_bidirectional:
            costs[to][from_] = BIDIRECTIONAL
        else:
            costs[to][from_] = UNIDIRECTIONAL

    return costs

def calculateShortestPaths(costs): # 플로이드 와샬
    for intermediate in range(len(costs)):
        for start in range(len(costs)):
            for end in range(len(costs)):
                if start == end:
                    continue
                
                costs[start][end] = min(costs[start][end], costs[start][intermediate] + costs[intermediate][end])

def answerToQuestions(costs):
    number_of_questions = int(stdin.readline().strip())
    
    for _ in range(number_of_questions):
        from_, to = map(int, stdin.readline().strip().split())
        from_ -= 1
        to -= 1

        print(costs[from_][to])

costs = initializeCosts()
calculateShortestPaths(costs)
answerToQuestions(costs)
