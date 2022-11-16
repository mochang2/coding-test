"""
20221115
플레5 찾기
url: https://www.acmicpc.net/problem/1786
후기: 문자열 알고리즘이다. 참고로 이 문제는 문자열 예시에 공백도 존재하므로 input_().strip()으로 입력을 받으면 안 된다.
추가적으로 입력받을 때 replace가 아니라 rstrip을 사용하면 입력값을 순회를 할 필요가 없기 때문에 더 빠르다.
KMP에 대해서 공부하다가 이 문제가 KMP를 사용하는 문제라고 해서 풀어봤다.

KMP는 접두사와 접미사가 일정 길이만큼 일치하는지를 KMP_table에 담아놓고 해당 table을 이용하는 알고리즘이다.
찾아야 하는 문자열을 pattern, 찾는 위치를 text라고 할 때 일반적인 탐색은 O(len(pattern) * len(text))이지만,
KMP를 이용한다면 O(len(text))에 찾을 수 있다.
더 자세한 설명은 https://www.youtube.com/watch?v=yWWbLrV4PZ8 , https://bowbowbow.tistory.com/6 를 이용하자.

KMP 알고리즘을 이용한 첫 번째 코드는 실패했다.
KMP_table 구하는 공식만 보고 구했다가 start_index를 찾는 부분에서 비효율성이 발생했다.
만약 'ababab'에서 'abab'를 찾고자 할 때, 'ababab'의 0번째 index에서 찾았다면 1번째 index가 아닌 2번째 index에서부터 다시 찾는게 더 효율적일 것이다.
그런데 첫 번째 시도는 1번째 index부터 찾아서 시간 초과가 났다.

두 번째 코드는 KMP 알고리즘을 이용해서 성공했다.

Rabin Karp 알고리즘을 이용한 세 번째 코드는 실패했다.
이 문제는 KMP를 위한 문제이지만 라빈 카프를 적용할 수 있고, 해당 내용이 문자열 탐색에는 더 직관적인 알고리즘 같아서 시도해봤다.
하지만 지속적인 시간 초과가 났다.
https://www.acmicpc.net/source/26975317 를 참고하여 다른 점이 무엇인가 계속 시도해봤다.
MAX 값, input.replace -> input.rstrip으로 변경, power 구하는 방법 변경 등 각종 다양한 방법을 시도했지만 실패했다.

네 번째 코드는 Rabin Karp 알고리즘을 이용해서 성공했다.
세 번째 코드와 달랐던 점은 해시 충돌을 무시하는 것이었다.
세 번째 코드에서는 해시가 일치하면 해시 충돌일 수도 있으므로 text를 슬라이싱하여 pattern과 비교하는 작업을 했다.
그 부분이 시간 초과를 야기했었고, 해당 부분을 제거하니 오히려 KMP 보다 빠른 속도로 성공할 수 있었다.
"""

# 첫 번째 KMP
# 오답. 시간 초과
# start_index를 찾는 부분에서 비효율성 발생

import sys

input_ = sys.stdin.readline

def getKMPTable(string):
    KMP_table = [0] * len(string)
    left = 0

    for right in range(1, len(string)):
        while left > 0 and string[left] != string[right]:
            left = KMP_table[left - 1]

        if string[left] == string[right]:
            left += 1
            KMP_table[right] = left

    return KMP_table

def getStartIndexes(target, pattern):
    KMP_table = getKMPTable(pattern)
    
    start_indexes = []
    target_index = 0
    pattern_index = 0

    while target_index < len(target):
        target_char = target[target_index]
        
        while pattern_index > 0 and pattern[pattern_index] != target_char:
            pattern_index = KMP_table[pattern_index - 1]

        if pattern[pattern_index] == target_char:
            pattern_index += 1

            if pattern_index >= len(pattern): # 부분 문자열 발견
                start_index = target_index - len(pattern) + 1
                start_indexes.append(start_index + 1) # index가 1부터 시작하는 문제라서

                target_index = start_index
                pattern_index = 0

        target_index += 1

    return start_indexes

def printAnswer(start_indexes):
    print(len(start_indexes))

    for index in start_indexes:
        print(index, end=' ')

# get input
target = input_().strip()
pattern = input_().strip()

# KMP algorithm
start_indexes = getStartIndexes(target, pattern)
printAnswer(start_indexes)



# 두 번째 KMP
# 정답
## 전체적으로 pattern을 가리키는 index를 0으로 바로 이동하지 않는 이유는
## 더 효율적으로 index를 이동시키기 위함

import sys

input_ = sys.stdin.readline

def getKMPTable(string):
    KMP_table = [0] * len(string)
    left = 0

    for right in range(1, len(string)):
        # 일치하지 않는다면 right는 KMP_table[right - 1]이 가리키는 위치로 이동
        while left > 0 and string[left] != string[right]:
            left = KMP_table[left - 1]

        # 일치하면 left + 1이 KMP_table 값, left + 1, right + 1
        if string[left] == string[right]:
            left += 1
            KMP_table[right] = left

    return KMP_table

