"""
20220709
플래티넘4 숫자의 신
url: https://www.acmicpc.net/problem/1422
후기: 이미 비슷한 문제를 풀어봐서 그런지 플래티넘4까지는 아닌 문제 같다.
처음에는 중복 조합을 이용하는 백트래킹인 줄 알았으나 그렇게 풀면
50H50(==99C50) 이라는 택도 없는 시간 복잡도를 가진다.
그러면 처음부터 입력받은 수를 어떤 기준을 잘 정렬하면 되지 않을까? 라는 생각이 들면서 옛날에
프로그래머스(문제는 기억이 안남)에 있던 string형 숫자를 정렬하는 방법에 대한 문제가 기억이 났다.

함수를 이용해 list를 정렬하는 cmp_to_key 사용법이 기억나지 않아서 검색이 필요했다.
String class는 isBiggerOrEqual의 의미(비교되는 숫자가 큰지, 비교하는 숫자가 큰지)를 더 살리기 위해 정의했다.

num1 = '222'
num2 = '223'

num1 = '222'
num2 = '225'

num1 = '22'
num2 = '234'

num1 = '25'
num2 = '219'

이러한 숫자들에 대한 정렬은 num1 + num2와 num2 + num1을 비교함으로써 해결할 수 있다.
"""

# 무조건 1번씩만 사용할 수 있을 경우를 가정하고 숫자를 정렬. 정렬 기준은 위 주석에 정리.
# list에서 index가 가장 작으면서 len이 가장 큰 숫자 하나를 결정. 그 애를 최대한 많이 이어 붙이기.

import sys
from functools import cmp_to_key

input_ = sys.stdin.readline

class String(str):
    def isBiggerOrEqual(self: str, num: str) -> bool:
        if len(self) != len(num): # 길이 비교
            sys.exit(-1)
        
        for index in range(len(self)):
            if self[index] > num[index]: # 한 자리씩 비교
                return True 
            elif self[index] < num[index]:
                return False
            
        return True # Equal

def compare(num1: str, num2: str) -> int:
    number1 = String(num1 + num2)
    number2 = String(num2 + num1)
    
    if number1.isBiggerOrEqual(number2):
        return -1
    else:
        return 1

def findBiggestIndex(numbers: list) -> int:
    index = 0

    for i in range(1, len(numbers)):
        if len(numbers[i]) > len(numbers[index]):
            index = i

    return index

def makeAnswer(numbers: list, K: int, N: int) -> str:
    index = findBiggestIndex(numbers)

    result = ''
    for i in range(K):
        if i == index:
            result += numbers[i] * (N - K)
        result += numbers[i]
    
    return result

# initialization
K, N = map(int, input_().strip().split())
numbers = [input_().strip() for _ in range(K)]
numbers.sort(key=cmp_to_key(compare))

# print
print(makeAnswer(numbers, K, N))
