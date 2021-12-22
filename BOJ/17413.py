"""
211106
실버3 단어 뒤집기2
url: https://www.acmicpc.net/problem/17413

후기: valid_li = list("abcdefghijklmnopqrstuvwxyz0123456789")로 한 후 20번째 줄 조건에 string[i] in valid_li를 썼다가
isalnum() 내장 모듈이 더 공간 효율적이라 바꿨다.
"""

string = input()  # 입력값을 받음
i = 0
start = 0

while i < len(string):
    if string[i] == "<":
        i += 1 
        while string[i] != ">": 
            i += 1 
        i += 1   
    elif string[i].isalnum(): # 숫자나 알파벳 소문자를 만나면
        start = i
        while i < len(string) and string[i].isalnum():
            i+=1
        tmp = string[start:i][::-1]
        string = string[:start] + tmp + string[i:]
    else:   # 공백
        i+=1 

print(string)
