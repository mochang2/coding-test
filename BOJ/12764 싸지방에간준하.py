"""
20220603
골드3 싸지방에 간 준하
url: https://www.acmicpc.net/problem/12764
후기: 구현, 자료구조 특히 힙 문제였다.
boj 11000번 강의실 배정이나, 19598번 최소 회의실 개수와 비슷한 문제였다.
다만 이번에는 입력받은 times를 기준으로 반복문을 도는 것이 아니라, 시각(0 ~ 1,000,000)을 기준으로 반복문을 돌아야 했다.
"""

import heapq as h
import sys
input_ = sys.stdin.readline

# initialization
N = int(input_().strip())
times = []
for _ in range(N):
    times.append(list(map(int, input_().strip().split())))
times.sort(key=lambda x: (x[0], x[1]))
answer = [] # 이용 횟수
usage = [] # heap, (끝나는 시각, 이용 중인 answer의 index)
available_seat = [] # heap, 사용 가능한 answer의 index

# 현재 시각을 기준으로 for문을 순회
# time complexity: O(M log N)
max_time = -1
for time in times:
    max_time = max(max_time, time[1])
index = 0
for time in range(max_time):
    if index < N and times[index][0] == time:
        if available_seat:
            seat_number = h.heappop(available_seat)
            answer[seat_number] += 1
        else:
            seat_number = len(answer)
            answer.append(1)
        h.heappush(usage, (times[index][1], seat_number))
        index += 1
    elif usage and usage[0][0] == time:
        _, seat_number = h.heappop(usage)
        h.heappush(available_seat, seat_number)
        
print(len(answer))
for result in answer:
    print(result, end= " ")
    
