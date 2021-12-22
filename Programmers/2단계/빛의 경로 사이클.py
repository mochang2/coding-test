"""
211108
월간 코드 챌린지 시즌3
url: https://programmers.co.kr/learn/courses/30/lessons/86052
후기1. 좌표와 방향을 잘 기억해야 함(3차원 배열 필요)
2. 한 번 지나간 길을 또 지나려 하는 것을 막아야 시간 초과가 발생하지 않음.
"""

def solution(grid):
    # 한 격자에서 같은 방향으로 지나갔으면 해당 두 route는 같은 경로 사이클임
    answer = []
    num_of_row = len(grid)
    num_of_column = len(grid[0])
    check_if_passed = [[[0,0,0,0] for _ in range(num_of_column)] for __ in range(num_of_row)] # 어디로 쐈는지

    for i in range(num_of_row):
        y_axis = i
        for j in range(num_of_column):
            x_axis = j
            for k in range(4): #[0]: 위, [1]: 오른쪽, [2]: 아래, [3]: 왼쪽
                if check_if_passed[i][j][k] != 0:  # 시작지점이 이미 경로에 포함된 것
                    continue
                
                check_if_passed[i][j][k] = 1  # 시작 지점 체크
                direction = k
                count = 1
                while True: # 지나간 경로인지 체크
                    # 격자 이동
                    # print(grid[y_axis][x_axis], check_if_passed)
                    if direction == 0:
                        y_axis = (y_axis - 1) % num_of_row
                    elif direction == 1:
                        x_axis = (x_axis + 1) % num_of_column
                    elif direction == 2:
                        y_axis = (y_axis + 1) % num_of_row
                    else: #direction == 3:
                        x_axis = (x_axis - 1) % num_of_column

                    # 방향 체크
                    if grid[y_axis][x_axis] == "S":
                        pass # direction = direction
                    elif grid[y_axis][x_axis] == "L":
                        direction = (direction + 3) % 4
                        """
                        if direction == 0:
                            direction = 3
                        elif direction == 1:
                            direction = 0
                        elif direction == 2:
                            direction = 1
                        else: #direction == 3:
                            direction = 2
                        """
                    else: # grid[y_axis][x_axis] == "R"
                        direction = (direction + 1) % 4
                        """
                        if direction == 0:
                            direction = 1
                        elif direction == 1:
                            direction = 2
                        elif direction == 2:
                            direction = 3
                        else: #direction == 3:
                            direction = 0
                        """

                    if check_if_passed[y_axis][x_axis][direction] != 0:  # 이미 계산된 경로
                        break
                    else: #check_if_passed[y_axis][x_axis][direction] == 0
                        check_if_passed[y_axis][x_axis][direction] = 1
                        count += 1
                        
                answer.append(count)
                
    return sorted(answer)


# 시간초과 발생. 500 * 500 * 4 * count 수만큼이니까 100만을 넘어감
def solution(grid):
    answer = []
    num_of_row = len(grid)
    num_of_column = len(grid[0])
    
    for i in range(num_of_row): # 격자 선택
        for j in range(num_of_column):
            for k in range(4): # 빛을 쏠 방향 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
                route = [[i, j, k]] # 이동한 경로. 현재 위치와 방향만 추가해서 초기화
                
                while True:
                    if route[-1][2] == 0: # 이전 단계에서 위로 쐈다
                        y_axis = (route[-1][0] - 1) % num_of_row
                        x_axis = route[-1][1]
                        if grid[y_axis][x_axis] == "S":
                            direction = 0
                        elif grid[y_axis][x_axis] == "L":
                            direction = 3
                        else: # grid[y_axis][x_axis] == "R":
                            direction = 1
                        next_route = [y_axis, x_axis, direction]
                        
                    elif route[-1][2] == 1: # 이전 단계에서 오른쪽으로 쐈다
                        y_axis = route[-1][0]
                        x_axis = (route[-1][1] + 1) % num_of_column
                        if grid[y_axis][x_axis] == "S":
                            direction = 1
                        elif grid[y_axis][x_axis] == "L":
                            direction = 0
                        else: # grid[y_axis][x_axis] == "R":
                            direction = 2
                        next_route = [y_axis, x_axis, direction]
                        
                    elif route[-1][2] == 2: # 이전 단계에서 아래로 쐈다
                        y_axis = (route[-1][0] + 1) % num_of_row
                        x_axis = route[-1][1]
                        if grid[y_axis][x_axis] == "S":
                            direction = 2
                        elif grid[y_axis][x_axis] == "L":
                            direction = 1
                        else: # grid[y_axis][x_axis] == "R":
                            direction = 3
                        next_route = [y_axis, x_axis, direction]
                        
                    else: # 이전 단계에서 왼쪽으로 쐈다
                        y_axis =route[-1][0]
                        x_axis = (route[-1][1] - 1) % num_of_column
                        if grid[y_axis][x_axis] == "S":
                            direction = 3
                        elif grid[y_axis][x_axis] == "L":
                            direction = 2
                        else: # grid[y_axis][x_axis] == "R":
                            direction = 0
                        next_route = [y_axis, x_axis, direction]
                    
                    if route[0] == next_route:
                        # route[0] == route[-1]면 정지
                        answer.append(len(route))
                        break
                    else:
                        route.append(next_route)
                    
            # 마지막에 같은 경로인지 아닌지 확인해야 하는데... 이걸 어찌할까
                
    return sorted(answer)
