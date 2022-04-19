"""
211222
실버2 LCD Test
url: https://www.acmicpc.net/problem/2290
후기: 진짜 별로인 문제였다.
c언어 콘솔처럼 입력시 커서 이동하는 방법을 찾아봤는데 없었다. 그래서 리스트를 활용했다.
근데 첫 번째 방법으로 입력하면 답이 틀린다. 근데 틀린 부분 못 찾겠어서 다른 코드 복붙해왔다...
"""

# 첫 번째 
def one():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                continue
            if j == s + 1:
                li[i][j] = "|"
    return li

def two():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j != 0 and j != s + 1:
                    li[i][j] = "-"
            elif i < s + 1:
                if j == s + 1:
                    li[i][j] = "|"
            else: # i > s + 1
                if j == 0:
                    li[i][j] = "|"     
    return li

def three():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j != 0 and j != s + 1:
                    li[i][j] = "-"
            else:
                if j == s + 1:
                    li[i][j] = "|"    
    return li

def four():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2:
                continue
            if i < s + 1:
                if j == 0 or j == s + 1:
                    li[i][j] = "|"
            elif i == s + 1:
                if j !=0 and j != s + 1:
                    li[i][j] = "-"
            else: # i > s + 1:
                if j == s + 1:
                    li[i][j] = "|"
    return li

def five():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j != 0 and j != s + 1:
                    li[i][j] = "-"
            elif i < s + 1:
                if j == 0:
                    li[i][j] = "|"   
            else: # i > s + 1:
                if j == s + 1:
                    li[i][j] = "|"
    return li

def six():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j != 0 and j != s + 1:
                    li[i][j] = "-"
            elif i < s + 1:
                if j == 0:
                    li[i][j] = "|"   
            else: # i > s + 1:
                if j == 0 or j == s + 1:
                    li[i][j] = "|"
    return li

def seven():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 2 * s + 2 or i == s + 1:
                continue
            if i == 0:
                if j != 0 or j != s + 1:
                    li[i][j] = "-"
            else:
                if j == s + 1:
                    li[i][j] = "|"
    return li

def eight():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j != 0 and j != s + 1:
                    li[i][j] = "-"
            else: # i > s + 1:
                if j == 0 or j == s + 1:
                    li[i][j] = "|"
    return li

def nine():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j != 0 and j != s + 1:
                    li[i][j] = "-"
            elif i < s + 1:
                if j == 0 or j == s + 1:
                    li[i][j] = "|"   
            else: # i > s + 1:
                if j == s + 1:
                    li[i][j] = "|"
    return li

def zero():
    global s
    li = [[" " for _ in range(s + 2)] for __ in range(2 * s + 3)]
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == s + 1:
                continue
            
            if i == 0 or i == 2 * s + 2:
                if j != 0 and j != s + 1:
                    li[i][j] = "-"
            else: # i > s + 1:
                if j == 0 or j == s + 1:
                    li[i][j] = "|"
    return li



import sys
s, n = sys.stdin.readline().strip().split()
s = int(s)

result = [[] for _ in range(2 * s + 3)]
for i in range(2 * s + 3):
    for num in n:
        if num == "1":
            result[i].append("".join(one()[i]))
        elif num == "2":
            result[i].append("".join(two()[i]))
        elif num == "3":
            result[i].append("".join(three()[i]))
        elif num == "4":
            result[i].append("".join(four()[i]))
        elif num == "5":
            result[i].append("".join(five()[i]))
        elif num == "6":
            result[i].append("".join(six()[i]))
        elif num == "7":
            result[i].append("".join(seven()[i]))
        elif num == "8":
            result[i].append("".join(eight()[i]))
        elif num == "9":
            result[i].append("".join(nine()[i]))
        else: # num == "0"
            result[i].append("".join(zero()[i]))
        result[i].append(" ")

for i in range(2 * s + 3):
    #print(result[i])
    print("".join(result[i]))

    
# 두 번째 
s, n = input().split()
s = int(s)
col, row = 2*s+3, s+2
def one(s):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' '*row
        else:
            text[i] += ' ' * (row-1) + '|'
    return text

def two(s):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += ' ' * (row-1) + '|'
            else:
                text[i] += '|' + ' ' * (row-1)
    return text

def three(s):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            text[i] += ' ' * (row-1) + '|'
    return text

def four(s):
    global text
    for i in range(col):
        if i in (0, col-1):
            text[i] += ' '*row
        elif i == s+1:
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += '|' + ' ' * s + '|'
            else:
                text[i] += ' ' * (row-1) + '|'
    return text

def five(s):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += '|' + ' ' * (row-1)
            else:
                text[i] += ' ' * (row-1) + '|'
    return text

def six(s):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += '|' + ' ' * (row-1)
            else:
                text[i] += '|' + ' ' * s + '|'
    return text

def seven(s):
    global text
    for i in range(col):
        if i == 0:
            text[i] += ' ' + '-'*s + ' '
        elif i in (s+1, col-1):
            text[i] += ' '*row
        else:
            text[i] += ' ' * (row-1) + '|'
    return text

def eight(s):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            text[i] += '|' + ' ' * s + '|'
    return text

def nine(s):
    global text
    for i in range(col):
        if i in (0, s+1, col-1):
            text[i] += ' ' + '-'*s + ' '
        else:
            if i < s+1:
                text[i] += '|' + ' ' * s + '|'
            else:
                text[i] += ' ' * (row-1) + '|'
    return text

def zero(s):
    global text
    for i in range(col):
        if i in (0, col-1):
            text[i] += ' ' + '-'*s + ' '
        elif i == s+1:
            text[i] += ' '*row
        else:
            text[i] += '|' + ' ' * s + '|'
    return text

text = [''] * col
func_dict = {
    '0': zero,
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine
}
def run(number):
    func_dict[number](s)
    for i in range(col):
        text[i] += ' '

for i in n:
    run(i)

for i in text:
    print(i)
