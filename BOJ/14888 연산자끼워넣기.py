"""
211118
실버1 연산자 끼워넣기
url: https://www.acmicpc.net/problem/14888
후기: dfs 정말 좋은 것 같다. 다시 공부해야겠다. 참고로 permutation을 쓴 풀이도 있다. 소연이꺼 참고하면 됨.
"""

import sys

def dfs(num, index, add, sub, mul, div):
    global N, A_li, Max, Min
    if index == N - 1:
        Max = max(Max, num)
        Min = min(Min, num)
    else:
        if add: # add > 0
            dfs(num + A_li[index + 1], index + 1, add - 1, sub, mul, div)
        if sub:
            dfs(num - A_li[index + 1], index + 1, add, sub - 1, mul, div)
        if mul:
            dfs(num * A_li[index + 1], index + 1, add, sub, mul - 1, div)
        if div: 
            if num >= 0: # div는 c++의 기준을 따른다고 해서 두 가지 경우(음수, 양수)로 나눔
                dfs(num // A_li[index + 1], index + 1, add, sub, mul, div - 1)
            else:
                dfs(-(abs(num) // A_li[index + 1]), index + 1, add, sub, mul, div - 1)


# 인풋 받기
N= int(input())
A_li = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
Max = -1000000000
Min = 1000000000

dfs(A_li[0], 0, add, sub, mul, div)
print(Max)
print(Min)
