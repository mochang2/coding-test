"""
211030
Summer / Winter Coding(2019)
url: https://programmers.co.kr/learn/courses/30/lessons/62048
후기: 수학 문제. 코딩 실력은 그닥 필요가 없었던 문제.
"""

import math


def solution(w,h): # 실패
    M = max(w,h)
    m = min(w,h)
    portion = M / m
    
    tmp = 0
    for i in range(2, m + 1):
        if ((i - 1) * portion) % 1 != 0 and (i * portion) % 1 != 0 and math.floor(i * portion) - math.floor((i - 1) * portion) != math.floor(portion):
            tmp += 1
    
    return (M - math.ceil(portion)) * m - tmp

def solution(w,h): # 답 참고
    return w * h - (w + h - math.gcd(w,h))
