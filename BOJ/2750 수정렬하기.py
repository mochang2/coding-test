"""
20220604
브론즈1 수 정렬하기
url: https://www.acmicpc.net/problem/2750
후기: 문제 그대로 아주 단순한 구현문제이다.
"""

N = int(input().strip())
li = [int(input().strip()) for _ in range(N)]
li.sort()
for num in li:
    print(num)
