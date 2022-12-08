"""
211101
실버2 괄호의 값
url: https://www.acmicpc.net/problem/2504
후기: 스택을 잘 써야 됐는데, 규칙을 결국 못 찾아서 포기하고 답을 봤다.

+) 221208 채점이 다시 되어서 수정했다.
()]() 입력을 받으면 0이 아닌 2를 출력했었다.
for문을 돌 때 만나는 char이 ) 또는 ]일 때 그 이전 계산 결과가 숫자이고, 그 앞에 다른 숫자나 닫는 괄호가 없을 때의 예외를 처리해줬다.
"""

from sys import exit, stdin

parenthesis = {
    2: {
        'open': '(',
        'close': ')'
    },
    3: {
        'open': '[',
        'close': ']'
    }
}

def getInput():
    return stdin.readline().strip()

def convert(string):
    expressions = []
    tmp = 0

    for char in string:
        if char == parenthesis[2]['close']:
            cannot_close_parenthesis = len(expressions) == 0
            if cannot_close_parenthesis:
                return getEmptyList()

            tmp = 0
            
            while len(expressions) != 0:
                last_expression = expressions.pop()
                
                if last_expression == parenthesis[3]['open']:
                    return getEmptyList()
                elif last_expression == parenthesis[2]['open']:
                    if tmp == 0:
                        expressions.append(2)
                    else:
                        expressions.append(tmp * 2)
                    break
                else:
                    not_single_close = len(expressions) != 0
                    if not_single_close:
                        tmp += last_expression
                    else:
                        return getEmptyList()
                
        elif char == parenthesis[3]['close']:
            cannot_close_parenthesis = len(expressions) == 0
            if cannot_close_parenthesis:
                return getEmptyList()

            tmp = 0
            
            while len(expressions) != 0:
                last_expression = expressions.pop()
                
                if last_expression == parenthesis[2]['open']:
                    return getEmptyList()
                elif last_expression == parenthesis[3]['open']:
                    if tmp == 0:
                        expressions.append(3)
                    else:
                        expressions.append(tmp * 3)
                    break
                else:
                    not_single_close = len(expressions) != 0
                    if not_single_close:
                        tmp += last_expression
                    else:
                        return getEmptyList()

        else:
            expressions.append(char)

    return expressions

def getEmptyList():
    return []

def calculate(numbers):
    result = 0
    
    for number in numbers:
        if type(number) == int:
            result += number
        else:
            return 0

    return result

parentheses = getInput()
numbers = convert(parentheses)
answer = calculate(numbers)

print(answer)