def getStartIndexes(text, pattern):
    KMP_table = getKMPTable(pattern)
    
    start_indexes = []
    pattern_index = 0

    for text_index, text_char in enumerate(text):
        # 일치하지 않는다면 pattern_index는 KMP_table[pattern_index - 1]이 가리키는 위치로 이동
        while pattern_index > 0 and pattern[pattern_index] != text_char:
            pattern_index = KMP_table[pattern_index - 1]

        if pattern[pattern_index] == text_char:
            if pattern_index != len(pattern) - 1: # 아직은 부분 문자열의 일부만 일치
                pattern_index += 1
                continue

            # 부분 문자열 발견
            start_indexes.append(text_index - len(pattern) + 2)
            pattern_index = KMP_table[pattern_index]

    return start_indexes

def printAnswer(start_indexes):
    print(len(start_indexes))

    for index in start_indexes:
        print(index, end=' ')

# get input
text = input_().replace('\n', '')
pattern = input_().replace('\n', '')

# KMP algorithm
start_indexes = getStartIndexes(text, pattern)
printAnswer(start_indexes)



# 세 번째 Rabin Karp
# 오답. 시간 초과
## sub_text 선언 부분에서 비효율성 발생
## MAX와 base = 7은 해시 충돌이 일어나지 않게 하기 위한 설정
## 실무에서는 일어날 수 있으므로 해당 문제에서만 

import sys

input_ = sys.stdin.readline
MAX = 10 ** 10 + 7

def mod(number):
    global MAX
    
    return number % MAX

def getPowers(length, base = 7):
    powers = [1]

    for index in range(1 ,length):
        powers.append(mod(powers[index - 1] * base))

    return powers

def calculateHash(string, powers):
    hash_value = 0
    
    for index, char in enumerate(string[::-1]):
        hash_value += mod(ord(char) * powers[index])

    return mod(hash_value)

def isSame(value1, value2):
    return value1 == value2

def getStartIndexes(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)

    start_indexes = []
    powers = getPowers(pattern_length)
    text_hash = calculateHash(text[:pattern_length], powers)
    pattern_hash = calculateHash(pattern, powers)
    
    for start_index in range(text_length - pattern_length + 1):
        sub_text = text[start_index:start_index + pattern_length] # 
        """
        sub_text를 해시값이 동일할 때만 구하도록
        if isSame(text_hash, pattern_hash):
            sub_text = ...
            
            if isSame(sub_text, pattern):
                ...
        으로 해도 시간 초과 발생
        """
        
        if isSame(text_hash, pattern_hash) and isSame(sub_text, pattern):
            start_indexes.append(start_index + 1) # 문제는 index를 1부터 세기 때문에 +1 필요

        if start_index != text_length - pattern_length: # index range 에러가 나므로 조건 필요
            prev_value = ord(text[start_index]) * powers[-1]
            next_value = ord(text[start_index + pattern_length])
            text_hash = mod(7 * (text_hash - prev_value) + next_value)

    return start_indexes

def printAnswer(start_indexes):
    print(len(start_indexes))

    for index in start_indexes:
        print(index, end=' ')

# get input
text = input_().rstrip('\n')
pattern = input_().rstrip('\n')



# 네 번째 Rabin Karp
# 정답

import sys

input_ = sys.stdin.readline
MAX = 10 ** 10 + 7

def mod(number):
    global MAX
    
    return number % MAX

def getPowers(length, base = 7):
    powers = [1]

    for index in range(1 ,length):
        powers.append(mod(powers[index - 1] * base))

    return powers

def calculateHash(string, powers):
    hash_value = 0
    
    for index, char in enumerate(string[::-1]):
        hash_value += mod(ord(char) * powers[index])

    return mod(hash_value)

def isSame(value1, value2):
    return value1 == value2

def getStartIndexes(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)

    start_indexes = []
    powers = getPowers(pattern_length)
    text_hash = calculateHash(text[:pattern_length], powers)
    pattern_hash = calculateHash(pattern, powers)
    
    for start_index in range(text_length - pattern_length + 1):
        if isSame(text_hash, pattern_hash): # 충돌 무시
            start_indexes.append(start_index + 1) # 문제는 index를 1부터 세기 때문에 +1 필요

        if start_index != text_length - pattern_length: # index range 에러가 나므로 조건 필요
            prev_value = ord(text[start_index]) * powers[-1]
            next_value = ord(text[start_index + pattern_length])
            text_hash = mod(7 * (text_hash - prev_value) + next_value)

    return start_indexes

def printAnswer(start_indexes):
    print(len(start_indexes))

    for index in start_indexes:
        print(index, end=' ')

# get input
text = input_().rstrip('\n')
pattern = input_().rstrip('\n')

# Rabin Karp 알고리즘
start_indexes = getStartIndexes(text, pattern)
printAnswer(start_indexes)

