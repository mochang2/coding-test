"""
20220403
골드4 알파벳
url: https://www.acmicpc.net/problem/1987
후기: 구현은 정말 쉬웠다. 하지만 시간초과를 잡는 것이 일이었다.
첫 번째 예시는 dictionary를 써서 시간 초과가 난 풀이다.
두 번째 예시는 ascii 값을 토대로 list indexing을 해서 통과한 풀이다.
dictionary 조회는 최선이 O(1) 최악이 O(N)이기 때문에 발생한 문제라고 한다.
https://www.acmicpc.net/board/view/56580 와
https://thecodingbot.com/time-complexity-analysis-of-python-dictionarys-get-method/ 에 나와 비슷한 문제가 나와 있었다.
오늘만큼은 개같은 파이썬...

# depth 최대 400(O^2)인 DFS, 시간 제한 2초이므로 완탐 가능.
# 일반적인 dfs처럼 visited라는 이차원 배열을 선언할 필요가 없음. dic으로 확인하면 됨.
"""


## 시간 초과
# 입력과 관계 없는 초기화
import sys
input_ = sys.stdin.readline
dy = (-1, 0, 1, 0) # 상 우 하 좌
dx = (0, 1, 0, -1)
dic = dict() # dfs 이미 지나간 알파벳이 아니어야 함.
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for alphabet in alphabets:
    dic[alphabet] = False

def dfs(y, x, result):
    global answer
    answer = max(answer, result)

    dic[board[y][x]] = True
    for direct in range(4):
        new_y, new_x = y + dy[direct], x + dx[direct]
        if not 0 <= new_y < R or not 0 <= new_x < C or dic[board[new_y][new_x]]:
            continue

        dfs(new_y, new_x, result + 1)
    dic[board[y][x]] = False

# initialization
answer = 1
R, C = map(int, input_().strip().split())
board = []
for _ in range(R):
    board.append(input_())

dfs(0, 0, answer)

print(answer)



## 통과
# 입력과 관계 없는 초기화
import sys
input_ = sys.stdin.readline
dy = (-1, 0, 1, 0) # 상 우 하 좌
dx = (0, 1, 0, -1)
alphabets = [False for _ in range(26)] # 이미 지나간 알파벳이 아니어야 함.

def to_num(x):
    return ord(x) - ord('A')

def dfs(y, x, result):
    global answer
    answer = max(answer, result)

    alphabets[to_num(board[y][x])] = True
    for direct in range(4):
        new_y, new_x = y + dy[direct], x + dx[direct]
        if not 0 <= new_y < R or not 0 <= new_x < C or alphabets[to_num(board[new_y][new_x])]:
            continue

        dfs(new_y, new_x, result + 1)
    alphabets[to_num(board[y][x])] = False

# initialization
answer = 1
R, C = map(int, input_().strip().split())
board = []
for _ in range(R):
    board.append(input_())

dfs(0, 0, answer)

print(answer)
