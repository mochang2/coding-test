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

def isPrime(num):
    max_range = int(num ** 0.5)
    for i in range(2, max_range + 1):
        # max_range + 2로 범위를 설정하면 num = 2일 때 틀림
        if num % i == 0:
            print(num, i)
            return False
    return True

def solution(n, k):
    answer = 0
    li = [] # 몫 저장할 변수
    k_driven = k
    count = 1 # 곱셈한 횟수 계산
    while k_driven <= n:
        k_driven *= k
        count += 1
    k_driven = k_driven // k
    count -= 1
    
    while count >= 0:
        if n >= k_driven:
            quota = n // k_driven
            n = n - quota * k_driven
        else:
            quota = 0
        k_driven = k_driven // k
        count -= 1
        li.append(str(quota))
        
    number = ''.join(li) # k진수의 string 형태
    print(number)
    
    for digits in number.split('0'):
        if digits == '' or digits == '1':
            continue
        if isPrime(int(digits)):
            answer += 1
        
    return answer
  
