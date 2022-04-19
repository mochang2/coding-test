"""
20220312
골드5 강의실 배정
url: https://www.acmicpc.net/problem/14500
후기: 노가다 문제였다. 다만 이게 노가다 문제인지 확신이 필요해서 계산을 해보니 1억번 이내로 충분한 계산이었다.
가로 500, 세로 500, 계산해야 되는 모양 19, 최대 4번의 덧셈 연산이므로 충분했다.
좌표 실수가 잦아 https://www.acmicpc.net/board/view/61597 와 https://www.acmicpc.net/board/view/81456의 테스트 케이스 도움을 받았다.
그리고 굳이 traverse 함수에 flag를 선언하지 않았어도 답이 바뀌진 않았을 거 같다.
"""

import sys

movements = {
    "I": [((0,1), (0,2), (0,3)),
          ((1,0), (2,0), (3,0))],
    "ㅁ": [((1,0), (0,1), (1,1))],
    "ㄴ": [((1,0), (2,0), (2,1)),
          ((0,1), (0,2), (-1,2)),
          ((-1,0), (-2,0), (-2,-1)),
          ((0,-1), (0,-2), (1,-2)),
          ((1,0), (2,0), (2,-1)),
          ((0,-1), (0,-2), (-1,-2)),
          ((-1,0), (-2,0), (-2,1)),
          ((0,1), (0,2), (1,2))],
    "ㅗ": [((0,1), (0,2), (-1,1)),
          ((1,0), (2,0), (1,1)),
          ((0,1), (0,2), (1,1)),
          ((1,0), (2,0), (1,-1))],
    "Z": [((1, 0), (1, 1), (2, 1)),
          ((0, 1), (-1, 1), (-1, 2)),
          ((1, 0), (1, -1), (2, -1)),
          ((0, 1), (1, 1), (1, 2))]
}

def traverse(y, x):
    global paper, movements, N, M, answer
    flag = True
    
    for keys in movements.keys():
        for values in movements[keys]:
            sum_ = paper[y][x]
            for value in values:
                new_y = y + value[0]
                new_x = x + value[1]
                if not 0 <= new_y < N or not 0 <= new_x < M:
                    flag = False
                    break
                sum_ += paper[new_y][new_x]
            if flag:
                answer = max(answer, sum_)
            sum_ = 0
            flag = True
        

N, M = map(int, sys.stdin.readline().strip().split())
paper = []
answer = 0
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    for j in range(M):
        traverse(i, j)

print(answer)
