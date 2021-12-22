"""
211204
완전탐색
url: https://programmers.co.kr/learn/courses/30/lessons/42842
후기: 완전탐색이었다. 그래서 가능한 모든 약수들을 구해서 비교했다. 다른 사람들의 풀이를 보니까 2차 방정식으로 근의 공식을 쓴 사람도 있었다.
"""

from math import sqrt, floor

def solution(brown, yellow):
    carpet = brown + yellow
    yellow_divisors = []
    carpet_divisors = []
    
    for i in range(1, floor(sqrt(yellow)) + 1):
        if yellow % i == 0:
            yellow_divisors.append([i, yellow // i])
    for i in range(1, floor(sqrt(carpet)) + 1):
        if carpet % i == 0:
            carpet_divisors.append([i, carpet // i])
    
    for yellow_divisor in yellow_divisors:
        if [yellow_divisor[0] + 2, yellow_divisor[1] + 2] in carpet_divisors:
            return [yellow_divisor[1] + 2, yellow_divisor[0] + 2]