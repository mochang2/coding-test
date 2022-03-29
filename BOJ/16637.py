"""
골드3 괄호 추가하기
url: https://www.acmicpc.net/problem/16637
후기: 근래 풀은 빡구현보다 어려웠다
예전에 비슷한 문제를 푼 적이 있었는데(번호는 기억이 안 남), 그 때는 괄호가 중첩될 수 있어서 연산의 우선순위를 정해줌으로써 풀었었다.
하지만 이 문제는 중첩이 안 돼서 우선순위로 풀 수 없을 것 같았고, 모든 경우의 수를 구해보니 0.5초 안에 브루트 포스로 풀 수 있을 것 같았다.

해결의 요점
1. 모든 연산의 길이를 19로 동일하게 만듦(+0을 붙여도 연산 결과에는 지장이 없으므로)
2. 각각의 연산에 대해 bit 값으로 정의. 해당 연산을 먼저 하는 괄호를 씌우면 그 연산의 bit값이 1이라고 가정
3. 만약 위 bit 값이 연속적으로 존재(0b00110000~, 0b1111100) 이런 식이면 괄호 안에 여러 연산이 들어가므로 pass
4. 괄호에 대한 연산을 할 때 인덱싱으로 접근하므로 뒤에서부터 계산 결과를 변경
5. 최종 연산할 때 왼쪽부터 연산(파이썬 문자 슬라이싱 최고)
6. 단, 최종 연산할 때 괄호를 먼저 연산했던 것으로 인해 음수값이 나오는 것에 대한 처리
7. answer의 초기값은 0이 아닌 아주 작은 수여야 함 => 이것 때문에 1번 틀림
"""

# -를 기점으로 나눈뒤 먼저 더하고 그 뒤에 곱하면 될 줄 알았는데...
# 괄호 중첩이 안됨 + 괄호 안에 연산자 1개만 + O(N) = 19 => 완탐 가능.
# 비트 연산으로 완탐.
# 음수 다루는 곳에서 문제가 좀 있었음.

import sys

def Calc(num1, num2, operator):
    if operator == "+":
        return str(int(num1) + int(num2))
    elif operator == "-":
        return str(int(num1) - int(num2))
    elif operator == "*":
        return str(int(num1) * int(num2))
    else:
        return

def FormulaToNum(formula):
    while True:
        break_condition = formula[1:]
        if "+" not in break_condition and "-" not in break_condition and "*" not in break_condition:
            return int(formula)
        
        for index, char in enumerate(formula):
            if (char == "+" or char == "-" or char == "*") and index != 0: # 계산할 첫 번째 수가 음수면 예외 처리
                next_index = index + 1
                
                if next_index < len(formula) and formula[next_index] == "-": # 계산할 두 번째 수가 음수면 예외 처리
                    next_index += 1
                while next_index < len(formula) and formula[next_index].isdigit():
                    next_index+=1

                formula = Calc(formula[:index], formula[index + 1: next_index], char) + formula[next_index:]
                break # 연산 하나 수행하고 while True로 돌아가기 위해
            
# initialization
answer = -sys.maxsize
max_len = 19
N = int(input()) # (N + 1 // 2): 숫자의 개수
formula = input()
for _ in range((19 - N) // 2):
    formula+="+0"

for i in range(512): #숫자의 개수가 10개이므로, 최대 2^9 경우의 수
    if i & 0b110000000 == 0b110000000 or i & 0b011000000 == 0b011000000 \
       or i & 0b001100000 == 0b001100000 or i & 0b000110000 == 0b000110000 \
       or i & 0b000011000 == 0b000011000 or i & 0b000001100 == 0b000001100 \
       or i & 0b000000110 == 0b000000110 or i & 0b000000011 == 0b000000011 :
        continue
    
    one_bit_pos = bin(i)[2:]
    one_bit_pos = one_bit_pos.zfill(max(10 - len(one_bit_pos), 9))
    tmp_formula = formula
    for index, pos in enumerate(one_bit_pos[::-1]): # O(9), index slicing을 하므로 뒤에서부터 바꾸게. 
        if pos == "0":
            continue
        
        if index == 0: # replace는 기본적으로 앞에서부터 바꾸므로 사용하지 못 함.
            tmp_formula = tmp_formula[:16] + Calc(formula[16], formula[18], formula[17])
        elif index == 1:
            tmp_formula = tmp_formula[:14] + Calc(formula[14], formula[16], formula[15]) + tmp_formula[17:]
        elif index == 2:
            tmp_formula = tmp_formula[:12] + Calc(formula[12], formula[14], formula[13]) + tmp_formula[15:]
        elif index == 3:
            tmp_formula = tmp_formula[:10] + Calc(formula[10], formula[12], formula[11]) + tmp_formula[13:]
        elif index == 4:
            tmp_formula = tmp_formula[:8] + Calc(formula[8], formula[10], formula[9]) + tmp_formula[11:]
        elif index == 5:
            tmp_formula = tmp_formula[:6] + Calc(formula[6], formula[8], formula[7]) + tmp_formula[9:]
        elif index == 6:
            tmp_formula = tmp_formula[:4] + Calc(formula[4], formula[6], formula[5]) + tmp_formula[7:]
        elif index == 7:
            tmp_formula = tmp_formula[:2] + Calc(formula[2], formula[4], formula[3]) + tmp_formula[5:]
        elif index == 8:
            tmp_formula = Calc(formula[0], formula[2], formula[1]) + tmp_formula[3:]

    # 음수 처리
    tmp_formula = tmp_formula.replace("+-", "-")
    tmp_formula = tmp_formula.replace("--", "+")

    result = FormulaToNum(tmp_formula)
    answer = max(answer, result)
    
print(answer)
