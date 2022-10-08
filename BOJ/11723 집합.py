"""
20221008
실버5 집합
url: https://www.acmicpc.net/problem/11723
후기: 비트마스킹 문제이다.
간단히 list를 선언해서 해결이 되지만 13701, 2098 비트마스킹 문제를 풀기 전 몸 풀기로 시도해봤다.
all_()를 변수에 저장해두지 않으면 시간 초과가 나서 메모리에 저장해서 해결했다.
"""

# 20 19 18 ... 1

import sys

input_ = sys.stdin.readline
LENGTH = 20

def all_():
    global LENGTH

    result = 0
    for i in range(LENGTH):
        result += 2 ** i

    return result

def isIn(bits, x):
    return (bits & 1 << (x - 1) != 0)

def empty():
    return 0

MAX = all_()
value = empty()

for _ in range(int(input_().strip())):
    command = input_().strip().split()
    execution = command[0]
    
    if execution == 'add' or \
       execution == 'remove' or \
       execution == 'check' or \
       execution == 'toggle':
        x = int(command[1])
        in_ = isIn(value, x)

        if execution == 'add':
            if not in_:
                value += 1 << (x - 1)
        elif execution == 'remove':
            if in_:
                value -= 1 << (x - 1)
        elif execution == 'check':
            if in_:
                print(1)
            else:
                print(0)
        else: # execution == 'toggle'
            if in_:
                value -= 1 << (x - 1)
            else:
                value += 1 << (x - 1)
        
    elif execution == 'all':
        value = MAX
        
    elif execution == 'empty':
        value = empty()

