"""
211130
골드4 중량제한
url: https://www.acmicpc.net/problem/1939
후기: parametric search인 것을 알고 풀지 않았다면 못 풀었을 것 같다. 알고 풀었는데도 시간이 오래 걸렸다. 그리고 dfs로 하니까 recursion error가 떴다.
너무 stack 깊이가 깊어져서 그런 것 같다. bfs도 익힐 필요를 느꼈다.
"""

import sys
from collections import deque

def minus_one(num):
    return int(num) - 1

def bfs(vertex):
    global temp_adj_li, visited, To, queue
    flag = False
    
    while len(queue) != 0:
        first_vertex = queue.popleft()
        for adj_vertex in temp_adj_li[first_vertex]:
            if adj_vertex == To:
                flag = True
                break
            
            if not visited[adj_vertex]:
                visited[adj_vertex] = True
                queue.append(adj_vertex)
        if flag:
            break

    return flag
    

N, M = map(int, sys.stdin.readline().strip().split())
adj_li = []
for i in range(M):
    adj_li.append(list(map(int, sys.stdin.readline().strip().split())))
adj_li.sort(key=lambda x: (-x[2]))  # 2번째 index(중량제한)에 대해서 내림차순
From, To = map(minus_one, sys.stdin.readline().strip().split())

# parametric search pointer
start = 0
end = adj_li[0][2]
answer = 0

while start <= end:
    mid = (start + end) // 2
    temp_adj_li = [[] for _ in range(N)]
    visited = [False for _ in range(N)]

    # mid 값을 버틸 수 있는 다리만 연결
    for adj_info in adj_li:
        if adj_info[2] < mid:
            break
        temp_adj_li[adj_info[0] - 1].append(adj_info[1] - 1)
        temp_adj_li[adj_info[1] - 1].append(adj_info[0] - 1)

    # bfs로 From과 To가 연결되어 있는지 확인
    visited[From] = True
    queue = deque([From])
    if bfs(From):  # From과 To가 연결되어 있음.
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(end)
    
    
