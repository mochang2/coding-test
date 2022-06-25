"""
20220625
실버4 스택
url: https://www.acmicpc.net/problem/10828
후기: 엄청 쉬운 스택 구현이었다. 파이썬의 list가 이미 stack이어서 쉬웠다.
"""

import sys

def Push(li, n):
    li.append(n)

def Pop(li):
    if li:
        return li.pop()
    else:
        return -1

def Size(li):
    return len(li)

def Empty(li):
    if li:
        return 0
    else:
        return 1
    
def Top(li):
    if li:
        return li[-1]
    else:
        return -1

N = int(sys.stdin.readline().strip())
stack = []
for _ in range(N):
    operation = sys.stdin.readline().strip().split()
    if operation[0] == 'push':
        Push(stack, operation[1])
    elif operation[0] == 'pop':
        print(Pop(stack))
    elif operation[0] == 'size':
        print(Size(stack))
    elif operation[0] == 'empty':
        print(Empty(stack))
    elif operation[0] == 'top':
        print(Top(stack))
