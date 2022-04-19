"""
211101
실버2 괄호의 값
url: https://www.acmicpc.net/problem/2504
후기: 스택을 잘 써야 됐는데, 규칙을 결국 못 찾아서 포기했다.
"""

import sys
string = sys.stdin.readline().strip()
stack = []
answer = 0

def exit_with_zero():
    print(0)
    sys.exit(0)

for s in string:
    if s == ")":
        tmp = 0
        if len(stack) == 0:
            exit_with_zero()
        while len(stack) != 0:
            top = stack.pop()
            if top == "[":
                exit_with_zero()
            elif top == "(":
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(tmp * 2)
                break
            else:
                tmp += top
            
    elif s == "]":
        tmp = 0
        if len(stack) == 0:
            exit_with_zero()
        while len(stack) != 0:
            top = stack.pop()
            if top == "(":
                exit_with_zero()
            elif top == "[":
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(tmp * 3)
                break
            else:
                tmp += top

    else:
        stack.append(s)


for i in stack:
    if i == '(' or i == '[':
        exit_with_zero()
    else:
        answer += i

print(answer)
