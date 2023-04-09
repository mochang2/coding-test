"""
20230409
골드3 순회강연
url: https://www.acmicpc.net/problem/2109
후기: 힙을 이용한 그리디 문제다.
처음에는 deadline이 작은 offer부터 deadline이 넘지 않았으면 무조건 수락했다.
하지만 이러한 방식은 더 큰 pay가 뒤에 존재한다면 수락하지 못하는 문제가 생긴다.

반례
3
1 1
1000 2
2000 2
정답: 3000, 오답: 2001

4
20 2
30 2
40 3
40 3
정답: 110, 오답: 70

20
85 8
56 11
58 12
28 20
36 12
45 9
55 4
1 3
71 6
72 15
38 9
76 20
67 5
78 2
48 18
100 3
16 2
7 10
95 5
42 14
정답: 1050, 오답: 970

다음과 같은 방법으로 문제를 풀었다.
1. 입력을 받고 offers를 deadline 기준으로 오름차순 정렬을 한다(아래 풀이에서는 pay 기준으로 내림차순을 했지만 답에는 영향을 끼치지 않는다).
2. offer의 pay를 최소힙에 넣는다.
   만약 해당 offer의 deadline 때문에 수락을 못한다면, pay가 가장 작은 offer를 최소힙에서 제거한다.
   이때 deadline이 작은 것부터 순회해야 pay가 높은 offer가 최소힙에서 사라지지 않는다.
"""

## 오답

from sys import stdin
from heapq import heappush, heappop

def initialize():
    offers = []

    offer_count = int(stdin.readline().strip())
    for _ in range(offer_count):
        pay, deadline = map(int, stdin.readline().strip().split())
        heappush(offers, (deadline, -pay))

    return offers

def calculateMaxPay(offers):
    total_pay = 0
    day = 1

    while len(offers) != 0: # 더 일할 거리가 남아 있다면
        pay = -heappop(offers)[1]
        total_pay += pay

        while len(offers) != 0 and day >= offers[0][0]: # 처리하지 못하는 일들 제외
            heappop(offers)

        day += 1

    return total_pay

offers = initialize()
total_pay = calculateMaxPay(offers)
print(total_pay)



## 정답
from sys import stdin
from heapq import heappush, heappop

def initialize():
    offers = []

    offer_count = int(stdin.readline().strip())
    for _ in range(offer_count):
        pay, deadline = map(int, stdin.readline().strip().split())
        offers.append((deadline, -pay))

    return sorted(offers)

def calculateMaxTotalPay(offers):
    accepted_offers = []

    for deadline, pay in offers:
        heappush(accepted_offers, -pay)
        
        accept_with_replacing_min_pay = len(accepted_offers) > deadline
        if accept_with_replacing_min_pay:
            heappop(accepted_offers)
            
    return sum(accepted_offers)

offers = initialize()
total_pay = calculateMaxTotalPay(offers)
print(total_pay)

