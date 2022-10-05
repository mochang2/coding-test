"""
20221005
실버1 쿼드트리
url: https://www.acmicpc.net/problem/1992
후기: 분할 정복 문제이다.
문제가 이해가 안 돼서 검색해보니 주어진 입력을 계속해서 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래로 4등분해서 분할 정복하면 되는 문제였다.
이제 재귀는 dp 재귀 정도만 아니면 잘 풀 수 있겠다.
디버깅은 좀 여전히 힘들다...

모든 숫자가 0, 1로만 이루어진 입력을 억지로 ()를 씌우다가 틀렸다.
해당 출력은 (0), (1)이 아닌 그냥 0 또는 1이면 된다.
"""

import sys

input_ = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def isAllSame(y_start, x_start, y_end, x_end, video):
    value = video[y_start][x_start]

    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            if value != video[y][x]:
                return False

    return True

def makeQuadTree(y_start, x_start, y_end, x_end, video):
    if isAllSame(y_start, x_start, y_end, x_end, video):
        return video[y_start][x_start]

    result = '('
    result += makeQuadTree(
        y_start,
        x_start,
        y_start + (y_end - y_start) // 2,
        x_start + (x_end - x_start) // 2,
        video
    )
    result += makeQuadTree(
        y_start,
        x_start + (x_end - x_start) // 2,
        y_start + (y_end - y_start) // 2,
        x_end,
        video
    )
    result += makeQuadTree(
        y_start + (y_end - y_start) // 2,
        x_start,
        y_end,
        x_start + (x_end - x_start) // 2,
        video
    )
    result += makeQuadTree(
        y_start + (y_end - y_start) // 2,
        x_start + (x_end - x_start) // 2,
        y_end,
        x_end,
        video
    )
    result += ')'

    return result
    
# initialization
n = int(input_().strip())
video = [input_().strip() for _ in range(n)]

# print
print(makeQuadTree(0, 0, n, n, video))
