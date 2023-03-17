"""
20220315
골드3 파티
url: https://www.acmicpc.net/problem/1238
후기: 다익스트라 문제이다.
처음에는 모든 점에서 모든 점으로 가는 cost를 구해야 된다고 생각했다.
그래서 간단히 플로이드 와샬 알고리즘을 생각했다.
하지만 N이 1000이라서 시간 초과가 날 거 같아 시도하지 않았다.

그 이후에 생각한 것이 다익스트라였다.
다익스트라 알고리즘의 시간복잡도는 N log N이므로 모든 점을 시작점으로 다익스트라 알고리즘을 구현하면 N ^ 2 log N이므로 시간 초과를 피할 수 있었다.
이 방법으로 처음에 통과했다.
하지만 간당간당하게 통과해서 다른 방법이 없나 찾아봤다.

간단한 해결방법이 있었다.
이 문제는 단방향 가중치만 있기 때문에 할 수 있는 색다른 풀이였다.
처음에 입력받은 costs를 기준으로 파티가 열리는 지점에서 다른 모든 지점으로 다익스트라 알고리즘을 통해 최소 비용을 계산한다.
그리고 해당 costs를 반대로 기록한 reverse_costs(시작점과 도착점이 반대임)를 기준으로
다시 파티가 열리는 지점에서 다른 모든 지점으로 다익스트라 알고리즘을 계산한다.
이는 다른 모든 지점에서 파티가 열리는 지점으로 갈 수 있는 최소 비용을 계산하는 것이다.
이 방법은 시간복잡도는 N log N으로 훨씬 짧은 시간에 문제를 풀 수 있었다.
"""

## 첫 번째 시도
## 정답. pypy 3752ms

from sys import stdin
import heapq as h

INF = 10000 * 1000

def getInput():
    global INF
    
    number_of_towns, number_of_roads, town_throwing_party = map(int, stdin.readline().strip().split())
    costs = [[INF for _ in range(number_of_towns)] for __ in range(number_of_towns)]
    
    for _ in range(number_of_roads):
        from_, to, cost = map(int, stdin.readline().strip().split())
        costs[from_ - 1][to - 1] = cost

    return number_of_towns, town_throwing_party - 1, costs

def updateCost(start_town, costs): # 다익스트라
    global INF
    
    heap = [(start_town, 0)]
    cost = [INF for _ in range(len(costs))]
    cost[start_town] = 0

    while len(heap) != 0:
        current_town, current_cost = h.heappop(heap)

        for next_town in range(len(costs)):
            if current_town == next_town:
                continue

            next_cost = current_cost + costs[current_town][next_town]
            if next_cost < cost[next_town]: # 더 짧은 비용으로 가는 길이 존재한다면
                cost[next_town] = next_cost
                h.heappush(heap, (next_town, next_cost))
    costs[start_town] = cost

def getMaxRoundTripCost(costs, town_throwing_party):
    max_round_trip_cost = 0

    for town in range(len(costs)):
        if town == town_throwing_party:
            continue

        max_round_trip_cost = max(max_round_trip_cost, costs[town][town_throwing_party] + costs[town_throwing_party][town])

    return max_round_trip_cost

number_of_towns, town_throwing_party, costs = getInput()

for start_town in range(number_of_towns):
    updateCost(start_town, costs)

max_round_trip_cost = getMaxRoundTripCost(costs, town_throwing_party)
print(max_round_trip_cost)



## 두 번째 시도
## 정답 pypy 276ms

from sys import stdin
import heapq as h

INF = 10000 * 1000

def getInput():
    number_of_towns, number_of_roads, town_throwing_party = map(int, stdin.readline().strip().split())
    costs = initializeCosts(number_of_towns)
    reverse_costs = initializeCosts(number_of_towns)
    
    for _ in range(number_of_roads):
        from_, to, cost = map(int, stdin.readline().strip().split())
        costs[from_ - 1][to - 1] = cost
        reverse_costs[to - 1][from_ - 1] = cost

    return number_of_towns, town_throwing_party - 1, costs, reverse_costs

def initializeCosts(number_of_towns):
    global INF
    
    return [[INF for _ in range(number_of_towns)] for __ in range(number_of_towns)]

def calculateSmallestCost(start_town, costs): # 다익스트라
    global INF
    
    heap = [(start_town, 0)]
    cost = [INF for _ in range(len(costs))]
    cost[start_town] = 0

    while len(heap) != 0:
        current_town, current_cost = h.heappop(heap)

        for next_town in range(len(costs)):
            if current_town == next_town:
                continue

            next_cost = current_cost + costs[current_town][next_town]
            if next_cost < cost[next_town]: # 더 짧은 비용으로 가는 길이 존재한다면
                cost[next_town] = next_cost
                h.heappush(heap, (next_town, next_cost))

    return cost

def getMaxRoundTripCost(from_cost, to_cost):
    max_round_trip_cost = 0

    for town in range(len(from_cost)):
        max_round_trip_cost = max(max_round_trip_cost, from_cost[town] + to_cost[town])

    return max_round_trip_cost

number_of_towns, town_throwing_party, costs, reverse_costs = getInput()

from_town_throwing_party_cost = calculateSmallestCost(town_throwing_party, costs)
to_town_throwing_party_cost = calculateSmallestCost(town_throwing_party, reverse_costs)

print(getMaxRoundTripCost(from_town_throwing_party_cost, to_town_throwing_party_cost))
