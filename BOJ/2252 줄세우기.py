"""
20230401
골드3 줄 세우기
url: https://www.acmicpc.net/problem/2252
후기: 위상 정렬 문제다.
처음에는 그리디? DP? 고민하다가 트리 같나? 근데 단방향 간선이네? 라는 생각이 미치니 위상 정렬이라고 느껴졌다.
근데 문제는 위상 정렬 푸는 방법이 기억이 안 났다는 것... 그래서 다른 위상 정렬 알고리즘을 검색해서 해결했다.

기본적으로 위상 정렬은 (in, out)degree를 가지고 있다.
in_degree가 0인 node부터 queue에 집어넣는다.
이후 해당 node로부터 이어지는 다음 node들을 방문한다.
만약 그 방문으로 인해 다음 node들의 in_degree가 0이 되면 그 node들도 queue에 집어넣는다.
queue가 빌 때까지 이 행동을 반복한다.

이 문제도 비슷한 방식으로 해결했다.
degrees는 {'in_count': 'in_degree의 개수', 'out': 'out_degree들의 index[]'}와 같이 선언했다.
degrees[index]['in_count'] == 0인 node들을 deque에 넣고 계속해서 새로운 node를 방문, 'in_count'가 다시 0이 되는지 확인함으로써 문제를 해결했다.
"""

from sys import stdin
from collections import deque

def getBasicInformation():
    number_of_students, number_of_comparisons = map(int, stdin.readline().strip().split())

    return initializeDegrees(number_of_students, number_of_comparisons)

def initializeDegrees(number_of_students, number_of_comparisons):
    degrees = [{'in_count': 0, 'out': []} for _ in range(number_of_students)]

    for _ in range(number_of_comparisons):
        before, after = map(lambda number: int(number) - 1, stdin.readline().strip().split())
        degrees[after]['in_count'] += 1
        degrees[before]['out'].append(after)

    return degrees


def lineUp(degrees):
    line = initializeLine(degrees)

    while len(line) != 0:
        student = line.popleft()

        for next_student in degrees[student]['out']:
            degrees[next_student]['in_count'] -= 1

            if degrees[next_student]['in_count'] == 0: # 앞선 node들이 전부 시작됐을 때, 다시 시작점으로 지정 가능한 node라면
                print(next_student + 1, end=" ") # 입력받을 때 1씩 뺐으므로
                line.append(next_student)

def initializeLine(degrees): # 위상 정렬에서 시작점으로 지정 가능한 node들을 지정
    number_of_students = len(degrees)
    line = deque(filter(lambda index: degrees[index]['in_count'] == 0, range(number_of_students)))

    printStudents(line)

    return line

def printStudents(line):
    for student in line:
        print(student + 1, end=" ") # 입력받을 때 1씩 뺐으므로

degrees = getBasicInformation()
lineUp(degrees)

