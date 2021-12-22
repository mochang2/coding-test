"""
211110
월간 코드 챌린지 시즌2
url: https://programmers.co.kr/learn/courses/30/lessons/77884
후기: 약수의 개수가 홀수인 수는 제곱수였음을 간과
"""

def solution(left, right):
    answer = 0
    for i in range(left, right + 1) :
        count = 1 # 본인
        for j in range(1, (i // 2) + 1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer
