"""
211211
실버1 극장 좌석
url: https://www.acmicpc.net/problem/2302
후기: DP 문제였다. 나는 피보나치로 풀었는데 피보나치가 되는 원리는 https://mygumi.tistory.com/132 여기에서 설명을 해줬다. DP 공부는 여전히 부족하다.
"""

N = int(input())
M = int(input())
fixed_seats = []
for i in range(M):
    fixed_seats.append(int(input()))

# 연결된 좌석의 수가 증가할수록 가능한 경우의 수는 피보나치 수열로 증가.
fibo = [1 for _ in range(N + 1)]
fibo[1] = 1
fibo[2] = 2
for i in range(3, N + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
    
result = 1
tmp = 0
for i in range(1, N + 1):
    # VIP 좌석을 기준으로 경우의 수 곱의 법칙 적용.
    if i in fixed_seats:
        result *= fibo[tmp]
        tmp = 0
    else:
        tmp += 1

print(result * fibo[tmp])
