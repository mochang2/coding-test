"""
230325
url: https://school.programmers.co.kr/learn/courses/30/lessons/42893
후기: 단순 문자열 파싱, 정규 표현식 문제이다.
이 문제는 풀기 전에 그냥 답에서 정규 표현식만 가져왔다.
알고리즘 문제인 것 같지는 않았기 때문이다.
그리고 HTML은 property를 single quote로도, double quote로도 감쌀 수 있기 때문에 문제가 더러우면 이런 것까지 고려해야 될 것 같았기 때문이다.
(그런데 다행히 이 문제는 그러지 않음. 그리고 점수가 소수점 단위 때문에 비교 연산에서 문제가 생기는 테스트 케이스도 존재하지 않음)
"""

import re

def solution(word, pages):
    answer = [0, 0] # index, score
    page_information = dict()
    
    for index, page in enumerate(pages):
        page_url = parsePageUrl(page)
        hrefs = parseHref(page)
        base_score = calculateBaseScore(word, page)
        
        page_information[page_url] = dict()
        page_information[page_url]['index'] = index
        page_information[page_url]['hrefs'] = hrefs
        page_information[page_url]['base_score'] = base_score
        page_information[page_url]['score'] = base_score
        
    for value in page_information.values(): # 링크 점수기더하기
        if len(value['hrefs']) == 0: # 0이면 run time error 발생
            continue
            
        link_score = value['base_score'] / len(value['hrefs'])
        
        for href in value['hrefs']:
            if href in page_information.keys():
                page_information[href]['score'] += link_score
                
    for value in page_information.values():
        index, score = value['index'], value['score']
        
        if score > answer[1] or score == answer[1] and index < answer[0]:
            answer = [index, score]
    
    return answer[0]
    
def parsePageUrl(page):
    searched_object = re.search('<meta\sproperty=.+content="(https:\/\/\S*)"\/>', page)
    
    return searched_object.group(1)

def parseHref(page):
    return re.findall('<a\shref="(https://\S*)"', page)

def calculateBaseScore(word, page):
    base_score = 0
    
    for searched_word in re.findall('[a-zA-Z]+', page, re.IGNORECASE):
        if searched_word.casefold() == word.casefold():
            base_score += 1
            
    return base_score
