"""
20220730
골드3 소수의 연속합
url: https://www.acmicpc.net/problem/1644
후기: 모든 소수를 구해야 하므로 에라토스테네스의 체가 반드시 필요하다.
다만 잊고 있던 것은 에라토스테네스가 N ** 0.5의 수까지만 판별해도 된다는 것이고, 이로 인해 O(N) = 4,000,000이면 소수들이 판별된다.
이때, primes를 list가 아닌 set으로 하면 속도가 느리므로 주의해야 한다(생각보다 python set이 해시 충돌이 자주나나...? 느릴 때가 많다).
이후 부분합과 투포인터 알고리즘을 사용하면 해결된다.
"""

import sys
from math import sqrt, ceil

input_ = sys.stdin.readline

def eratostenes(N):
    primes = [True for i in range(N + 1)]
    N_root = ceil(sqrt(N))

    for prime in range(2, N_root + 1):
        if not primes[prime]:
            continue
        
        for not_prime in range(prime * 2, N + 1, prime):
            primes[not_prime] = False

    return [index for index, is_prime in enumerate(primes) if is_prime][2:]  # primes (0, 1은 제외)

def calcSubTotal(li):
    N = len(li)
    if not N: # N == 1일 때의 예외처리
        return []
    
    subtotal = [0]
    for i in range(N):
        subtotal.append(subtotal[-1] + li[i])

    return subtotal

def twoPointer(li, target):
    answer = 0
    left = 0
    right = 1

    while left < len(li):
        sum_ = li[right] - li[left]
        if sum_ == target:
            answer += 1
            
        if right < len(li) - 1 and sum_ < target:
            right += 1
        else:
            left += 1

    return answer

# initialization
N = int(input_().strip())
primes = eratostenes(N)
subtotal = calcSubTotal(primes)

# print
print(twoPointer(subtotal, N))

