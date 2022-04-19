"""
211102
실버1 A->B
url: https://www.acmicpc.net/problem/16953
후기: B->A로의 경우를 생각하니까 훨씬 쉬웠다.
"""

import sys

def divide_by_two(num):
    return int(num / 2)

def sub_one_at_last(num):
    return int((num - 1) / 10)

def exit_with_minus_one():
    print(-1)
    sys.exit(0)

if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().strip().split())
    count = 0
    m = min(a,b)  # a < b 라는 조건이 없으니 추가
    M = max(a,b)

    if M % 10 in (3, 5, 7, 9) and m != M:  # m == M일 수도 있으니 조건 추가
        exit_with_minus_one()

    while m < M:
        if M % 2 == 0:  # M이 짝수인 경우(M의 일의 자리 숫자가 2,4,6,8,0인 경우
            M = divide_by_two(M)
            count += 1
        elif M % 10 == 1: # M의 일의 자리 숫자가 1일 경우
            M = sub_one_at_last(M)
            count += 1
        else: #M의 일의 자리 숫자가 3,5,7,9인 경우
            break
        
    if m == M:
        print(count + 1)
    else:
        #print(m)
        #print(M)
        exit_with_minus_one()
