"""
230311
url: https://school.programmers.co.kr/learn/courses/30/lessons/150365#
후기: 백트래킹 문제다.

풀이는 간단하다.
visited 필요 없이 목적지까지 정확히 k번 이동으로 도달 가능한지 확인하면 된다.
하지만 일반적인 dfs와 달리 추가적으로 필요한 조건이 4가지가 있다.

1. DIRECTIONS를 사전 순으로 정의해야 한다.
   그래야 첫 번째로 찾은 route가 정답이다.
2. 도달 불가능 조건을 확인해야 한다.
   start point -> end point로 k번 안에 갈 수 있는지, 그리고 (end point와 start point 사이의 거리 - k)가 2의 배수인지 확인해야 한다.
3. 재귀 호출 깊이를 재조절해야 한다.
4. 백트래킹을 도는 내내 end point 도달 가능한지 확인해야 한다.
   그래야 시간 초과가 나지 않는다.
"""

DIRECTIONS = ['d', 'l', 'r', 'u']
DELTAS = [
    { 'y': 1,  'x': 0 },
    { 'y': 0,  'x': -1 },
    { 'y': 0,  'x': 1 },
    { 'y': -1, 'x': 0 }
]

def solution(number_of_y, number_of_x, start_y, start_x, end_y, end_x, route_length):
    import sys
    sys.setrecursionlimit(10 ** 6)
    
    if isImpossible(start_y, start_x, end_y, end_x, route_length):
        return 'impossible'
    
    answer = searchRoute(
        number_of_y,
        number_of_x,
        start_y, 
        start_x, 
        end_y, 
        end_x,
        route_length
    )
    
    return answer

def isImpossible(start_y, start_x, end_y, end_x, route_length):
    # k 안에 도달할 수 없는 거리 또는 최단거리로 목적지 도착 이후에 홀수 번만 더 움질 수 있다면
    distance = abs(start_y - end_y) + abs(start_x - end_x)
    
    return distance > route_length or (route_length - distance) % 2 == 1

def searchRoute(
        number_of_y,
        number_of_x,
        current_y, 
        current_x, 
        end_y, 
        end_x,
        route_length,
        current_route = ''
    ): 
    # 백트래킹
    global DELTAS, DIRECTIONS
    
    arrived = len(current_route) == route_length and current_y == end_y and current_x == end_x
    if arrived:
        return current_route
    
    if isImpossible(current_y, current_x, end_y, end_x, route_length - len(current_route)):
        # 중간마다 다시 확인: 현재 위치에서 목적지 도착 가능한지. 이게 없으면 시간 초과
        return
    
    for index, delta in enumerate(DELTAS):
        dy, dx = delta['y'], delta['x']
        new_y, new_x = current_y + dy, current_x + dx
        
        if isOutOfRange(number_of_y, number_of_x, new_y, new_x):
            continue
            
        searched_route = searchRoute(
            number_of_y,
            number_of_x,
            new_y, 
            new_x, 
            end_y, 
            end_x,
            route_length,
            current_route + DIRECTIONS[index]
        )
        
        if searched_route:
            return searched_route

def isOutOfRange(number_of_y, number_of_x, y, x):
    return not (0 < y <= number_of_y) or not (0 < x <= number_of_x)
