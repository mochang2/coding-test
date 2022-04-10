"""
20220410
실버3 1,2,3 더하기
url: https://www.acmicpc.net/problem/9095
후기: DP이다. 1937번 욕심쟁이 판다를 풀려고 했으나 DP는 나에게 너무 어려웠다...
DP를 다시 다잡기 위해 쉬운 문제 맛보기를 했다.
단순히 구현으로 생각했다면 3,2,1을 각각의 비트로 생각하고 0b111~0b001 총 7가지 경우의 수 중에서
6을 0b111로 표현하고자 한다면 1+2+3, 1+3+2, 2+1+3, 2+3+1, 3+1+2, 3+2+1이 있으며,
0b011로 표현하고자 한다면 2+2+1+1 등 6가지와 2+1+1+1+1 등 4가지가 있다.
이런 식으로 구하려고 했다.
시간 초과는 날 것 같지 않지만 구현이 복잡해지고 다른 규칙을 찾던 중에 피보나치와 비슷한 성질이 있다는 것을 발견했다.
"""

def makeFibo():
    global fibo
    for i in range(3, M + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2] + fibo[i - 3]

li = [] # input값을 기억하기 위한 변수
T = int(input())
for _ in range(T):
    li.append(int(input()))
M = max(li) # 가장 큰 값에 따라 fibo의 크기를 결정하기 위함
fibo = [0 for _ in range(M + 1)]
fibo[0] = 1 # 피보나치 수열 초기값
fibo[1] = 1
fibo[2] = 2
makeFibo()

for num in li:
    print(fibo[num])
