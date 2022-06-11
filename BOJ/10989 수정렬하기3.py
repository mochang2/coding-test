"""
20220611
브론즈1 수 정렬하기 3
url: https://www.acmicpc.net/problem/10989
후기: O(N) = 10,000,000인데 반해 메모리 제한이 8MB 밖에 되지 않아, counting sort로만 풀 수 있는 문제였다.
counting sort은 주어진 배열의 값 범위가 작은 경우 빠른 속도를 갖는 정렬 알고리즘이다.
최댓값과 입력 배열의 원소 값 개수를 누적합으로 구성한 배열로 정렬을 수행한다.
"""

import sys
input_ = sys.stdin.readline

MAX = 10001
N = int(input_().rstrip())
counts = [0 for _ in range(MAX)]
for _ in range(N):
    counts[int(input_().rstrip())] += 1

for i in range(1, MAX):
    for _ in range(counts[i]):
        print(i)
