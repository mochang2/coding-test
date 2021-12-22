"""
211127
실버1 상어 초등학교
url: https://www.acmicpc.net/problem/21608
후기: 개빡구현. 그냥 알고리즘 알아서 푸는 것보다 훨씬 오랜 시간 걸린 것 같음. 그래도 디버깅 잘 하면 한 번에 풀 수 있었음.
"""

import sys
import math

def check(i, j, student_num, typeof):  # seat[i][j]의 상하좌우를 확인하여 조건에 맞는 것이 몇 개인지 개수 확인하는 함수
    global movements, seat, dic, N

    count = 0
    if typeof == "like":
        for movement in movements:
            if seat[i + movement[0]][j + movement[1]] in dic[student_num]:
                count +=1
    elif typeof == "empty":
        for movement in movements:
            row = i + movement[0]
            column = j + movement[1]
            if seat[row][column] == 0 and row != 0 and row != N + 1 and column != 0 and column != N + 1:
                # row, column이 1부터 N 사이일 때, 비어있으면
                count +=1
    return count


N = int(input())
seat = [[0 for _ in range(N + 2)] for __ in range(N + 2)]  # index: 0 ~ N+1, 실제 좌석은 1 ~ N
movements = [[-1,0], [0,1], [1,0], [0,-1]]

dic = dict() # key: value = 학생의 번호: 좋아하는 학생의 번호들
for i in range(N ** 2):
    li = list(map(int, sys.stdin.readline().strip().split()))
    dic[li[0]] = li[1:]
    
for student_num in dic.keys():
    max_like_count_in_adjacent = 0     # 주변에 좋아하는 학생 최대  몇 명인지
    store_axis_for_max_like_count = []  # 해당 좌표 저장하기 위한 리스트
    
    for i in range(1, N + 1): # row
        for j in range(1, N + 1): #column
            if seat[i][j] != 0:  # 좌석 주인이 이미 있다면 pass
                continue

            like_count = check(i, j, student_num, "like")      # 좌석 주인이 없다면 인접한 칸에 좋아하는 학생이 몇 명인지 셈
            if like_count > max_like_count_in_adjacent:
                max_like_count_in_adjacent = like_count
                store_axis_for_max_like_count.clear()            # 기존에 있던 좌표들 지우기
                store_axis_for_max_like_count.append([i, j])  # 새로 좌표 저장
            elif like_count == max_like_count_in_adjacent:
                store_axis_for_max_like_count.append([i, j])  # 해당 좌표 저장

    if len(store_axis_for_max_like_count) == 1:
        # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함
        row = store_axis_for_max_like_count[0][0]
        column = store_axis_for_max_like_count[0][1]
        seat[row][column] = student_num
    else:
        max_empty_count_in_adjacent = 0     # 주변에 빈칸이 최대  몇 명인지
        store_axis_for_max_empty_count = []  # 해당 좌표 저장하기 위한 리스트
        for axis in store_axis_for_max_like_count:
            empty_count = check(axis[0], axis[1], student_num, "empty")
            if empty_count > max_empty_count_in_adjacent:
                max_empty_count_in_adjacent = empty_count
                store_axis_for_max_empty_count.clear()            # 기존에 있던 좌표들 지우기
                store_axis_for_max_empty_count.append([axis[0], axis[1]])  # 새로 좌표 저장
            elif empty_count == max_empty_count_in_adjacent:
                store_axis_for_max_empty_count.append([axis[0], axis[1]])  # 해당 좌표 저장

        # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
        # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        # 어차피 axis를 row, column 순으로 돌면서 저장했어서 첫번째 것을 선택하면 됨.
        row = store_axis_for_max_empty_count[0][0]
        column = store_axis_for_max_empty_count[0][1]
        seat[row][column] = student_num


# 결과 출력
answer = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        count = check(i, j, seat[i][j], "like")
        answer += math.floor(10 ** (count - 1))
print(answer)

