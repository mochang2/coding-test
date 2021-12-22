"""
211028
위클리 챌린지
url: https://programmers.co.kr/learn/courses/30/lessons/87946
"""

from itertools import permutations

# tip: 전수조사
def solution(k, dungeons):
    dungeons = permutations(dungeons, len(dungeons))
    
    answer = 0
    for dungeon_list in list(dungeons): # 던전에 대한 모든 경우의 수가 리스트 형식으로 표현됨
        temp_answer = 0
        temp_k = k
        
        for dungeon in dungeon_list:
            if temp_k >= dungeon[0]:
                temp_k -= dungeon[1]
                temp_answer += 1
            
            answer = max(answer, temp_answer)
    
    return answer


""" 다른 사람의 풀이: dfs 이용 """
answer = 0
N = 0
visited = []


def dfs(k, temp_answer, dungeons):
    global answer
    if cnt > answer:
        answer = temp_answer

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], temp_answer + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
