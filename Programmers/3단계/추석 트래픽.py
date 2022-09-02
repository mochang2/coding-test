"""
220902
추석 트래픽
url: https://school.programmers.co.kr/learn/courses/30/lessons/17676
후기: 그리디 문제다.
문제를 잘못 읽어서 한 번은 잘못된 방향으로 접근했고, 한 번은 틀렸다.
'1초 동안'을 확인하는 것이 아니라 '특정 시점'을 확인해서 boj의 강의실 배정과 같이 heap을 사용하는 문제로 착각했었고,
그 뒤에 주어진 lines가 '끝난' 시각을 나타내는 것이 아니라 '시작' 시각을 나타내는 것인 줄 알고 틀렸다.

문제의 큰 힌트가 lines가 '끝난' 시각을 기준으로 오름차순되어 있다는 것이다.
line을 하나씩 확인하면서 해당 line이 끝나는 시각에 다른 몇 개의 line이 시작했는지를 확인하면 된다.

모두 날짜가 같기 때문에 datetime을 조금 쉽게 다루기 위해 ms단위로 바꿨다.
"""

def timeToMs(time: str) -> int:
    ms = 0
    hour, minute, rest = time.split(':')
    second, millisecond = rest.split('.')
    
    ms += int(hour) * 60 * 60 * 1000
    ms += int(minute) * 60 * 1000
    ms += int(second) * 1000
    ms += int(millisecond)
    
    return ms

def formatProcessingTime(processingTime: str) -> str:
    if len(processingTime) == 2:
        processedTime = processingTime[:-1] + '.0'
    elif len(processingTime) == 4:
        processedTime = processingTime[:-1] + '00'
    elif len(processingTime) == 5:
        processedTime = processingTime[:-1] + '0'
    elif len(processingTime) == 6:
        processedTime = processingTime[:-1]
    
    return '00:00:0' + processedTime

def solution(lines: list) -> int:
    n = len(lines)
    answer = 0
    starts = []
    ends = []
    
    for line in lines:
        date, time, processingTime = line.split(' ')
        end = timeToMs(time)
        start = end - timeToMs(formatProcessingTime(processingTime)) + 1
        ends.append(end)
        starts.append(start)
    
    for i in range(n): # 각 트래픽이 끝나는 시점 뒤에 몇 개의 트래픽들이 시작됐는지
        count = 0
        interval_end = ends[i]
        
        for j in range(i, n):
            if interval_end > starts[j] - 1000:
                count += 1
        
        answer = max(answer, count)
        
    return answer
  
