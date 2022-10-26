"""
221026
url: https://school.programmers.co.kr/learn/courses/30/lessons/42890
후기: n이 작은 것을 보고 완탐이 충분하다고 생각했다(효율성 테스트도 없었다).
4중 for문이 좀 걸리긴 하지만...

1번째 for문은 몇 개의 후보키를 선택할 지를,
2번째 for문은 combination을,
3번째 for문은 tuple을,
4번째 for문은 tuple에 특정 attribute를 선택한다.
유일성을 만족하는지 확인한 뒤

마지막에 is_unique를 통해 최소성을 만족하는지 확인한다.
"""

from itertools import combinations

def solution(relation):
    uniques = [] # 유일성을 만족하는 키s
    keys = [i for i in range(len(relation[0]))] # column 이름
    
    # 1 ~ n 까지 콤비네이션
    # set으로 집어넣음
    # set의 길이가 relation의 길이와 같으면 전부 li에 추가(유일성)
    for length in range(1, len(relation[0]) + 1): # combination 길이
        for comb in combinations(keys, length): # 작은 수부터 정렬됨
            key_set = set()
            
            for tuple_ in relation:
                result = ''
                
                for index in comb:
                    result += tuple_[index]
            
                key_set.add(result)
                
            if len(key_set) == len(relation):
                uniques.append(set(comb))

    # 최소성 확인
    # True / False로 set 비교 후 True의 개수만 셈
    # 두 개씩 비교
    is_unique = [True for _ in range(len(uniques))]
    
    for left in range(0, len(uniques) - 1):
        for right in range(left + 1, len(uniques)):
            if not is_unique[left]:
                continue
                
            if len(uniques[left] - uniques[right]) == 0:
                is_unique[right] = False
    
    return len(list(filter(lambda x: x, is_unique)))
