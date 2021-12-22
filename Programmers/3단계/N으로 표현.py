"""
211221
동적 계획법
url: https://programmers.co.kr/learn/courses/30/lessons/42895
후기: DP 진짜.. 너무 어렵다 많이많이 연습이 필요하고 48~52번째 줄 4중 for문도 정말 신박한 방법이다.
연속된 N으로 표현된 수끼리 산술연산하는 것까지 포함시키는 for문이다.
"""

# 첫 번재 시도
# 예전에 산술 연산을 dfs로 푼 문제가 있어서 비슷한 문제인 것 같아서 이렇게 접근했다.
# 하지만 dfs(index + 1, current_num * 10 + N, N, target_num)를 잘못 생각해서 틀렸다.

answer = 9

def dfs(index, current_num, N, target_num):
    global answer
    if index == 9:
        return
    if current_num == target_num:
        answer = min(answer, index)
        return
    
    dfs(index + 1, current_num * 10 + N, N, target_num)
    dfs(index + 1, current_num + N, N, target_num)
    dfs(index + 1, current_num - N, N, target_num)
    dfs(index + 1, current_num * N, N, target_num)
    dfs(index + 1, current_num // N, N, target_num)
    

def solution(N, target_num):
    global answer
    current_num = N
    dfs(1, current_num, N, target_num)
    return answer if answer != 9 else -1



# 두 번째 시도
def solution(N, target_num):    
    dp = [set() for _ in range(9)]
    temp = 0
    for i in range(1, 9): # N을 1개부터 8개까지 이어붙일 때 나올 수 있는 모든 수
        temp = 10 * temp + N
        if temp == target_num:
            return i
        dp[i].add(temp)
            
    for i in range(2, 9): # N을 몇 개 썼는지 나타내는 수
        # 이전에 계산된 것을 이용하는 메모이제이션, x + y == i인 것에 대해서 계산
        for j in range(1, i + 1):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
                    
        for result in dp[i]:
            if result == target_num:
                return i
    return -1
