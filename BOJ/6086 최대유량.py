"""
20221208
골드4 최대 유량
url: https://www.acmicpc.net/problem/6086
후기: 최대 유량 문제였다.

https://www.youtube.com/watch?v=Wn51_ypG_T8
https://www.youtube.com/watch?v=BQ0Yq-sufnk
https://roamingman.tistory.com/39

위 풀이들을 보고 이해했다.

간단히 정리만 하자면 capacity: A -> B로 보낼 수 있는 최대 유량, flow: A -> B로 보낸 실제 유량이다.
다만 'A -> B로 양의 유량을 보낸다면 반대로 B -> A는 음의 유량을 보낸 것과 마찬가지이다'라는 전제에서
시작해 숨은 route를 찾는 알고리즘이다.
보통 BFS로 푸는데 DFS가 일반적으로는 더 느리기 때문이다.

풀이 과정은 다음과 같다.
1. 입력을 초기화한다. 여기서 주의할 것은 이 문제는 양방향 그래프라는 점이다(요거 때문에 많이 틀렸다).
   directions[from_][to]로 from_에서 to로 유량을 보내는 데에 필요한 정보를 담고 있다.
2. 보낼 수 있는 길을 찾는다. froms[to] = from_은 from_ -> to로 가는 길을 찾았다는 의미이다.
3. A -> Z까지의 길 중 최대로 감당 가능한 유량을 흘려보낸다.
4. 보낸 유량을 더한다.
5. 보낼 수 있는 길이 없을 때까지 2부터 반복한다.
"""

from sys import stdin
from copy import deepcopy

MAX_FLOW_AMOUNT = 1001
SOURCE_DRAIN = 'A'
SINK_DRAIN = 'Z'

class Direction(dict):
    def __init__(self):
        self.default = {
            'capacity': 0,
            'flow': 0
        }
        
    def initializeKey(self, from_, to):
        if from_ not in self.keys():
            self[from_] = dict()

        if to not in self[from_].keys():
            self[from_][to] = deepcopy(self.default)

        if to not in self.keys():
            self[to] = dict()

        if from_ not in self[to].keys():
            self[to][from_] = deepcopy(self.default)

def initializeInputs():
    input_ = stdin.readline
    directions = Direction()

    number_of_drains = int(input_().strip())
    for _ in range(number_of_drains):
        from_, to, capacity = input_().strip().split(' ')
        directions.initializeKey(from_, to)

        directions[from_][to]['capacity'] += int(capacity)
        directions[to][from_]['capacity'] += int(capacity)

    return directions

def initializeFroms(drains):
    froms = dict()

    for drain in drains:
        froms[drain] = None

    return froms

def findRoute(): # bfs
    global directions, SOURCE_DRAIN, SINK_DRAIN
    
    froms = initializeFroms(directions.keys())
    queue = [SOURCE_DRAIN]

    while queue:
        from_ = queue.pop()

        for to in directions[from_].keys():
            can_flow = directions[from_][to]['capacity'] > directions[from_][to]['flow']
            not_visited = froms[to] == None
            if can_flow and not_visited:
                froms[to] = from_ # check visited
                queue.append(to)

    return froms

def calculateMinFlow(froms):
    global MAX_FLOW_AMOUNT, SOURCE_DRAIN, SINK_DRAIN, directions

    min_flow = MAX_FLOW_AMOUNT
    drain = SINK_DRAIN

    while drain != SOURCE_DRAIN:
        capacity = directions[froms[drain]][drain]['capacity']
        current_flow = directions[froms[drain]][drain]['flow']
        
        min_flow = min(min_flow, capacity - current_flow)
        drain = froms[drain]

    return min_flow

def flow(froms, amount):
    global SOURCE_DRAIN, SINK_DRAIN, directions

    drain = SINK_DRAIN

    while drain != SOURCE_DRAIN:
        directions[froms[drain]][drain]['flow'] += amount
        directions[drain][froms[drain]]['flow'] -= amount

        drain = froms[drain]

total_flow_amount = 0
directions = initializeInputs() # { from: { to: { capacity: int, flow: int } } }

while True:
    froms = findRoute()
    cannot_flow = froms[SINK_DRAIN] == None
    if cannot_flow:
        break
    
    min_flow = calculateMinFlow(froms)
    flow(froms, min_flow)
    total_flow_amount += min_flow

# print answer
print(total_flow_amount)
