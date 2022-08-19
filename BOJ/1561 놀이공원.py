"""
20220819
골드2 놀이 공원
url: https://www.acmicpc.net/problem/1561
후기: parametric search 문제임을 알고 풀어도 3번이나 틀리고 3시간이 훌쩍 넘게 걸렸다...

그 이전 시도들은 minute = (min_ + max_) // 2의 시간이 됐을 때 몇 명의 아이들이 놀이기구 탑승을 '완료'했는지를 파악하여
마지막 아이가 타는 놀이기구를 찾으려고 했으나 지속적인 반례가 나왔다.
마지막으로 시도했고 맞은 답이 minute = (min_ + max_) // 2의 시간이 됐을 때 몇 명의 아이들이 놀이기구 탑승을 '시작'했는지를 파악하여
마지막 아이가 타는 놀이기구를 찾았다. 다만 이때 heap을 사용해서 먼저 끝나는 놀이기구가 무엇인지 찾아야 한다.

# 반례
https://hsin.hr/2003/index.html
에서 Regional Competition. 14th March 2003. Seniors의 test data를 들어가면 테스트 데이터를 얻을 수는 있지만 답은 없다.

1987654321 2
15 14
=> 2

24 5
1 2 2 4 4
=> 4

3 5
1 2 3 4 5
=> 3

7 2
3 2
=> 2

22 5
1 2 3 4 5
=> 4

5 3
12 9 11
=> 3

22 5
11 12 8 5 7
=> 4
"""

# (min_ + max_) // 2 분에 몇 명의 아이가 (이미) 놀이기구를 탔는지

import sys
from math import ceil
import heapq as h

input_ = sys.stdin.readline

n, m = map(int, input_().strip().split()) # 아이들 수, 놀이기구 수
operating_hours = list(map(int, input_().strip().split()))
min_ = 1
max_ = ((n * 30) // m) + 1 # 30은 max(operating_hours)

while True:
    minute = (min_ + max_) // 2

    count = 0
    minutes_needed = [] # 힙. 몇 분 후에 다음 아이가 탈 수 있는지, index
    for index, operating_hour in enumerate(operating_hours):
        quotient, remainder = ceil(minute / operating_hour), minute % operating_hour
        count += quotient
        if remainder == 0:
            h.heappush(minutes_needed, (remainder, index + 1))
        else:
            h.heappush(minutes_needed, (operating_hour - remainder, index + 1))
    
    if n - m <= count < n:
        for _ in range(n - count - 1):
            remainder, index = h.heappop(minutes_needed)
            h.heappush(minutes_needed, (remainder + operating_hours[index - 1], index))
        answer = minutes_needed[0] # 마지막 아이는 heap의 0번째 위치에 탐
        print(answer[1]) # index
        sys.exit(0)

    if count >= n:
        max_ = minute - 1
    else:
        min_ = minute + 1

