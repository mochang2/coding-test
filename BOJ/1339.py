"""
211228
골드4 단어 수학
url: https://www.acmicpc.net/problem/1339
후기: 그리디 문제라서 당연히 가장 앞 자리 수부터 9876.. 이렇게 부여해서 더해주면 될 줄 알았으나, 반례가 존재했다.
결국 세 번째 시도는 답을 보고 알았다. 수학문제 같았다.
"""
# 첫 번째 시도
# 반례 : ABB, BB, BB... BB(9개)  A:9, B:8 vs A:8, B:9
N = int(input())
answer = 0
alphabet_map = dict()
words = [[" " for _ in range(8)] for __ in range(10)]

for i in range(N):
    word = input()
    n = len(word)
    for index, char in enumerate(word):
        words[i][8 - n + index] = char
        if char not in alphabet_map.keys():
            alphabet_map[char] = -1

next_digit = 9
for j in range(8):
    for i in range(10):
        char = words[i][j]
        if char == " ":
            continue
        if alphabet_map[char] == -1:
            alphabet_map[char] = next_digit
            next_digit -= 1
print(words)
print(alphabet_map)
            
for word in words:
    temp = ""
    for char in word:
        if char == " ":
            continue
        temp += str(alphabet_map[char])
    if temp != "":
        answer += int(temp)
print(answer)


# 두 번째 시도
# 브루트 포스 10!은 대략 300만이니까 가능할 거라 생각
# 하지만 시간 초과
from itertools import permutations
N = int(input())
answer = 0
alphabet_set = set()
alphabet_dic = dict()
words = []

for i in range(N):
    word = input()
    words.append(word)
    for char in word:
        alphabet_set.add(char)
        if char not in alphabet_dic.keys():
            alphabet_dic[char] = -1

alphabet_li = list(alphabet_set)
n = len(alphabet_li)
for permutation in permutations(alphabet_li, n):
    digit = 9
    for i in range(n - 1, -1, -1):
        alphabet_dic[permutation[i]] = digit
        digit -= 1

    temp = 0
    for word in words:
        for i in range(len(word)):
            temp += 10 ** (len(word) - i - 1) * alphabet_dic[word[i]]
    answer = max(temp, answer)
print(answer)


# 세 번째 시도
# 첫 번째 시도 수정
N = int(input())
answer = 0

# 각각의 알파벳을 위치와 개수에 따라 높은 숫자를 부여받을지를 결정하는, 가중치 계산.
alphabet_map = dict() 
for alph in list("QWERTYUIOPASDFGHJKLZXCVBNM"):
    alphabet_map[alph] = 0
words = [[" " for _ in range(8)] for __ in range(10)]

for i in range(N):
    word = input()
    n = len(word)
    for index, char in enumerate(word):
        words[i][8 - n + index] = char
        alphabet_map[char] += 10 ** (n - index - 1)

alphabet_map_items = []
for items in list(alphabet_map.items()):
    if items[1] != 0:
        alphabet_map_items.append(items)
alphabet_map_items.sort(key=lambda x: -x[1])

next_digit = 9
for item in alphabet_map_items:
    alphabet_map[item[0]] = next_digit
    next_digit -=1

for word in words:
    temp = ""
    for char in word:
        if char == " ":
            continue
        temp += str(alphabet_map[char])
    if temp != "":
        answer += int(temp)
print(answer)

