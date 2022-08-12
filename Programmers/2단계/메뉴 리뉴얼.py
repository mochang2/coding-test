"""
220504
2022 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/92335
후기: 92334번 1단계보다는 오히려 쉬웠다.
1. 문제의 요점은 주어진 수를 k진수의 문자열로 변환한 뒤
2. 0을 기준으로 문자열을 나누고
3. 해당 숫자들이 소수인지 판별한다.

isPrime 함수에서 16, 17번째 줄 범위를 잘 설정하는 것이 중요했다.
그냥 넉넉히 하기 위해 16번째 줄을 max_range = num // 2로 했다면 시간초과가 나며
17번째 줄을 max_range + 2까지로 잡으면 num = 2일 때 범위 계산을 잘못해서 틀리게 된다.
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
        temp.extend([0])
        max_string_count = max(temp)
        if max_string_count < 2:
            continue
            
        for key, value in dic.items():
            #print(key, value, max_string_count)
            if value == max_string_count:
                answer.append(key)

    return sorted(answer)

  
