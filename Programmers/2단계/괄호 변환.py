"""
211101
2020 KAKAO BLIND RECRUIMENT
url: https://programmers.co.kr/learn/courses/30/lessons/60058
후기: 결국 원리는 이해 못 했으나, 하라는 대로 하니까 구현이 됐다.
"""

def divide_into_two_balanced_strings(string):
    num_of_left = 0
    num_of_right = 0
    for i, s in enumerate(string):
        if s == "(":
            num_of_left += 1
        else:
            num_of_right += 1
        if num_of_left == num_of_right:
            return string[:i+1], string[i+1:]

def is_right_string(balanced_string):
    li = []
    for s in balanced_string:
        if len(li) == 0:
            if s == ")":
                return False
            else:
                li.append(s)
        else:
            if s == "(":
                li.append(s)
            elif s == ")" and li[-1] == "(":
                li.pop()
    
    if not li:  # li가 비어있으면
        return True
    return False

def flip(string):
    res = ""
    for s in string:
        if s == "(":
            res += ")"
        else:
            res += "("
    return res

def solution(p):
    res=""
    if p == "":  # 1단계
        return ""
    
    u,v = divide_into_two_balanced_strings(p) # 2단계
    #print()
    #print(u, v)
    
    if is_right_string(u): # 3단계
        u += solution(v)
        #print(u)
        return u
    else: # 4단계
        res += "("
        res += solution(v)
        res += ")"
        res += flip(u[1:-1])
        #print(res)
        return res

