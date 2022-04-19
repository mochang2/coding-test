"""
211109
실버5 팩토리얼 분해
url: https://www.acmicpc.net/problem/2057
팩토리얼 분해. 0~1,000,000,000,000,000 사이의 수 중에서 서로 다른 팩토리얼의 합으로 나타낼 수 있는 수를 찾기.
후기: 0도 input으로 올 경우를 생각을 안 해서 고생했다.
"""

import math
N = int(input())

if N == 0:
    print("NO")
else:
    res = 0
    flag = False
    for i in range(20, -1, -1):

        if res + math.factorial(i) <= N:
            res += math.factorial(i)
        if res == N:
            flag = True
            print("YES")
            break

    if not flag:
        print("NO")
