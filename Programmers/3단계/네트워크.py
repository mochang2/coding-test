"""
211129
깊이/너비 우선 탐색(DFS/BFS)
url: https://programmers.co.kr/learn/courses/30/lessons/43162
후기: BFS, DFS를 되짚어보는 시간이었다. DFS가 조금 더 구현이 쉬운 것 같다.
"""

# DFS 버전
def dfs(index, visited, adj_li):
    for adj_node in adj_li[index]:
        if not visited[adj_node]:
            visited[adj_node] = True
            dfs(adj_node, visited, adj_li)
        
def solution(n, computers):
    adj_li = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    # 모든 edge 연결
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                adj_li[i].append(j)
    
    # dfs
    answer = 0
    for index in range(n):
        if not visited[index]:
            dfs(index, visited, adj_li)
            answer += 1
    return answer


# BFS 버전
from collections import deque

def solution(n, computers):
    adj_li = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                adj_li[i].append(j)
                
    # bfs
    answer = 0
    queue = deque()
    for i in range(n):
        if visited[i]:
            continue
        
        queue.append(i)
        while len(queue) != 0:
            queue_first = queue.popleft()
            for adj_node in adj_li[queue_first]:
                if not visited[adj_node]:
                    queue.append(adj_node)
                    visited[adj_node] = True
        answer += 1

    return answer
