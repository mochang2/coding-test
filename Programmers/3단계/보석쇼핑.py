"""
211115
2020 카카오 인턴십
url: https://programmers.co.kr/learn/courses/30/lessons/67258
후기: while 문 안에서 계속 새로운 set을 만들고, 그것의 길이를 구하니 O(n^2)이 되면서 효율성 실패함.
새로 넣고 빠지는 것이 어떤 보석의 종류인지만 기억하고 이를 변수에 저장해두면 됨.
추가로 해당 보석이 빠지면 gem_dict라는 변수에서 제외시켜줘야 isvalid 함수가 잘 작동함.

def isvalid(gem_dict, num_of_kind):
    if len(gem_dict) != num_of_kind:
        return False
    for value in gem_dict.values():
        if value <= 0 :
            return False
    return True 이렇게 선언했다가 효율성을 통과하지 못함.
"""

def isvalid(gem_dict, num_of_kind, gems, left):
    if len(gem_dict) != num_of_kind:
        # 아직 모든 보석이 gem_dict에 들어오지 않음.
        return False
    if  gem_dict[gems[left - 1]] == 0:
        # left 포인터가 이동함으로써 특정 보석 종류의 개수가 0이 됐는지 확인. 0이면 gem_dict에서 제외시킴.
        gem_dict.pop(gems[left - 1])
        return False
    
    return True

def solution(gems):
    # 투 포인터 알고리즘(슬라이딩 윈도우)
    # 초기화
    n = len(gems)
    num_of_kind = len(set(gems))  # 보석의 종류의 개수
    left = 0    # left pointer
    right = 0   # right pointer
    li = [1,n]  # 최종적으로 return 할 값 초기화
    gem_dict = {gems[0]: 1}  # gem_dict에 0번째 인덱스 추가하고 시작
    
    while left < n:
        valid = isvalid(gem_dict, num_of_kind, gems, left)  # 모든 보석들이 1개 이상씩 포함되었는지 판단
        if valid and li[1] - li[0] > right - left:
            # 모든 보석들이 포함되어 있고 기존 것보다 길이가 더 짧다면. 길이가 같다면 시작 인덱스가 더 작아야 되므로 등호는 뺌.
            li = [left + 1, right + 1]  

        if valid or right == n - 1:  # 왼쪽 포인터가 이동하는 조건. 제일 왼쪽에 있는 보석을 gem_dict에서 1개 뺌.
            left += 1
            gem_dict[gems[left - 1]] -= 1
        else:  # 오른쪽 포인터가 이동하는 조건. 제일 오른쪽에 있는 보석을 gem_dict에서 1개 더함.
            right += 1
            if gems[right] in gem_dict:
                gem_dict[gems[right]] += 1
            else:
                gem_dict[gems[right]] = 1

    return li
