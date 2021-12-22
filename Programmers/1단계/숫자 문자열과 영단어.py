"""
211029
2021 카카오 채용연계형 인턴십
url: https://programmers.co.kr/learn/courses/30/lessons/81301
"""

def solution(s):
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"} # dict 선언(c++의 map)
    
    while True:
        flag = False  # s에 아직 문자열이 남아있는지 체크 (수정사항) => 필요 없음 replace는 find처럼 해당하는 첫 문자열만 찾는 것이 아니라 모든 문자열을 찾아서 바꿈
        for key in list(dic.keys()):
            if key in s:
                s = s.replace(key, dic[key])
                flag = True
        
        if not flag:
            break
    
    return int(s)
