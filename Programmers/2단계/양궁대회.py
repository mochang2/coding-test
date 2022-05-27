"""
220527
양궁대회
url: https://programmers.co.kr/learn/courses/30/lessons/92342
후기: 양궁대회.js를 푼 뒤에 python으로 다시 풀어봤다.
이번에는 deep copy, shallow copy만 잘 신경써줬으면 됐다.
"""

from copy import deepcopy

answer = [-1]
best_difference = -1
SCORE_KIND = 11

def ChooseBestScore(lion):
    global answer
    
    for index in range(SCORE_KIND - 1, -1, -1):
        if lion[index] == answer[index]:
            continue
        if lion[index] > answer[index]:
            return lion
        if lion[index] < answer[index]:
            return answer
    return answer # return할 일 없음

def CalcResult(appeach, lion):
    # return can win, score difference
    appeach_score = 0
    lion_score = 0

    for index in range(SCORE_KIND - 1): # 0점칸은 셀 필요 없음
        if appeach[index] == lion[index] and lion[index] == 0:
            continue
        if lion[index] > appeach[index]:
            lion_score += SCORE_KIND - 1 - index
        else:
            appeach_score += SCORE_KIND - 1 - index
    
    return lion_score > appeach_score, lion_score - appeach_score

def BackTrack(n, score_index, appeach, lion):
    # n: 몇 발 쏠 수 있는지, score_index: 몇 점 쏘는지
    global answer, best_difference
    
    if score_index == SCORE_KIND:
        # 백트래킹 종료 조건
        if n != 0:
            lion[-1] = n
        can_win, score_difference = CalcResult(appeach, lion)
        if not can_win:
            return
        
        if score_difference > best_difference:
            best_difference = score_difference
            answer = deepcopy(lion)
        elif score_difference == best_difference:
            answer = deepcopy(ChooseBestScore(lion))
        return
    
    if n > appeach[score_index]:
        lion[score_index] = appeach[score_index] + 1
        BackTrack(n - lion[score_index], score_index + 1, appeach, lion)
        lion[score_index] = 0
    
    lion[score_index] = 0
    BackTrack(n, score_index + 1, appeach, lion)
    lion[score_index] = 0

def solution(n, info):
    BackTrack(n, 0, info, [0 for _ in range(11)])
    return answer
