"""
220902
추석 트래픽
url: https://school.programmers.co.kr/learn/courses/30/lessons/17676
후기: 그리디 문제다.
문제를 잘못 읽어서 틀렸다. 주어진 lines는 트래픽이 '끝난' 시각, '걸린' 시간을 담고 있다.
문제의 큰 힌트가 lines가 '끝난' 시각을 기준으로 오름차순되어 있다는 것이다.
1초가 되는 시각과 비교해야 되는 line들을 비교할 때 end를 기준으로 비교하면 된다.

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
  
