"""
220925
2019 카카오 개발자 겨울 인턴십
url: https://programmers.co.kr/learn/courses/30/lessons/64065
후기: 분명 문제는 쉬운데... 생각보다 오래 걸린다. 10분 이내에 풀어본 적이 없다.
사실은 쉽지 않은걸까?

단순한 문제였다.
str -> set -> list로 계속 type conversion을 해주면 된다.

되게 간단한 풀이는 re.findAll로 \d+를 찾은 뒤, Counter를 import해서 2줄만에 푸는 풀이도 있었다.
"""

def splitIntoList(string):
    return set(map(int, string.split(',')))

def solution(s):
    number_sets = list(map(splitIntoList, s[2:-2].split('},{'))) # set 별로 split한 뒤 진짜 set 타입으로 만듦
    number_sets.sort(key=lambda x: len(x))
    
    for index in range(len(number_sets) - 1, 0, -1):
        number_sets[index] = number_sets[index] - number_sets[index - 1] # 각 set의 인자가 1개만 남도록 만듦
        
    numbers = [set_.pop() for set_ in number_sets]
    
    return numbers
  
