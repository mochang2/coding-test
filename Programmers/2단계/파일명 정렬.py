"""
211210
2018 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/17686
후기: 일전에 문자열 정렬 문제에서 cmp_to_key를 배운 적이 있어서 써먹었다.
그런데 다른 사람 답을 보니까 re로 3줄만에 해결한 것이 있었다... 충격.
re 모듈도 이참에 공부해두자.
"""

from functools import cmp_to_key

def sort_criteria(file1, file2):
    if file1[0].lower() > file2[0].lower(): # head 비교
        return 1
    elif file1[0].lower() == file2[0].lower():
        if int(file1[1]) > int(file2[1]): # number 비교
            return 1
        elif int(file1[1]) == int(file2[1]):
            return 0
        else: # file1[1] < file2[1]:
            return -1
    else: # file1[0] < file2[0]:
        return -1

def solution(files):
    li = []
    
    for index, file in enumerate(files):
        tmp_li = []
        tmp_str = ""
        for char in file:
            if len(tmp_li) == 0:
                # head
                if not char.isdigit(): # number를 만나기 전까지
                    tmp_str += char
                else:
                    tmp_li.append(tmp_str)
                    tmp_str = char
            elif len(tmp_li) == 1:
                # number
                if char.isdigit():
                    tmp_str += char
                else:
                    tmp_li.append(tmp_str)
                    tmp_str = char
            else: # len(tmp_li) == 2
                # tail
                tmp_str += char
        tmp_li.append(tmp_str)
        li.append(tmp_li)
        
    li.sort(key=cmp_to_key(sort_criteria))
    return ["".join(i) for i in li]



# 다른 사람의 풀이
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b