"""
골드5 배
url: https://www.acmicpc.net/problem/1092
후기: 그리디 문제였다. heap을 쓰려고 고민했으나 의도치 않은 대로 결과가 나왔다.
dictionary와 같은 느낌이지만 순서가 중요하기에 weight_limits라는 변수를 이차원 배열로 선언했다.
시간이 생각보다 오래 걸려서 줄일 필요가 있다.
"""

# 어차피 sort는 해야되니 M log(M) 이내로 끝내야 함
# 선형탐색으로 끝내는 방법 고민하기
# 크레인의 최대 한계 무게를 기준으로 개수 나누기
import sys
import math

N = int(input()) # 크레인 수
weight_limits = [[-1, 0]]
for limit in map(int, sys.stdin.readline().strip().split()):
    weight_limits.append([limit, 0])
weight_limits.sort(key=lambda x: (-x[0]))  # 첫 번째 인자, 즉 한계 무게를 기준으로 내림차순 정렬
max_limit = weight_limits[0][0]
print(weight_limits)

M = int(input()) # 박스 수
for weight in map(int, sys.stdin.readline().strip().split()):
    if weight > max_limit:
        print(-1)
        sys.exit(0)
    for i in range(1, N + 1):
        if weight_limits[i - 1][0] >= weight > weight_limits[i][0]:
            # 해당 weight limit 보다 작은 물건의 개수가 몇 개인지 파악
            weight_limits[i - 1][1] += 1
            break
print(weight_limits)
answer = 0
sum_ = 0
for i in range(N + 1):
    sum_ += weight_limits[i][1] 
    answer = max(answer, math.ceil(sum_ / (i + 1)))
print(answer)
