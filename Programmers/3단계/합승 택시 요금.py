"""
220914
url: https://programmers.co.kr/learn/courses/30/lessons/42895
후기: 출발지는 거의 fake였고 중간에 어디서 헤어질지가 이 문제의 요점이었는데 해당 요점에 집중하니
모든 지점에서 다른 모든 지점으로의 cost를 요하는 문제다! 라고 생각이 들었다.

O(N^3) <= 200^3인 문제였다.
수가 작으니 당연히 완탐도 가능할 것이라 생각이 들었고 O(N^3)까지 가능한 완탐 알고리즘으로 플로이드 와샬이 생각나서 바로 해결됐다.
"""

MAX = 100000 * 200 * 200

def floydWarshal(n, fares = []):
    global MAX
    
    costs = [[MAX for _ in range(n)] for __ in range(n)]
    
    for i in range(n):
        costs[i][i] = 0 # 출발지 == 목적지
            
    for end_point1, end_point2, cost in fares:
        costs[end_point1 - 1][end_point2 - 1] = cost
        costs[end_point2 - 1][end_point1 - 1] = cost
    
    for k in range(n): 
        for i in range(n): # 출발지
            for j in range(n): # 목적지
                min_ = min(costs[i][j], costs[i][k] + costs[k][j])
                costs[i][j] = min_
                costs[j][i] = min_
    
    return costs
    

def solution(n, s, a, b, fares):
    global MAX
    
    answer = MAX
    costs = floydWarshal(n, fares)
    
    for intermediate in range(n):
        cost = costs[s - 1][intermediate] + costs[intermediate][a - 1] + costs[intermediate][b - 1]
        answer = min(answer, cost)
    
    return answer
  
  
