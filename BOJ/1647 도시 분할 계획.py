"""
20220530
골드4 도시 분할 계획
url: https://www.acmicpc.net/problem/1647
후기: union find를 이용한 크루스칼 알고리즘이다.
이번에도 union find를 까먹어서 다시 검색했다.
find는 이제 재귀적으로 호출해야지 최적화가 된다는 사실에 익숙하지만
union에서 25th, 27th 인덱스에 find로 찾은 parent가 들어간다는 사실을 잊었었다.
"""

import sys
input_ = sys.stdin.readline

def find(x):
    global parents
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]
    
def union(x, y):
    global parents
    parent_x, parent_y = find(x), find(y)
    if parent_x > parent_y:
        parents[parent_x] = parent_y
    else:
        parents[parent_y] = parent_x
        
# initialization
answer = 0 # 길의 유지비
count = 0 # 연결된 도시 개수
N, M = map(int, input_().strip().split())
if N == 2: # 연결짓지 않아도 됨
    print(0)
    sys.exit(0)
    
costs = []
parents = [i for i in range(N + 1)]
for _ in range(M):
    costs.append(tuple(map(int, input_().strip().split())))
costs.sort(key=lambda x: (x[2]))
for x, y, cost in costs: # 크루스칼 알고리즘. cost가 작은 간선부터 연결지어봄
    if find(x) == find(y):
        continue
    union(x, y)
    answer += cost
    count += 1
    if count == N - 2:
        break
    
print(answer)
