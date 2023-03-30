"""
20230330
골드5 캠프 준비
url: https://www.acmicpc.net/problem/16938
후기: 골드 같지 않게 너무 쉬웠고 함수를 별도로 선언하기도 민망한 내용이었다.
단순히 완전 탐색 문제였다.
N의 수가 너무 적기 때문에 DP나 중간에 재귀를 중단하는 백트래킹, 정렬 이후 그리디 등의 방식을 고민하지 않아도 됐다.

다음과 같이 풀었다.
1. 2부터 문제 난이도의 개수만큼 문제 난이도들의 조합을 생성한다.
2. 조건에 부합하면 number_of_ways_to_choose에 1을 더한다.
"""

from sys import stdin
from itertools import combinations

def initialize():
    number_of_questions, min_sum, max_sum, min_gap = map(int, stdin.readline().strip().split())
    
    return list(map(int, stdin.readline().strip().split())), lambda questions: min_sum <= sum(questions) <= max_sum and min_gap <= max(questions) - min(questions)

number_of_ways_to_choose = 0
difficulties, isSatisfied = initialize()

for count in range(2, len(difficulties) + 1):
    for chosen_questions in combinations(difficulties, count):
        if isSatisfied(chosen_questions):
            number_of_ways_to_choose += 1

print(number_of_ways_to_choose)
