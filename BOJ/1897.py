"""
골드5 토달기
url: https://www.acmicpc.net/problem/1897
후기: d <= 1000, 모든 단어의 길이는 80이하이므로 O(d^2 * 80)이면 1억 번 이내에 계산이 가능하다고 판단했다.
하지만 최소 O(d^3)의 알고리즘밖에 생각이 나지 않아 답을 봤다.
"""

# queue를 이용한 풀이
## python은 시간초과해서 pypy로 해야 통과
from collections import deque

d, origin = input().strip().split()
d = int(d)
words = []
first = ""
for i in range(d):
    words.append(input())

queue = deque([origin])
while len(queue) != 0:
    first = queue.popleft()
    first_length = len(first)
    
    for word in words:
        # 이전 단어에 한 글자만 추가해서 만들 수 있는 글자인지 판단하는 로직
        if len(word) != first_length + 1:
            continue
        if word[1:] == first or word[:-1] == first:
            # 추가된 한 글자가 단어의 제일 앞이나 제일 뒤에 추가된 경우
            queue.append(word)
            continue

        # 추가된 한 글자가 단어의 중간에 추가된 경우
        first_index = 0
        word_index = 0
        difference = 0
        while first_index != first_length:
            if first[first_index] == word[word_index]:
                first_index += 1
                word_index += 1
            else:
                if difference == 1:
                    difference += 1
                    break
                difference += 1
                word_index += 1
        if difference == 1:
            queue.append(word)

print(first)
