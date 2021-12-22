"""
211124
실버3 퇴사
url: https://www.acmicpc.net/problem/14501
후기: 점화식 거의 근접한 거 같은데 아니었다.. dp 쉬운 문제부터 다시 연습할 필요가 있다.
"""


# 1차 시도
import sys

N = int(input())
TP = [] # (상담하는데 걸리는 시간, 상담함으로써 받는 금액)
dp = [0 for _ in range(N)]

for _ in range(N):
    TP.append(tuple(map(int, sys.stdin.readline().split())))

index = N - 1 # 뒤에서부터 비교
while index >= 0:
    # index + TP[index][0] - 1 : 해당 index에서 상담이 시작한다면 상담이 끝나는 일자
    if index + TP[index][0] - 1 >= N: # 퇴사 전까지 해결 못하는 상담. -1은 상담 시작일은 빼줘야 하므로
        index -= 1
        continue

    """
    dp[index:index + TP[index][0]] 전부 하고 TP[index][1]하고 크기 비교.
    만약 TP[index][1]이 가장 크면 dp[index] = TP[index][1]. 나머지는 다시 0으로 초기화(상담을 못 받으니)
    그렇지 않다면 pass
    """
    if TP[index][1] > sum(dp[index:index + TP[index][0]]):
        dp[index] = TP[index][1]
        dp[index + 1:index + TP[index][0]] = [0 for _ in range(TP[index][0] - 1)]
    index -= 1
    
print(sum(dp))

"""
반례
5
4 10
2 9
2 3
2 2
3 100
답 11(9 + 2) -> 10이 나옴
"""


# 2차 시도
import sys

N = int(input())
TP = [] # (상담하는데 걸리는 시간, 상담함으로써 받는 금액)
dp = [0 for _ in range(N + 1)] # dp[N] 은 dp[-2] 계산을 위해 0

for _ in range(N):
    TP.append(tuple(map(int, sys.stdin.readline().split())))

index = N - 1 # 뒤에서부터 비교
while index >= 0:
    if index + TP[index][0] - 1 > N - 1:  # 상담 못 하는 날짜
        dp[index] = dp[index + 1]
    else: # 상담할 수 있는 날짜는 상담을 할지 말지 선택.
        # <i번째 일을 할때의 이익( = i번째일의 이익 + i번째 일을 한 후의 이익)>,  <i번째 일을 건너뛰고 i+1번째 일을 할 때의 이익> 비교
        dp[index] = max(dp[index + TP[index][0]] + TP[index][1], dp[index + 1])
    index -= 1
    
print(dp[0])
