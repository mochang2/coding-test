"""
221019
url: https://school.programmers.co.kr/learn/courses/30/lessons/118669
후기: 자력으로 못 풀고 접근법, 시간 초과 해결법 이렇게 두 번이나 힌트를 얻어야 했다.
union-find로 풀었다는 사람도 있다는데 나는 다익스트라를 이용했다.

문제에서 중요한 부분은 '등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 함'이다.

아이디어는 다음과 같다.
1. start -> end로 가는 편도만 구하면, end -> start는 그 길 그대로 거꾸로 오기면 하면 되므로 편도만 구한다.
2. 어떤 start였는지 중요하지 않다. 따라서 모든 start를 다익스트라하기 전 우선 순위 큐에 전부 넣는다.
3. 특정 vertex까지 가는 cost를 list로 관리한다. 그 cost보다 높은 intensity를 통해서 해당 vertex에 도착한다면 그 경로는 무시한다.
"""

# 첫 번재 시도
# 25번 TC 시간 초과
# heappush, heappop 최소화하기 위해 여러 조건문을 변경했지만 실패했다.
# for gate in gates: 조건에서 모든 시작 지점을 각각 구분하여 반복문을 돌려준 부분이 문제였다.

import heapq as h

def getIsSummit(n, summits):
    is_summit = [False for _ in range(n + 1)]

    for summit in summits:
        is_summit[summit] = True

    return is_summit

def getIsGate(n, gates):
    is_gate = [False for _ in range(n + 1)]

    for gate in gates:
        is_gate[gate] = True

    return is_gate

def getCosts(n, paths, is_gate):
    costs = [[] for _ in range(n + 1)]

    for vertex1, vertex2, cost in paths: # 목적지가 gate인 것에 대해서는 관심 없음
        if not is_gate[vertex1]:
            costs[vertex2].append([cost, vertex1])
        if not is_gate[vertex2]:
            costs[vertex1].append([cost, vertex2])       

    return costs

def getVisited(n):
    return [False for _ in range(n + 1)]

def solution(n, paths, gates, summits):
    answer = [n + 1, 10000000] # [summit, max intensity]
    is_summit = getIsSummit(n, summits)
    is_gate = getIsGate(n, gates)
    costs = getCosts(n, paths, is_gate)

    for gate in gates:
        queue = costs[gate] # [cost, 목적지][]
        h.heapify(queue) # 최소 비용으로 갈 수 있는 vertex부터 방문하기 위해
        
        max_intensity = 0
        visited = getVisited(n)
        visited[gate] = True

        while queue: # 가망이 없는 지점은 이미 queue에 넣지 않기 때문에 summit 도착하지 않고 종료할 수도 있음
            cost, next_vertex = h.heappop(queue)
            max_intensity = max(cost, max_intensity)

            if is_summit[next_vertex]: # gate에서 최소의 intensity로 도착할 수 있는 summit(next_vertex)
                if max_intensity < answer[1] or \
                   (max_intensity == answer[1] and next_vertex < answer[0]):
                    answer = [next_vertex, max_intensity]
                break

            visited[next_vertex] = True
            
            for cost, adjacent in costs[next_vertex]:
                if not visited[adjacent] and cost <= answer[1]: # 이미 더 낮은 비용으로 갈 수 있는 방법 존재한다면 pass
                    h.heappush(queue, [cost, adjacent])
    
    return answer



# 두 번째 시도
# 정답

