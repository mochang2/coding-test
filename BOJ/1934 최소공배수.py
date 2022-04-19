"""
211109
실버5 최소공배수
url: https://www.acmicpc.net/problem/1934
입력된 두 수들의 최소공배수를 차례로 출력하면 된다.
후기: math 모듈에는 참 편한 함수들이 많다. 잘 익혀두자.
"""

import sys
import math

T = int(sys.stdin.readline().strip())
data = []
for i in range(T):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(T):
    print(int((data[i][0] * data[i][1]) / math.gcd(data[i][0], data[i][1])))
