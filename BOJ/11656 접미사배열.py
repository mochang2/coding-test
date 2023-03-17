"""
20230317
실버4 접미사 배열
url: https://www.acmicpc.net/problem/11656
후기: 간단히 하나만 풀고 자려고 했는데 너무 간단했다.
모든 단어를 잘라서 배열을 만들고 sort를 하면 된다.
파이썬 짱짱맨
"""

from sys import stdin

word = stdin.readline().strip()
postfixes = [word[index:] for index in range(len(word))]
for postfix in sorted(postfixes):
    print(postfix)
