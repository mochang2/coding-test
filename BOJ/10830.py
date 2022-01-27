"""
골드4 행렬 제곱
url: https://www.acmicpc.net/problem/10830
후기: 행렬 거듭 제곱을 효율적으로 하는 알고리즘 따로 있다고 했는데,
나중에 플래티넘 문제에 있다고 들었다. 그때 다시 찾아봐야겠다.
지금은 정수의 거듭제곱을 간단히 하는 방법(암호학에서 배운 내용)을 생각해서 구현했다.
"""

import sys

def init_input(i):  # input에 1000이 있는데 1000으로 나눈 나머지를 구하라고 해서 정의함
    return int(i) % 1000

def mul_matrix(matrix1, matrix2):  # 프로그래머스에서 예전에 푼 구현 문제가 있었는데, 다시 계산하기 귀찮아서 검색했다.
    global N
    result = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][k] += matrix1[i][j] * matrix2[j][k]
                result[i][k] %= 1000
    return result

N, B = map(int, sys.stdin.readline().strip().split())
cal_order = []  # "s": square, "m": mul_origin_matrix
while B != 1:  # 정수의 거듭제곱을 간단하게 하는 방법 사용
    if B % 2 == 1:
        cal_order.append("m")
        B -= 1
    else:
        cal_order.append("s")
        B = B // 2

matrix = []
for i in range(N):
    matrix.append(list(map(init_input, sys.stdin.readline().strip().split())))

answer = matrix
for s in cal_order[::-1]:
    if s == "s":
        answer = mul_matrix(answer, answer)
    else: # s == "m":
        answer = mul_matrix(answer, matrix)

for i in range(N):
    for j in range(N):
        print(answer[i][j], end= " ")
    print()
