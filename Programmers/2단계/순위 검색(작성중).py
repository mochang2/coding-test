"""
20221130
url: https://school.programmers.co.kr/learn/courses/30/lessons/72412
후기: 

첫 번째 시도는 문제를 풀다가 포기했다.
개발언어, 직군, 경력, 소울푸드를 각 set으로 나누고 & 연산으로 구하고 - a,
점수는 세그먼트 트리로 특정 점수 이상의 사람 수를 구하려고 했다 - b.
하지만 간과한 것이 a랑 b의 교집합을 구하는 방법을 찾으려하다가 포기했다.
"""

# 첫 번째 시도
# 실패(포기)

language_list = ['cpp', 'java', 'python']
job_group_list = ['frontend', 'backend']
career_list = ['junior', 'senior']
soul_food_list = ['chicken', 'pizza']
ANY = '-'
MAX_SCORE = 100000

def solution(informations, queries):
    counts = []
    
    languages, job_groups, careers, soul_foods, score_segment_tree = parseInformations(informations)
    
    
    for query in queries:
        condition = parseQuery(query)
        queried_count = calculateIncludedCount(
            languages,
            job_groups,
            careers,
            soul_foods,
            condition
        )
        counts.append(queried_count)
    
    return counts

def parseInformations(informations):
    global MAX_SCORE
    
    languages, job_groups, careers, soul_foods = initializeInformationSets()
    score_range = initializeSegmentTree(MAX_SCORE) # 각 점수 개수 저장
    
    for id_, information in enumerate(informations):
        language, job_group, career, soul_food, score = information.split(' ')
        
        languages[language].add(id_)
        job_groups[job_group].add(id_)
        careers[career].add(id_)
        soul_foods[soul_food].add(id_)
        updateSegmentTree(score_range, int(score), 1, 1, MAX_SCORE)
        
    return languages, job_groups, careers, soul_foods, score_segment_tree

def initializeInformationSets():
    global language_list, job_group_list, career_list, soul_food_list
    
    languages = { language: set() for language in language_list }
    job_groups = { job_group: set() for job_group in job_group_list }
    careers = { career: set() for career in career_list }
    soul_foods = { soul_food: set() for soul_food in soul_food_list }
    
    return languages, job_groups, careers, soul_foods

def initializeSegmentTree(length, default_value = 0):
    return [default_value for _ in range(length * 4 + 1)]

def mergeSegmentTree(left_value, right_value):
    return left_value + right_value

def updateSegmentTree(segment_tree, score, node, left_range, right_range):
    isIrrelevant = score < left_range or score > right_range
    if isIrrelevant:
        return segment_tree[node]
    
    arrivedLeaf = left_range == right_range
    if arrivedLeaf:
        segment_tree[node] += 1
        return segment_tree[node]
    
    mid_range = left_range + (right_range - left_range) // 2
    left_sum = updateSegmentTree(segment_tree, score, node * 2, left_range, mid_range)
    right_sum = updateSegmentTree(segment_tree, score, node * 2 + 1, mid_range + 1, right_range)
    
    segment_tree[node] = mergeSegmentTree(left_sum, right_sum)
    return segment_tree[node]

def parseQuery(query):
    global ANY
    
    language, job_group, career, rest = query.split(' and ')
    soul_food, score = rest.split(' ')
    
    return {
        'language': None if language == ANY else language,
        'job_group': None if job_group == ANY else job_group,
        'career': None if career == ANY else career,
        'soul_food': None if soul_food == ANY else soul_food,
        'score': int(score)
    }

def calculateIncludedCount(languages, job_groups, careers, soul_foods, condition):
    pass


 
