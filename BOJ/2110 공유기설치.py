"""
20220818
골드5 공유기 설치
url: https://www.acmicpc.net/problem/2110
후기: parametric search 문제였다. 어떤 문제 분류임을 아는데도 몰라서 답(https://velog.io/@nnnyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%92%80%EC%9D%B4-%EB%B6%84%EC%84%9D-BOJ-2110-%EA%B3%B5%EC%9C%A0%EA%B8%B0-%EC%84%A4%EC%B9%98)을 봤다... 해당 문제 분류를 더 풀어봐야겠다.


입력으로 받은 집 위치를 기반으로 가능한 "최소 공유기 사이 거리(max_)" = 1, "최대 공유기 사이 거리(min_)" = (마지막 집 위치) - (첫 집 위치).
modem_distance = (max_ + min_) // 2 를 기준으로 C개의 공유기를 설치 할 수 있는지 확인.
(현재집 + modem_distance)의 위치보다 크거나 같은 곳에 있는 첫번째 집에 두번째 공유기 설치, 현재 집 = 두번째 공유기 위치 로 변경
반복하며 주어진 집 범위 내에서 C 개의 공유기를 모두 설치 할 수 있는지 확인

C 개 보다 적게 설치했다면 최대 공유기 사이 거리 값 조정 (간격 좁히기)
C 개 설치 했다면 현재의 mid 값 저장
C 개 이상 설치했다면 최소 공유기 사이 거리 조정 (간격 늘리기)
"""

# 처음에는 (가장 큰 수 - 가장 작은 수)를 N - 1 등분한 지점을 찾으려고 했으나
# 정수로 정확히 나누어 떨어지지도 않고, 해당 위치에 집이 없을 수도 있어서 불가능한 방법이라고 생각했다.

# 이후 답을 봤는데 공유기 사이 거리(modem_distance)를 기준으로 하는 파라메트릭 서치를 하면
# O(log(1,000,000,000) * 200,000) = 6,000,000이므로 시간 초과 없이 해결할 수 있다.

import sys

input_ = sys.stdin.readline

# initialization
answer = 0
N, C = map(int, input_().strip().split()) # 집의 개수, 설치할 공유기의 개수
houses = sorted([int(input_().strip()) for _ in range(N)])
min_ = 1
max_ = houses[-1] - houses[0]

while min_ <= max_:
    modem_distance = (min_ + max_) // 2 # 현재집 + modem_distance의 위치보다 크거나 같은 곳에 있는 첫번째 집에 두번째 공유기 설치
    modem_count = 1
    current = houses[0]

    for index in range(N):
        if houses[index] - current < modem_distance:
            continue

        modem_count += 1
        current = houses[index]
        
    if modem_count >= C:
        answer = max(answer, modem_distance)
        min_ = modem_distance + 1
    else:
        max_ = modem_distance - 1

# print
print(answer)
