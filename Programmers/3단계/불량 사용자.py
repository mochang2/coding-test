"""
230319
url: https://school.programmers.co.kr/learn/courses/30/lessons/64064
후기: 순열, 완전 탐색을 이용한 문제이다.
의외로 간단한 풀이인데 3단계여서 너무 어렵게 고민한 것도 있었나보다.

첫 번째로 시도한 풀이는 다음과 같다.
1. banned_id를 key를 가지는 mapper를 만든다.
2. banned_id에 매핑되는 user_id를 mapper에 각각 따로 저장한다.
3. 매핑해야할 banned_id의 개수와 매핑된 user_id의 개수는 경우의 수에 영향을 주지 않으므로 고려해야 할 선택지에서 지운다.
4. 재귀를 돌며 중복되지 않은 개수를 구한다.

하지만 이 풀이법에는 문제가 있었다.
3번째 단계에서 ["a123","b123","c123"], ["*123", "a***"] 와 같은 input이 들어온다면,
mapper에서 "a***"를 가지는 key를 지워버리므로 정답인 2와 다르게 3이 출력된다.
+) 추가적으로 잘못된 게 있었는데, combination을 돌렸을 때 이중 for문일 필요가 없다.
결국 답을 봤다.


문제 해설은 여기를 봤다: https://school.programmers.co.kr/questions/23330

문제 해설을 본 뒤 풀이는 다음과 같다.
1. user_ids를 banned_ids의 길이만큼 순열을 돌린다. 조합이 아니어야 하는 이유는 위 링크에서 확인 가능하다.
2. 돌려서 나온 순열이 각각 banned_ids에 매칭되는지 확인한다.
3. 매칭되면 중복되지 않은 방식으로 set에 추가한다.
4. set의 길이를 return한다.
"""

"""
시도한 테스트 케이스

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]), 'to be 2\n')
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]), 'to be 2\n')
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]), 'to be 3\n')
print(solution(["fradi"], ["frady"]), 'to be 0\n')
print(solution(["frido", "frodo"], ["fr*do", "fr**o"]), 'to be 1\n')
print(solution(["prodo", "piodi", "proda", "pradak"], ["p*od*", "prod*", "pr*da*"]), 'to be 3\n')
print(solution(["aa","ab","cc"], ["a*", "a*", "c*"]), 'to be 1\n')
print(solution(["a123","b123","c123"], ["*123", "a***"]), 'to be 2\n')
"""

## 첫 번재 시도
## 실패

from re import compile, match
from itertools import combinations

def solution(user_ids, banned_ids):
    mapper = initializeMapper(banned_ids)
    matchId(mapper, user_ids)
    deleted_count = deleteUnnecessaryKeys(mapper) # 매칭되는 user_id와 banned_id의 개수가 같아 계산할 필요가 없는 key 삭제
    
    cases = set()
    calculateValidCases(
        list(map(convertToSequentialType, mapper.values())),
        len(banned_ids) - deleted_count,
        0,
        cases
    )
    
    return len(cases)

def initializeMapper(banned_ids):
    mapper = dict()
    
    for banned_id in banned_ids:
        if banned_id in mapper.keys():
            mapper[banned_id]['count'] += 1
        else:
            mapper[banned_id] = dict()
            mapper[banned_id]['count'] = 1
            mapper[banned_id]['user_ids'] = []
    
    return mapper

def matchId(mapper, user_ids):
    for banned_id in mapper.keys():
        regexp = str(banned_id.replace('*', '.{1}'))
        regexp = compile('^' + regexp + '$')
        
        for user_id in user_ids:
            if regexp.match(user_id):
                mapper[banned_id]['user_ids'].append(user_id)
                
def deleteUnnecessaryKeys(mapper):
    count = 0
    keys = []
    
    for banned_id in mapper.keys():
        if mapper[banned_id]['count'] == len(mapper[banned_id]['user_ids']):
            keys.append(banned_id)
            
    for key in keys:
        count += mapper[key]['count']
        del mapper[key]
        
    return count

def convertToSequentialType(mapper_value):
    return [mapper_value['count'], mapper_value['user_ids']]
        
def calculateValidCases(mapper_values, counts_to_be_selected, index, cases, selected_user_ids = []):
    if len(selected_user_ids) == counts_to_be_selected: # index == len(mapper_values)
        isNotDuplicatedIds = len(selected_user_ids) == len(set(selected_user_ids))
        if isNotDuplicatedIds:
            cases.add(str(sorted(selected_user_ids)))
            
        return
    
    for count, user_ids in mapper_values[index:]:
        for combination in combinations(user_ids, count):
            calculateValidCases(
                mapper_values,
                counts_to_be_selected,
                index + 1,
                cases,
                [*selected_user_ids, *combination] # JS의 spread 연산
            )


            
# 두 번재 시도
## deleteUnnecessaryKeys를 지우고, 첫 번째 풀이 calculateValidCases의 이중 for문을 지움
## 성공

from re import compile, match
from itertools import combinations

def solution(user_ids, banned_ids):
    mapper = initializeMapper(banned_ids)
    matchId(mapper, user_ids)
    
    cases = set()
    calculateValidCases(
        list(map(convertToSequentialType, mapper.values())),
        len(banned_ids),
        0,
        cases
    )
    
    return len(cases)

def initializeMapper(banned_ids):
    mapper = dict()
    
    for banned_id in banned_ids:
        if banned_id in mapper.keys():
            mapper[banned_id]['count'] += 1
        else:
            mapper[banned_id] = dict()
            mapper[banned_id]['count'] = 1
            mapper[banned_id]['user_ids'] = []
    
    return mapper

def matchId(mapper, user_ids):
    for banned_id in mapper.keys():
        regexp = str(banned_id.replace('*', '.{1}'))
        regexp = compile('^' + regexp + '$')
        
        for user_id in user_ids:
            if regexp.match(user_id):
                mapper[banned_id]['user_ids'].append(user_id)

def convertToSequentialType(mapper_value):
    return [mapper_value['count'], mapper_value['user_ids']]
        
def calculateValidCases(mapper_values, counts_to_be_selected, index, cases, selected_user_ids = []):
    if len(selected_user_ids) == counts_to_be_selected:
        isNotDuplicatedIds = len(selected_user_ids) == len(set(selected_user_ids))
        if isNotDuplicatedIds:
            cases.add(str(sorted(selected_user_ids)))
            
        return
    
    [count, user_ids] = mapper_values[index]
    for combination in combinations(user_ids, count):
        calculateValidCases(
            mapper_values,
            counts_to_be_selected,
            index + 1,
            cases,
            [*selected_user_ids, *combination]
        )


        
## 세 번재 시도
## 성공(두 번째 시도보다는 느림)

from re import compile, match
from itertools import permutations

def solution(user_ids, banned_ids):
    cases = set()
    banned_ids = [banned_id.replace('*', '.{1}') for banned_id in banned_ids]

    for permutation in permutations(user_ids, len(banned_ids)): # banned_ids의 길이만큼 순열
        matched = True

        for index in range(len(permutation)):
            user_id = permutation[index]
            banned_id = banned_ids[index]
            
            if not isMatched(user_id, '^' + banned_id + '$'):
                matched = False
                break

        if matched:
            cases.add(str(sorted(permutation)))
    
    return len(cases)

def isMatched(word, regexp):
    regexp = compile(regexp)
    return regexp.match(word)
  
