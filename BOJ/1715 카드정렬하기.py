"""
20220721
골드4 카드 정렬하기
url: https://www.acmicpc.net/problem/1715
후기: 그리디, 힙 문제이다.
처음에는 그냥 정렬해서 순서대로 더하면 되는 그리디인 줄 알아서 '이게 어떻게 골드?' 싶었는데 내리 두 번 연속 틀렸다.
반례를 찾아보다가 힙이라는 힌트를 얻어버려서 빨리 풀 수 있었다.
마냥 쉽지는 않은 문제였던 것 같다.

카드 덱은 남아 있는 카드 덱에서 가장 양이 적은 덱과 두 번째로 양이 적은 덱을 합침으로써 계산을 최소화할 수 있다.
"""

import sys
import heapq as h

input_ = sys.stdin.readline

# initialization
answer = 0
N = int(input_().strip())
cards = [int(input_().strip()) for _ in range(N)]
h.heapify(cards) # 최소힙

while len(cards) >= 2:
    smallest_deck = h.heappop(cards)
    next_smallest_deck = h.heappop(cards)
    card_deck = smallest_deck + next_smallest_deck
    
    answer += card_deck
    h.heappush(cards, card_deck)

# print
print(answer)
