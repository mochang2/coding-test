"""
20220716
플래티넘4 축사 배정
url: https://www.acmicpc.net/problem/2188
후기: 이분매칭 문제이다.
9576 책 나눠주기가 그리디 문제였는데, 이분매칭으로도 풀 수 있다고 해서 이분매칭이 무엇인지 공부하기 위해 풀었다.
이분매칭의 시간 복잡도는 O(VE^2) = 200^3이므로 이 문제에서 충분히 2초 안에 풀 수 있는 시간 복잡도이다.
"""

import sys

input_ = sys.stdin.readline

# bipartite matching
def dfs(index: int) -> bool:
    global cows, matching, barns

    for barn_index in cows[index]:
        if barns[barn_index]:
            continue

        barns[barn_index] = True # 해당 축사는 소가 들어갈 수 있음
        if matching[barn_index] == -1 or dfs(matching[barn_index]): # 배정이 안된 축사거나 이전에 배정된 축사가 배정된 소가 다른 축사로 갈 수 있다면
            matching[barn_index] = index # index의 소가 barn_index의 축사에 배정
            return True
    
    return False

# initialization
answer = 0
cow_num, barn_num = map(int, input_().strip().split()) # N, M
cows = [tuple(map(int, input_().strip().split()))[1:] for _ in range(cow_num)] # 소가 원하는 축사
matching = [-1 for _ in range(barn_num + 1)] # 축사. 들어간 소를 기록

for cow_index in range(len(cows)):
    barns = [False for _ in range(barn_num + 1)] # 매칭됐는지 여부. 매 cow_index 마다 초기화
    if dfs(cow_index):
        answer += 1

# print
print(answer)
