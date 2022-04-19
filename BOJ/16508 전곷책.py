"""
211117
실버3 전공책
url: https://www.acmicpc.net/problem/16508
후기: 전수 조사 문제.
input이 최대 16개까지밖에 안된다는 것에 감안. 2^16(모든 combination 개수)이면 100만 보다 훨씬 적기 때문에 모든 경우의 수를 조사할 수 있었다.
"""

import sys
from itertools import combinations

# 입력받기
string = input()
dic = dict()
for char in string:
    if char in dic.keys():
        dic[char] += 1
    else:
        dic[char] = 1

num = int(input()) # 전공책 개수
books = []
for i in range(num):
    books.append(sys.stdin.readline().split())

# 모든 경우의 수 구하기(전수조사)
every_cases = []
for n in range(1, num + 1): # n: 몇 개를 가지고 combination을 만드는지
    for c in list(combinations(books, n)): # c: 가능한 모든 combination
        price = 0
        name = ""
        for i in c: # i: combination의 각각
            price += int(i[0])
            name += i[1]
        every_cases.append([price, name])

every_cases.sort(key=lambda x: (x[0]))
flag = True
for each_case in every_cases:
    temp = dic.copy()
    flag = True
    for char in each_case[1]:
        if char in temp.keys():
            temp[char] -= 1
    for i in temp.values():  # 제목을 만들 수 있는지 판단
        if i > 0:
            flag = False
            break
    if flag:
        print(each_case[0])
        break

if not flag:  # 못 만드는 경우
    print(-1)
