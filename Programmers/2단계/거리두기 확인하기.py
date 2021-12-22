"""
211103
프로그래머스 2021년 카카오 채용연계형 인턴십
url: https://programmers.co.kr/learn/courses/30/lessons/81302
후기: 반복적으로 사용되는 flag = False / break 두 부분을 하나의 함수로 뺐어도 좋았을 것 같다.
"""

from itertools import combinations

def calculate_Manhaten(pair):
    return abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

def solution(places):
    answer = []
    
    for place in places:  # 각각의 places 들을
        flag = True
        axis = []
        for i in range(5):  # P인 부분들만 골라서 따로 저장
            for j in range(5):
                if place[i][j] == "P":
                    axis.append((i,j))
        
        for axis_pair in list(combinations(axis,2)):  # P간의 combination을 만든 후 맨해튼 거리 계산 시작
            if calculate_Manhaten(axis_pair) == 1: # 맨해튼 거리 1이면 for문 종료 후 답에 0 추가
                flag = False
                break
            elif calculate_Manhaten(axis_pair) == 2: # 맨해튼 거리가 2이면 파티션 여부 검증
                if axis_pair[0][0] == axis_pair[1][0]: # row가 같을 때
                    if place[axis_pair[0][0]][int((axis_pair[0][1] + axis_pair[1][1]) / 2)] != "X":
                        flag = False
                        break
                elif axis_pair[0][1] == axis_pair[1][1]: # column이 같을 때
                    if place[int((axis_pair[0][0] + axis_pair[1][0]) / 2)][axis_pair[0][1]] != "X":
                        flag = False
                        break
                else: # 대각선일 때
                    if place[axis_pair[0][0]][axis_pair[1][1]] != "X" or place[axis_pair[1][0]][axis_pair[0][1]] != "X":
                        flag = False
                        break
                        
        if flag:
            answer.append(1)
        else:
            answer.append(0)
        
    
    return answer
