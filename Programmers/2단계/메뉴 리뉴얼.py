"""
220812
2021 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/72411
후기: 문제가 이해가 안 됐다... 진짜 이건 내 국어 이슈가 아니라 문제 해석의 여지가 너무 다양하게 나온 거 같다.

문제가 요구하는 바는 course에 입력된 숫자로 부분집합을 만들었을 때, 해당 부분집합이 총 몇 번 포함되었는지 계산하고
그 포함된 횟수가 가장 많은 애를 return해라. 라는 의미였다.

3중 for 문을 통해서 완탐했다.
len(orders) = O(20)
len(orders[0]) = O(10)
len(course) = O(10)
이므로 조합로 충분히 완탐이 가능하다고 생각했다.
1차 for문은 course를 순회,
2차 for문은 orders를 순회,
3차 for문은 orders를 이용한 조합으로 순회했다.
"""

from itertools import combinations

def solution(orders, course):
    answer = []

    for count in course:
        dic = dict()
        
        for order in orders:
            for combination in combinations(order, count):
                string = ''.join(sorted(list(combination))) # list는 unshable type이므로 str로 변환, sorted 필요
                string_count = dic.get(string, None)
                
                if string_count:
                    dic[string] += 1
                else:
                    dic[string] = 1
                    
        temp = [value for _, value in dic.items()] # max count를 세기 위함
        temp.extend([0]) # temp가 빈 list일 수도 있으므로 예외 처리
        max_string_count = max(temp)
        
        if max_string_count < 2:
            continue
            
        for key, value in dic.items():
            if value == max_string_count: # 개수가 같은 애들은 전부 return하라고 했으므로
                answer.append(key)

    return sorted(answer)

  
