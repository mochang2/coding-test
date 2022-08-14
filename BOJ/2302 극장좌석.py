"""
211211
실버1 극장 좌석
url: https://www.acmicpc.net/problem/2302
후기: DP 문제였다. 나는 피보나치로 풀었는데 피보나치가 되는 원리는 https://mygumi.tistory.com/132 여기에서 설명을 해줬다. DP 공부는 여전히 부족하다.
"""

import sys

input_ = sys.stdin.readline

N = int(input_().strip())
M = int(input_().strip())
fixed_seats = [int(input_().strip()) for _ in range(M)]

fibo = [1 for _ in range(N + 1)]
fibo[1] = 1
if N >= 2: # 수정사항. 재채점돼서 살펴보니 N == 1일 때에 대한 예외처리가 되어 있지 않았다.
    fibo[2] = 2
for i in range(3, N + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
    
result = 1
tmp = 0
for i in range(1, N + 1):
    if i in fixed_seats:
        result *= fibo[tmp]
        tmp = 0
    else:
        tmp += 1

print(result * fibo[tmp])
