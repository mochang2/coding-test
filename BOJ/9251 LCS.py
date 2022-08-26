"""
20220826
골드5 LCS
url: https://www.acmicpc.net/problem/9251
후기: 그동안 착각하고 살았던 부분이 1초면 약 1억 번의 연산을 할 수 있을 줄 알았다.
그런데 파이썬은 2천만 번 정도라고 한다.
그래서 이 문제에서 파이썬의 제한이 2초길래 완탐하면 1억 6천만 정도면 되므로 가능하겠다!
싶어서 진행하다가(심지어 잘못된 완탐이었다) 시간 초과가 날 것 같길래 포기했다.
고민 끝에 DP일 것이다 라는 결론에 도달했지만 점화식을 구하진 못 했다.
검색해보니 LCS가 이미 널리 알려진 알고리즘 그 자체였다.

두 사이트에서 도움을 받았다.
https://www.youtube.com/watch?v=z8KVLz9BFIo
https://velog.io/@nnnyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%92%80%EC%9D%B4-%EB%B6%84%EC%84%9D-BOJ-9251-LCS

9252번은 이 문제의 변형이다. 같이 참고하면 좋다.
""" 

# dp는 first[:i]인 문자열과 second[:j]인 문자열 중에서 최대길이의 부분 수열을 저장한다

import sys

input_ = sys.stdin.readline

# initialization
first = input_().strip()
second = input_().strip()
first_length = len(first)
second_length = len(second)
dp = [[0 for _ in range(second_length + 1)] for __ in range(first_length + 1)]

for i in range(first_length):
    for j in range(second_length):
        if first[i] == second[j]:
            # 같다면 first[:i - 1] second[:j - 1]의 LCS에서 1을 더한 값이다
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            # 다르다면 first[:i - 1]과 second[:j]의 LCS, first[:i]과 second[:j - 1]의 LCS 중 더 큰 값이다
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(dp[-1][-1])

