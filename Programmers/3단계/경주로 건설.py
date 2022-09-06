"""
220906
추석 트래픽
url: https://school.programmers.co.kr/learn/courses/30/lessons/67259
후기: dfs/dfs + dp 문제이다. 정확히는 점화식을 안 써서 dp인지는 모르겠지만 메모이제이션은 사용해야 된다.
처음에 메모이제이션을 사용하지 않고 단순히 완탐을 해서 시간초과가 났고 결국 답을 봤다.

routing이 필요한 알고리즘이라 dfs를 사용했고, 만약 도착한 지점이 기존에 도착했던 지점인데 더 싼 가격에 도착할 수 있었다고 판단하면 dfs를 종료했다.
cost라는 이차원 배열만 추가로 선언했으면 됐던 문제인데 아쉬웠다.
"""

answer = 0
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def calcCost(depth, corner_count):
    return (depth - 1) * 100 + corner_count * 500

def isOutOfRange(y, x, n):
    return not 0 <= y < n or not 0 <= x < n

def isCorner(y1, x1, y2, x2): # 이전 위치 좌표, 다음 위치 좌표 (현재 위치 좌표는 필요 없음)
    return abs(y1 - y2) == 1 and abs(x1 - x2) == 1

def dfs(y, x, corner_count, route, board, n, visited, cost):
    global answer
    
    current_cost = calcCost(len(route), corner_count)
    if cost[y][x] < current_cost:
        return
    cost[y][x] = current_cost
    
    if y == n - 1 and x == n - 1:
        answer = min(answer, current_cost)
        return
    
    for direction in range(4):
        new_y, new_x = y + dy[direction], x + dx[direction]
        
        if isOutOfRange(new_y, new_x, n) or visited[new_y][new_x] or board[new_y][new_x] == 1:
            continue
        
        # route와 corner_count 수정 필요
        if len(route) >= 2 and isCorner(route[-2][0], route[-2][1], new_y, new_x):
            corner_count += 1
        route.append((new_y, new_x))
        visited[new_y][new_x] = True
        
        dfs(new_y, new_x, corner_count, route, board, n, visited, cost)
        
        visited[new_y][new_x] = False
        route.pop()
        if len(route) >= 2 and isCorner(route[-2][0], route[-2][1], new_y, new_x):
            corner_count -= 1
    

def solution(board):
    global answer
    
    n = len(board)
    answer = 25 * 25 * 500 # max cost
    visited = [[False for _ in range(n)] for __ in range(n)]
    visited[0][0] = True
    cost = [[answer for _ in range(n)] for __ in range(n)] # 현재의 가격이 cost보다 크면 백트래킹을 종료
    dfs(0, 0, 0, [(0, 0)], board, n, visited, cost)
    
    return answer
  
