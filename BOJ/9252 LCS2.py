"""
20220826
골드4 LCS 
url: https://www.acmicpc.net/problem/9252
후기: 9251을 직후 풀었다.
9251을 풀 때 도움을 받았던 https://www.youtube.com/watch?v=z8KVLz9BFIo 사이트에서 이 풀이 그대로 있었어서 쉽게 해결했다.
""" 

# dp - first[:i]인 문자열과 second[:j]인 문자열 중에서 최대 길이의 부분 수열을 저장한다
# direciton - 1: 왼쪽 위 대각선, 2: 위, 3: 왼쪽. 어떤 방향을 따라 dp 값이 결정되었는지 기록한다. 역추적하며 1이었던 위치들을 합하면 lcs가 된다
# python recursion depth는 기본이 1000이므로 조정이 필요하다

import sys

input_ = sys.stdin.readline
sys.setrecursionlimit(1000 ** 2) # 문자열의 최대 길이가 1000이므로

def getLcs(i, j, result):
    global first, directions

    direction = directions[i][j]

    if direction == 0:
        return result
    elif direction == 1:
        return getLcs(i - 1, j - 1, first[i - 1] + result)
    elif direction == 2:
        return getLcs(i - 1, j, result)
    elif direction == 3:
        return getLcs(i, j - 1, result)
        
# initialization
first = input_().strip()
second = input_().strip()
first_length = len(first)
second_length = len(second)
dp = [[0 for _ in range(second_length + 1)] for __ in range(first_length + 1)]
directions = [[0 for _ in range(second_length + 1)] for __ in range(first_length + 1)]

# bottom up dp
for i in range(first_length):
    for j in range(second_length):
        if first[i] == second[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
            directions[i + 1][j + 1] = 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
            if dp[i + 1][j] >= dp[i][j + 1]:
                directions[i + 1][j + 1] = 3
            else:
                directions[i + 1][j + 1] = 2

# print
lcs_length = dp[-1][-1]

if lcs_length == 0:
    print(lcs_length)
else:
    lcs = getLcs(first_length, second_length, '')
    print(lcs_length)
    print(lcs)

