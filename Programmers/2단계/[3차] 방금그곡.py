"""
221014
url: https://school.programmers.co.kr/learn/courses/30/lessons/17683
후기: 정신이 나갈 것 같다. 실제 시험에서 마주했으면 카카오 1솔 탈이다...
10번은 넘게 틀린 것 같다.

1. new_melody의 길이를 어디까지 늘려야 할지 기준을 잘 잡았어야 한다. new_m과 길이를 비교해서 25번이 계속 틀렸었다.
2. E#이 존재한다고 한다? 27번 테스트 케이스 문제인데 나는 문제가 없었다.
3. '음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.' 멜로디가 재생 시간보다 길면 잘라줘야 한다. 30번 테스트 케이스이다.
"""

# C# -> H
# D# -> I
# F# -> J
# G# -> K
# A# -> L

def calcTimeDifference(start, end):
    start_hour, start_minute = map(int, start.split(':'))
    end_hour, end_minute = map(int, end.split(':'))
    
    start_time = start_hour * 60 + start_minute
    end_time = end_hour * 60 + end_minute
    
    return end_time - start_time

def changeNote(melody):
    result = ''
    
    for index in range(len(melody) - 1):
        if melody[index] == '#':
            continue
            
        note = melody[index:index + 2]
            
        if note == 'C#':
            result += 'H'
        elif note == 'D#':
            result += 'I'
        elif note == 'F#':
            result += 'J'
        elif note == 'G#':
            result += 'K'
        elif note == 'A#':
            result += 'L'
        else:
            result += melody[index]
            
    if melody[-1] != '#':
        result += melody[-1]
    
    return result

def solution(m, musicinfos):
    answers = [] # (재생된 시간, 입력 순서, 제목)
    
    new_m = changeNote(m)
    
    for index, musicinfo in enumerate(musicinfos):
        start_time, end_time, title, melody = musicinfo.split(',')
        new_melody = changeNote(melody)
        run_time = calcTimeDifference(start_time, end_time)
        
        while len(new_melody) < run_time:
            new_melody *= 2

        new_melody = new_melody[:run_time]

        if new_m in new_melody:
            answers.append((run_time, index, title))
            
    answers.sort(key=lambda x: (-x[0], x[1]))
    
    return answers[0][2] if len(answers) != 0 else '(None)'
