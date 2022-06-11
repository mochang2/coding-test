"""
20220611
실버5 수 정렬하기 2
url: https://www.acmicpc.net/problem/2751
후기: 처음에 시간초과가 났다.
귀찮아서 sys.stdin.readline가 아닌 input을 사용했기 때문이다.
시간초과가 난 이유는 https://buyandpray.tistory.com/7 여기에 정리되어 있다.
"""

import sys
input_ = sys.stdin.readline

N = int(input_().rstrip())
li = [int(input_().rstrip()) for _ in range(N)]
li.sort()
for num in li:
    print(num)
