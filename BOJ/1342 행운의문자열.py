"""
20230331
실버1 행운의 문자열
url: https://www.acmicpc.net/problem/1342
후기: 완전 탐색 문제다.
나는 파이썬에서 제공하는 itertools.permutations와 set을 이용해 완전 탐색해 3000ms 정도 걸렸다.

하지만 훨씬 빠르게 완전 탐색하는 방법도 존재한다(나는 안 풀었지만 참고할 만한 블로그 주소는 https://nato-blog.tistory.com/95 이다).
1. permutations를 직접 구현하며 string[index] != string[index + 1]이면 permutations을 중단한다.
2. index 위치에 특정 알파벳이 왔다면 체크한다. 이후에 그 위치에 해당 알파벳이 다시 온다면 permutations을 중단한다. 이미 중복 문자열이 존재하기 때문이다.
"""

# 시간 초과는 나지 않았지만 느린 정답

from sys import stdin
from itertools import permutations

def isLuckyString(string):
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            return False

    return True

answer = set()
original_string = stdin.readline().strip()

for permutation in permutations(original_string, len(original_string)):
    new_string = ''.join(permutation)
    
    if isLuckyString(new_string):
        answer.add(new_string)

print(len(answer))
