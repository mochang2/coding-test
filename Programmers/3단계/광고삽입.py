"""
221013
url: https://school.programmers.co.kr/learn/courses/30/lessons
후기: 누적합 문제였다.
힙이나 그리디와 같은 문제일거라 고민하다가 해결이 안돼서 결국 답을 봤다.
https://dev-note-97.tistory.com/156 를 참고했다.

중간에 answer에 대한 연산을 놓친 부분이 있는지... 시간이 00:00:00부터 시작해서 answer += 1 조건이 필요했다.
"""

def getSeconds(time):
    hour, minute, second = map(int, time.split(':'))
    
    return hour * 3600 + minute * 60 + second

def changeToSeconds(time):
    start, end = time.split('-')
    
    return getSeconds(start), getSeconds(end)

def changeToTime(second):
    hour, left = second // 3600, second % 3600
    minute, left = left // 60, left % 60

    return str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(left).zfill(2)

def solution(play_time, adv_time, logs):
    max_overlap_time = 0
    answer = -1
    
    play_time_in_seconds = getSeconds(play_time)
    play_time_in_seconds += 1 # 00:00:00부터 시작하므로
    adv_time_in_seconds = getSeconds(adv_time)
    logs_in_seconds = map(changeToSeconds, logs)

    time_in_seconds = [0 for _ in range(play_time_in_seconds)] # 누적 시청자 수 저장

    # 시작, 끝 시각 표시
    for start_time, end_time in logs_in_seconds:
        time_in_seconds[start_time] += 1
        time_in_seconds[end_time] -= 1

    # 구간 시청자 수 계산
    for second in range(1, play_time_in_seconds):
        time_in_seconds[second] += time_in_seconds[second - 1]
        
    # 누적 시간 계산
    for second in range(1, play_time_in_seconds):
        time_in_seconds[second] += time_in_seconds[second - 1]

    # 누적 시간이 가장 큰 구간 계산 
    for second in range(play_time_in_seconds):
        if second + adv_time_in_seconds < play_time_in_seconds:
            accumulative_time = time_in_seconds[second + adv_time_in_seconds] - time_in_seconds[second]
        else:
            accumulative_time = time_in_seconds[-1] - time_in_seconds[second]

        if accumulative_time > max_overlap_time:
            max_overlap_time = accumulative_time
            answer = second

    if answer != 0: # 시작 시각이 00:00:00이 있어서 예외처리 
        answer += 1
        
    return changeToTime(answer)
  
  
