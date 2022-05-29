"""
20220529
실버4 괄호
url: https://www.acmicpc.net/problem/9012
후기: 문제 이름이 마음에 들어서 골랐는데, 괄호 문제 중에서 제일 기초적이면서 쉬운 스택(구현) 문제였다.
"""

for _ in range(int(input().strip())):
    stack = [] # 괄호 저장하는 변수
    flag = False
    parenthesis_string = input().strip()
    for char in parenthesis_string:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0 or stack[-1] == ')':
                print('NO')
                flag = True
                break
            else:
                stack.pop()

    if flag:
        continue

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
