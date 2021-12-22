"""
211124
2021 Dev-Matching: 웹 백엔드 개발
url: https://programmers.co.kr/learn/courses/30/lessons/77485
후기: 빡구현. 계속하다 보면 2차원 배열이 익숙해질듯. 귀찮더라도 grid 자체를 copy하기 보다는 제자리에서 바꾸는 게 효율성에서는 좋다.
"""

def solution(rows, columns, queries):
    answer = []
    grid = [[i + 1 for i in range(columns * (j - 1), columns * j)] for j in range(1, rows + 1)]
    
    for query in queries:
        min_value = 10001
        
        # grid 자체를 copy하면 효율성 시간 초과가 나므로, 제자리에서 바꿔줌
        tmp_for_first = grid[query[0] - 1][query[1] - 1]
        
        # 왼변에 있는 것들 한 칸 위로
        for x in range(query[0], query[2]):
            min_value = min(min_value, grid[x][query[1] - 1])
            grid[x - 1][query[1] - 1] = grid[x][query[1] - 1]
        
        # 아랫변에 있는 것들 한 칸 왼쪽으로
        for y in range(query[1], query[3]):
            min_value = min(min_value, grid[query[2] - 1][y])
            grid[query[2] - 1][y - 1] = grid[query[2] - 1][y]
        
        # 오른변에 있는 것들 한 칸 아래로
        for x in range(query[2] - 1, query[0] - 1, -1):
            min_value = min(min_value, grid[x - 1][query[3] - 1])
            grid[x][query[3] - 1] = grid[x - 1][query[3] - 1]
        
        # 윗변에 있는 것들 한 칸 오른쪽으로
        for y in range(query[3] - 1, query[1] - 1, -1):
            min_value = min(min_value, grid[query[0] - 1][y - 1])
            grid[query[0] - 1][y] = grid[query[0] - 1][y - 1]
        
        # 처음에 따로 빼둔 (x1, y1)에 있는 수
        min_value = min(min_value, tmp_for_first)
        grid[query[0] - 1][query[1]] = tmp_for_first
        
        answer.append(min_value)
    
    return answer
