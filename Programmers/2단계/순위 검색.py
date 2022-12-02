"""
221202
url: https://school.programmers.co.kr/learn/courses/30/lessons/72412
후기: 역시 카카오 난이도는 믿을 게 못 된다. 효율성 따지면 최소 3단계 문제이다.

정확성만 따지면 너무 간단히 완탐으로 풀린다.
raw_query를 매번 parsing한 다음 각 information이 포함되는지 파악하면 된다.
하지만 이런 방식은 O(len(raw_queries) * len(informations))이기 때문에 효율성은 전혀 통과되지 않는다.

답을 봤고 정말 신박한 방법이라 놀랐다.

1. 모든 information을 parsing하여 score을 dictionary에 2 ** 4번 저장한다.
   여기서 4는 condition의 개수(언어, 직군, 경력, 소울푸드)를 의미한다.
   이때 dictionary의 key값은 언어 + 직군 + 경력 + 소울푸드의 string을 연결한 형태이다.
   조건이 '상관없음'을 의미하고 싶다면 문제대로 '-'로 표시한다.
   즉, ---pizza면 언어, 직군, 경력과 상관없이 소울푸드가 pizza인 점수들로 한정하여 계산한다.
2. 각 key별로 score들을 오름차순 정렬한다.
3. raw_query를 파싱하여 알고자 하는 query(dictionary의 키값)와 score을 구한다.
4. lower bound binary search를 이용해 query에 해당하는 score의 개수를 구한다.
5. 답에 추가한다.
"""

ANY = '-'
CONNECTIVE = ' and '
SPACE = ' '

class DictHavingList(dict):
    def add(self, key, value):
        has_key = key in self.keys()

        if has_key:
            self[key].append(value)
        else:
            self[key] = [value]

def solution(informations, raw_queries):
    counts = []

    scores_by_query = getScoresByQuery(informations)
    sortScores(scores_by_query)

    for raw_query in raw_queries:
        count = countCorrespondingScores(scores_by_query, raw_query)
        counts.append(count)

    return counts

def getScoresByQuery(informations):
    scores_by_query = DictHavingList()
    CONDITION_LENGTH = 4

    for information in informations:
        conditions, score = parseInformation(information, CONDITION_LENGTH)

        for binary in range(2 ** CONDITION_LENGTH): # bit 연산으로 모든 경우의 수 계산
            query = filterConditions(bin(binary)[2:].zfill(CONDITION_LENGTH), conditions)
            scores_by_query.add(query, score)

    return scores_by_query

def parseInformation(information, condition_length):
    global SPACE
    
    conditions = information.split(SPACE)[:condition_length]
    score = information.split(SPACE)[-1]

    return conditions, int(score)

def filterConditions(binary, conditions):
    global ANY

    query = ''

    for index, bit in enumerate(binary):
        if isBitSet(bit):
            query += conditions[index]
            continue

        query += ANY

    return query

def isBitSet(bit):
    return bit == '1'

def sortScores(scores_by_query):
    for key, value in scores_by_query.items():
        scores_by_query[key] = sorted(value)

def countCorrespondingScores(scores_by_query, raw_query):
    query, score = parseRawQuery(raw_query)
    scores = scores_by_query.get(query, []) # 존재하지 않는 키일 수 있으므로
    index = getLowerBound(scores, score)

    return len(scores) - index

def parseRawQuery(raw_query):
    global CONNECTIVE, SPACE

    language, job_group, career, rest = raw_query.split(CONNECTIVE)
    soul_food, score = rest.split(SPACE)

    return language + job_group + career + soul_food, int(score)
    
def getLowerBound(numbers, target):
    left = 0
    right = len(numbers)

    while left < right:
        mid = left + (right - left) // 2

        if target <= numbers[mid]:
            right = mid
        else:
            left = mid + 1

    return left
  
# 참고
# getLowerBound 함수 대신 side effect를 없애고자

def getBiggerNumbers(numbers, target):
  // 같은 로직
  return numbers[left:]

# 로 선언해서 사용하니 시간 초과가 났다.
# 인자의 개수가 너무 많아서 list를 메모리에 새로 할당하기만 해도 시간이 오래 걸린 것 같다.

