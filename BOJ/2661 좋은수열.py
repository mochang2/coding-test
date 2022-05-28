"""
20220528
골드4 좋은수열
url: https://www.acmicpc.net/problem/2661
후기: 문제를 고르다가 백트래킹이라는 것을 알고 풀었다. 그래서 훨씬 접근이 쉬웠던 것 같다.
경우의 수가 너무 많으므로 모든 경우를 따지는 것은 안되고, N자릿수까지 하나씩 숫자를 늘렸을 때
매번 반복되는 구간이 있는지 확인하는 게 제일 나을 거라고 판단했다.
또한 가장 작은 수를 return하라고 했으니 제일 높은 자릿수는 무조건 1이면 될 거라고 판단했다.
"""

# O(3 ** N) = 147808829414345923316083210206383297601이므로 줄일 방법 필요
# 앞 자리와 같은 수가 올 수 없음
# ex) n번째 자리가 1이면 n + 1번째 자리는 2 또는 3이어야 함
# 모든 경우를 찾을 필요가 없으므로 작은 수부터 넣으면 될 듯

def CheckIfGood(sequence):
    length = len(sequence)
    for i in range(1, (length // 2) + 1):
        if sequence[length - (2 * i):length - i] == sequence[length - i:]:
            return False
    return True

def BackTrack(index, sequence):
    if index == N:
        if not CheckIfGood(sequence):
            return
        return sequence

    if not CheckIfGood(sequence): # 수열내에 반복되는 구간이 나옴
        return

    for i in range(1, 4):
        char = str(i)
        if sequence[-1] == char: # 앞 자리와 같은 수가 올 수 없음
            continue
        answer = BackTrack(index + 1, sequence + char)
        if answer and len(answer) == N: # None을 받았는지 확인하기 위함
            return answer

N = int(input())
print(BackTrack(1, '1'))
