"""
20221011
골드1 외판원 순회
url: https://www.acmicpc.net/problem/2098
후기: 10971 외판원 순회2의 상위 버전이다.
이 문제를 보기 전에 해당 문제 먼저 풀어볼 걸 그랬다...

그림을 그려보면 MST와 완전 다른 모양이다.
그래서 크루스칼이나 프림이 떠올랐다가 바로 머릿속에서 지워버렸다.

문제를 읽자마자 답이 없다는 것을 알고 외판원 순회 알고리즘 설명 영상을 찾아나섰다.
https://www.youtube.com/watch?v=wj44Dd0zdzM&t=1328s
해당 알고리즘과 비트 마스킹, 출발지 선정(결론적으로 출발지를 어디로 잡아도 상관 없다)과 관련해서 가장 잘 설명해준 영상이다.
다만 해당 알고리즘으로 이 문제를 풀면 (나는 애초에 구현을 잘못해서 오답이었고) 시간 초과가 날 만한 시간 복잡도이다.

그래서 별도로 이 문제를 위한 답을 찾아봤다.
https://shoark7.github.io/programming/algorithm/introduction-to-tsp-and-solve-with-exhasutive-search
https://shoark7.github.io/programming/algorithm/solve-tsp-with-dynamic-programming
위 두 페이지에서 해당 문제를 완탐으로 푸는 방법부터 dp로 확장하는 방법까지 설명했다.

(dp로 풀어야 한다고 결정이 났다면)내가 이해한 바는
1. dp를 선언한다.
  - row의 개수는 n, column의 개수는 2 ** n이다.
  - 초기화와 관련된 부분은 아래에서 하겠다.
  - column의 개수가 2 ** n인 이유는 비트 마스킹을 사용하기 위해서이다.
  - 지나간 경로를 비트 마스킹으로 표시하여 시간 복잡도도, 공간 복잡도도 줄일 수 있다.
2. 모든 경로를 돌아 다시 시작점으로 올 수 있다면 정답을 갱신한다.
3. 돌다가 이미 연산된 지점(dp)이라면 dp를 반환한다.

dfs 중단 조건은
1. visited == ALL_VISITED
2. dp[current][visited] != -1 (기존 코드: dp[current][visited] != INF)
이다.

처음에 dp 초기화를 INF(sys.maxsize)로 했었다.
하지만 그렇게 하면 첫번째 dfs + dp 중단 조건이 많이 발생하지 않아 완탐으로 이어지는 경우가 있다.
아래와 같이 0번째 도시와 이어진 도시가 하나밖에 존재하지 않는 경우가 있다.

16
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1
0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0

output: 16

그래서 아래 정답 코드와 같이 dp는 -1로 초기화해야 한다
"""

import sys

input_ = sys.stdin.readline
INF = sys.maxsize # 파이썬은 maxsize + 100을 해도 오버플로우가 발생하지 않음

def dfs(current, visited):
    global INF, dp, costs, ALL_VISITED

    if visited == ALL_VISITED:
        return costs[current][0] or INF # 마지막 방문 지점이 시작점인 0과 이어져 있거나 or 이어져 있지 않거나

    if dp[current][visited] != -1: # 이미 계산한 내용이라면
        return dp[current][visited]

    min_cost = INF
    for next_vertex in range(1, n):
        if (visited & (1 << next_vertex)) != 0 or costs[current][next_vertex] == 0:
            # next_vertex를 이미 방문했거나 current와 이어져 있지 않다면
            continue
        
        min_cost = min(
            min_cost,
            dfs(next_vertex, visited | (1 << next_vertex)) + costs[current][next_vertex] # | 연산 대신 + 해도 되지만 bit 연산이 보통 더 빠름
        )

    dp[current][visited] = min_cost

    return dp[current][visited]

# initialization
n = int(input_().strip()) # number of cities
costs = [list(map(int, input_().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(2 ** n)] for __ in range(n)]
ALL_VISITED = 2 ** n - 1

print(dfs(0, 1))
