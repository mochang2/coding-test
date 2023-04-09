"""
20230409
실버2 친구
url: https://www.acmicpc.net/problem/1058
후기: 모든 노드에서 다른 모든 노드로의 거리를 구해야 하는 그래프 알고리즘이다.
N이 최대 50이어서 플로이드 와샬로 충분히 풀 수 있는 문제이지만,
N이 더 크다면 다익스트라를 이용하는 게 맞을 거 같아서 다익스트라를 이용해서 풀었다.

다음과 같이 풀었다.
1. 처음에 입력받은 내용이 Y이면 distance를 1로, N이면 INF로 설정한다.
2. 다익스트라로 모든 노드에서 다른 모든 노드로의 distance를 구한다.
3. distance가 1, 2이면 2-친구이므로 relations에서 distance가 1, 2인 개수를 구한다.
4. 3에서 구한 값 중 최댓값을 출력한다.
"""

from sys import stdin
from heapq import heappush, heappop

INF = 10000

def initialize():
    number_of_people = int(stdin.readline().strip())
    relations = [list(stdin.readline().strip()) for _ in range(number_of_people)]
    relations = [list(map(lambda is_friend: 1 if is_friend == 'Y' else INF, relation)) for relation in relations]

    return number_of_people, relations

def calculateRelationDistance(person): # 다익스트라
    relation_distance = [INF for _ in range(number_of_people)]
    relation_distance[person] = 0
    updated_relations = [(0, person)]

    while len(updated_relations) != 0:
        distance, current_person = heappop(updated_relations)

        if distance > relations[person][current_person]:
            continue

        for next_person in range(number_of_people):
            next_distance = distance + relations[current_person][next_person]
            has_shorter_distance = relation_distance[next_person] > next_distance
            
            if has_shorter_distance:
                relation_distance[next_person] = next_distance
                heappush(updated_relations, (next_distance, next_person))

    return relation_distance

def countSecondFriends():
    return [relation.count(1) + relation.count(2) for relation in relations]

number_of_people, relations = initialize()
for person in range(number_of_people):
    relations[person] = calculateRelationDistance(person)
second_friends_counts = countSecondFriends()
print(max(second_friends_counts))
