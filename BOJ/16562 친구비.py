"""
20220318
골드3 친구비
url: https://www.acmicpc.net/problem/16562
후기: 친구의 친구는 친구이다. 즉 같은 그래프 안에 있으면 친구다라는 개념에서 출발해서 BFS/DFS로 풀면 바로 풀릴 것이라 생각했다.
다만 친구 관계가 최대 10000개까지 주어진다면 DFS는 recursion 에러가 나서 sys.setrecursionlimit을 해줘야 될 것 같았다.
그나마 함수로 만들었는데도 BFS를 계속하면서 중단 조건을 찾아야 하니(리팩토링 없이) 코드가 보기 너무 안 좋다...
다른 사람들은 union-find로 했는데 코드가 훨씬 깔끔한 것 같다.
그리고 Oh no를 출력해줘야 하는데 계속 oh no를 출력해줘서 틀렸었다.. 꼭 확인하자
"""

import sys
from collections import deque

def Check():
    global is_friend
    for bool_ in is_friend:
        if not bool_:
            return False
    return True

def Is_Finished(num):
    global N
    if num == N:
        return True
    return False

max_value = 10001

# initialization
num_of_friend = 0
N, M, k = map(int, sys.stdin.readline().strip().split())
seed_money = k
prices = [max_value]
prices.extend(list(map(int, sys.stdin.readline().strip().split())))
friends = [[] for _ in range(N + 1)]
is_friend = [False for _ in range(N + 1)]
is_friend[0] = True
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    friends[a].append(b)
    friends[b].append(a)
matrix = []
for index, price in enumerate(prices):
    matrix.append([price, index])
matrix.sort(key=lambda x: (x[0]))

# BFS
for list_ in matrix:
    price = list_[0]
    index = list_[1]
    if is_friend[index]:
        continue
    k -= price
    if k < 0:
        break
    num_of_friend += 1
    is_friend[index] = True
    if Is_Finished(num_of_friend):
        break

    queue = deque([index])
    while len(queue) != 0:
        first = queue.popleft()
        for friend in friends[first]:
            if not is_friend[friend]:
                queue.append(friend)
                is_friend[friend] = True
                num_of_friend += 1
                if Is_Finished(num_of_friend):
                    print(seed_money - k)
                    sys.exit(0)


if Check():
    print(seed_money - k)
    sys.exit(0)
else:
    print("Oh no")
