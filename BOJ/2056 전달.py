"""
골드4 전달
211223
url: https://www.acmicpc.net/submit/2056/36601622
후기: 위상 정렬 문제였으나 위상 정렬이 아닌 다른 방식으로 풀었다. DP 방식도 아니라서 파이썬 인터프리터로는 시간 초과가 난 것 같다.
그치만 똑같은 코드를 pypy로 돌리니까 맞았다. 반복적인 작업은 pypy가 훨씬 빠르다고 한다.
"""

# 첫 번재 제출. 결국 pypy로 돌리니까 맞았다.
import sys

time = 0  # 걸리는 시간
finished = 0  # 작업이 끝난 일의 수
N = int(input())
works =[[] for _ in range(N)]
for i in range(N):
    # works: 3차원 배열
    # 2차원 배열은 [걸리는_시간, [남은 일들]]로 구성됨
    temp = list(map(int, sys.stdin.readline().strip().split()))
    works[i].append(temp[0])
    works[i].append(temp[2:])

while finished != N:
    possible_works = []  # 실행 가능한 일들을 모아두는 배열
    min_time = 100  # 실행 가능한 일들 중에서 가장 짧은 작업 시간
    for index, work in enumerate(works):
        if work[0] > 0 and len(work[1]) == 0:
            # 해결된 작업이 아니면서 앞선 작업들이 전부 끝났다면 실행 가능한 일임
            possible_works.append(index)
            min_time = min(work[0], min_time)

    time += min_time
    for possible_work in possible_works:
        works[possible_work][0] -= min_time
        if works[possible_work][0] <= 0:
            finished += 1
            for work in works:
                try:
                    work[1].remove(possible_work + 1)
                except:
                    pass

print(time)


# 두 번재 시도. set을 써봤다. 이것도 결국 pypy로 돌리니까 맞았다.
import sys

time = 0  # 걸리는 시간
finished = set()
finished_len = 0  # 작업이 끝난 일의 수
N = int(input())
works =[[] for _ in range(N)]
for i in range(N):
    # works: 3차원 배열
    # 2차원 배열은 [걸리는_시간, {남은 일들}]로 구성됨
    temp = list(map(int, sys.stdin.readline().strip().split()))
    works[i].append(temp[0])
    works[i].append(set(temp[2:]))

while finished_len != N:
    possible_works = []  # 실행 가능한 일들을 모아두는 배열
    min_time = 100  # 실행 가능한 일들 중에서 가장 짧은 작업 시간
    for index, work in enumerate(works):
        if work[0] > 0 and work[1].issubset(finished):
            # 해결된 작업이 아니면서 앞선 작업들이 전부 끝났다면 실행 가능한 일임
            possible_works.append(index)
            min_time = min(work[0], min_time)

    time += min_time
    for possible_work in possible_works:
        works[possible_work][0] -= min_time
        if works[possible_work][0] <= 0:
            finished_len += 1
            finished.add(possible_work + 1)

print(time)
