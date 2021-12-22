"""
211027
월간 코드 챌린지 시즌3
url: https://programmers.co.kr/learn/courses/30/lessons/86051
후기: 코테 처음 시작으로 간단히 푼 문제. 엄청 쉬움.
"""

def solution(numbers):
    """
    comparison_li = [i for i in range(10)]

    answer = 0
    for i in numbers:
        if i in comparison_li:
            comparison_li.remove(i)
            
    for i in comparison_li:
        answer += i
    """
    
    answer = 0
    for i in range(10):
        answer += i
    
    for i in numbers:
        answer -= i
    
    
    return answer
