"""
221017
url: https://school.programmers.co.kr/learn/courses/30/lessons/17678
후기: 그리디 문제였다.
힙을 사용해서 버스 시각마다 탈 수 있는 애들을 우선적으로 태우고,
만약 해당 시각에 인원이 가득 차지 않았으면 콘은 버스 도착 시각에 도착하면 된다.
만약 해당 시각에 인원이 가득 찼다면 가장 늦게 도착한 애보다 1분만 먼저 도착하면 된다.

m == 1인 경우를 간과해서 틀렸고, '질문하기'에서 반례를 보고 착각한 부분을 알 수 있었다.
len(crews) == m: (콘 없이 인원이 가득 찼을 때) last_time = max(crews) - 1이 아닌 last_time = secondLargest(crews)을 했었다.
(실전이었으면 생각할 수 있었을까...)


<반례>
n = 10
t = 25
m = 1
timetable = [
    "09:00", "09:10", "09:20" ,"09:30" ,"09:40" ,"09:50",
    "10:00", "10:10" ,"10:20" ,"10:30" ,"10:40" ,"10:50"
]

answer: "10:29"
"""

import heapq as h

def changeToMinutes(time = '09:00'):
    hour, minute = map(int, time.split(':'))
    
    return hour * 60 + minute

def changeToTime(minute):
    hour, minute_ = minute // 60, minute % 60
    
    return str(hour).zfill(2) + ':' + str(minute_).zfill(2)
    
def solution(n, t, m, timetable):
    minutes = list(map(changeToMinutes, timetable))
    h.heapify(minutes)
    last_time = max(0, minutes[0] - 1) # 탈 수 있는 가장 마지막 시각. 정답
    bus_times = [changeToMinutes() + index * t for index in range(n)] # 버스 도착 시각
    
    for bus_time in bus_times:
        crews = [] # 셔틀에 탄 크루들의 도착 시각. 오름차순 정렬됨
        
        while len(crews) < m and \
            len(minutes) and \
            minutes[0] <= bus_time:
            crews.append(
                h.heappop(minutes)
            )
        
        if len(crews) == m: # 콘 없이 인원이 다 참
            last_time = max(crews) - 1
        else: # len(crews) != m: # 콘 없이 인원이 다 차지 않음
            last_time = bus_time
    
    return changeToTime(last_time)
