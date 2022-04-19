"""
220101
골드5 센서
url: https://www.acmicpc.net/problem/2212
후기: (그리디 문제)우선 문제 이해가 안 됐다. 그래서 질문들을 보고 이해했다.
거의 근접했다고 생각했으나 훨씬 간단한 방법이 있었고, index out of range를 결국 해결 못 해 답을 봤다.
"""

# 첫 번째 시도
## 100%에서 index out of range가 남
import sys
import heapq as h

N = int(input())  # 센서
K = int(input())  # 집중국

placement = list(map(int, sys.stdin.readline().strip().split()))
placement.sort()
distance = []
heap = [[-1, -1]]   # 거리가 가장 긴 것들 K - 1개를 heap에 넣고 해당 heap을 기준으로 거리를 계산하려고 함.
h.heapify(heap)

for i in range(N - 1):
    temp = placement[i + 1] - placement[i]
    distance.append(temp)
    if len(heap) < K - 1:
        h.heappush(heap, [temp, i])
    else:
        if temp > heap[0][0]:
            h.heapreplace(heap, [temp, i])

index = []
for i in range(K - 1):
    index.append(heap[i][1])
index.sort()

if K == 1:
    print(placement[-1] - placement[0])
else:
    answer = 0
    temp_li = placement[:index[0] + 1]
    answer += (temp_li[-1] - temp_li[0])
    for i in range(len(index) - 1):
        temp_li = placement[index[i] + 1:index[i + 1] + 1]
        answer += (temp_li[-1] - temp_li[0])
    temp_li = placement[index[-1] + 1:]
    answer += (temp_li[-1] - temp_li[0])
    print(answer)


# 두 번째 시도
## 정답
import sys

N = int(input())  # 센서
K = int(input())  # 집중국

placement = list(map(int, sys.stdin.readline().strip().split()))
placement.sort()
distance = []

for i in range(N - 1):
    distance.append(placement[i + 1] - placement[i])
distance.sort()

answer = 0
for i in range(N - K):
    answer += distance[i]
print(answer)
