"""
220910
2018 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/17684
후기: 2단계 치고 엄청 쉬웠다. 카카오 문제는 프로그래머스 난이도가 이상한 것 같다.

투 포인터 알고리즘으로 문자열을 슬라이싱 한 뒤에 dic에 있는지 확인했다.
엣지 케이스가 있을 줄 알았는데 없이 금방 통과했다.
"""

def initDict():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {alpha[index]: index + 1 for index in range(len(alpha))}
    
    return dic, len(alpha)

def solution(msg):
    dic, dic_length = initDict()
    answer = []
    
    left = 0
    right = 0
    while left < len(msg):
        while right < len(msg) and msg[left:right + 1] in dic:
            right += 1
            
        answer.append(dic[msg[left:right]]) # dic에 저장된 문자열의 index 추가
        dic[msg[left:right + 1]] = dic_length + 1 # 새로운 문자열을 dic에 저장
        dic_length += 1
        
        left = right
    
    return answer
