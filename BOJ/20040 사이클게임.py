"""
골드4 사이클 게임
url: https://www.acmicpc.net/problem/20040
후기: 처음에는 한 줄 입력받을 때마다 dfs를 돌아서 찾으려고 했다. 입력받을 때 하나를 시작점, 하나를 끝점으로 둬서 dfs를 돌면, 끝점을 만나면 True를 반환하게 하려고 했다.
하지만 입력값이 너무 커서 시간 초과가 났다.
방법을 모르겠어서 검색을 해보니 union-find 문제랬다. 입력받은 정점 a,b가 같은 그룹에 포함되어 있으면, 해당 점을 잇는 간선만 그으면
cycle이 완성되는 것이니 맞는 말이었다. 탐색만 풀다보니, 생각의 전환이 힘든 문제였다.
"""

# 첫 번째 시도
"""
import sys

def dfs(end_v, vertex, i):
    global found, edges, answer
    if end_v == vertex:
        found = True
        answer = i + 1
        return

    for adj in adjs[vertex]:
        if not visited[adj]:
            visited[adj] = True
            dfs(end_v, adj, i)

n, m = map(int, sys.stdin.readline().strip().split())
adjs = [[] for _ in range(n)]
answer = 0
visited = [False for _ in range(n)]
found = False

for i in range(m):
    end_v, start_v = list(map(int, sys.stdin.readline().strip().split()))
    if found:
        continue
    dfs(end_v, start_v, i)
    adjs[start_v].append(end_v)
    adjs[end_v].append(start_v)
    visited = [False for _ in range(n)]

print(answer)
"""

# 두 번째 시도. union-find
import sys

def find(x):
    if x == parents[x]: return x # 부모 == 본인
    else: # 부모 != 본인
        parents[x] = find(parents[x])  # 최종 조상을 찾아서 업데이트 하기 위해
        return parents[x]
    
def union(child1, child2):
    p1 = find(child1)
    p2 = find(child2)
    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2

n, m = map(int, sys.stdin.readline().strip().split())
parents = [i for i in range(n)]
answer = 0

for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    if find(v1) == find(v2):
        answer = i + 1
        break
    union(v1, v2)

print(answer)
