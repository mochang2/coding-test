"""
플래5 어항 정리
url: https://www.acmicpc.net/problem/23291
후기: 이번에도 빡구현이다. 첫 플래 문제를 내 손으로 풀어서 뿌듯하다.
2차원에서 표현하므로 2차원 배열 사용했다.
배열의 끝에 추가하는 것이 아닌, 위나 왼쪽에도 추가하므로 deque을 사용했다.
deque을 사용한다고 생각한 시점에서 효율성은 통과할 것이라는 느낌이 들었다.
개인적으로는 두 번쨰 단계가 제일 어려웠던 것 같다.
그리고 AjdustFish는 23289번 온풍기 온도 조절하는 부분을 작성했던 부분이 생각나서 쉽게 풀었다.
"""

# 예제 틀렸던 포인트
# 1. 처음에 matrix의 행의 길이를 N // 2로 선언함. 굳이 그럴 이유가 없음.
# 2. 다섯 번째 단계인 4층으로 쌓는 부분에서 appendleft -> append -> appendleft로 쌓아야 함.

import sys
from collections import deque

def PrintMatrix(matrix):
    for i in range(N):
        print(matrix[i])
    print()

def PileAndRotate():
    global matrix, N
    while True:
        max_height = 0
        for i in range(N):
            if matrix[i] != deque([]):
                max_height += 1
        num_of_one_floor = len(matrix[-1]) - len(matrix[-2])
        if max_height > num_of_one_floor: # pile 중단 조건. 1층만 존재하는 어항들보다 어항 최대 높이가 더 크면.
            return

        tmp_matrix = [] # 임시로 deque을 저장하기 위함.
        for _ in range((N - num_of_one_floor) // max_height): # pile(pop -> append) 해야 되는 횟수
            queue = deque([])
            for i in range(N - max_height, N):
                queue.appendleft(matrix[i].popleft())
            tmp_matrix.append(queue)

        for i, queue in enumerate(tmp_matrix): # tmp_matrix를 matrix에 update
            matrix[i + N - len(tmp_matrix) - 1] = queue

def AdjustFish():
    global matrix, N
    result = []
    for i in range(N):
        result.append(deque([0 for _ in range(len(matrix[i]))]))

    for i in range(N):
        if matrix[i] == deque([]):
            continue

        for j in range(len(matrix[i])):
            for direction in range(2): # 0: 오른쪽, 1: 아래
                comparer_y = i + dy[direction]
                comparer_x = j + dx[direction]
                if comparer_y == N or comparer_x == len(matrix[i]):
                    continue

                difference = abs(matrix[i][j] - matrix[comparer_y][comparer_x]) // 5
                if matrix[i][j] > matrix[comparer_y][comparer_x]:
                    result[i][j] -= difference
                    result[comparer_y][comparer_x] += difference
                elif matrix[i][j] < matrix[comparer_y][comparer_x]:
                    result[i][j] += difference
                    result[comparer_y][comparer_x] -= difference
                # 같을 때는 조정이 필요없음.

    return result

def MakeOneLayer():
    global matrix, N
    queue = deque([]) # 꺼내는 어항들을 저장하기 위함
    while matrix[-1] != deque([]):
        for i in range(N - 1, -1, -1):
            if matrix[i] != deque([]):
                queue.append(matrix[i].popleft())
    matrix[-1] = queue
    
def PileFourLayer():
    global matrix, N
    for i in range(N // 4):
        matrix[-2].appendleft(matrix[-1].popleft())
    for i in range(N // 4):
        matrix[-3].append(matrix[-1].popleft()) # 이 부분을 착각해서 답을 보고 앎
    for i in range(N // 4):
        matrix[-4].appendleft(matrix[-1].popleft())
    
# initialization
dy = [0, 1]
dx = [1, 0]
N, K = map(int, sys.stdin.readline().strip().split())
matrix = [deque([]) for _ in range(N)]
matrix[-1] = deque(map(int, sys.stdin.readline().strip().split()))
answer = 0

while True:
    max_ = max(matrix[-1])
    min_ = min(matrix[-1])
    if max_ - min_  <= K:
        break
    
    # 1. 제일 작은 어항들에 물고기 1개씩 추가
    for i in range(N):
        if matrix[-1][i] == min_:
            matrix[-1][i] += 1

    # 2. 쌓으면서 90도 시계 방향으로 회전
    matrix[-2].append(matrix[-1].popleft())
    PileAndRotate()
    
    # 3. 첫 번째 물고기 조절
    delta_matrix = AdjustFish()
    for i in range(N):
        for j in range(len(matrix[i])):
            matrix[i][j] += delta_matrix[i][j]
    
    # 4. 첫 번째 바닥에 일렬로 놓기
    MakeOneLayer()
    
    # 5. 어항 다시 쌓기(두 단계 거치지 않고 한 번에 쌓기)
    PileFourLayer()
    
    # 6. 두 번째 물고기 조절
    delta_matrix = AdjustFish()
    for i in range(N):
        for j in range(len(matrix[i])):
            matrix[i][j] += delta_matrix[i][j]
    
    # 7. 두 번째 바닥에 일렬로 놓기
    MakeOneLayer()

    answer += 1

print(answer)

