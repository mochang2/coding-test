"""
20220407
골드5 N-Queen
url: https://www.acmicpc.net/problem/9663
후기: 백트래킹의 정석이라고 한다. 개념은 어렵지 않았다. 다만 어떻게 하면 더 효율적인가에 대한 구상이 많이 필요했다.
맨 처음에는 겹치는 경우의 수도 구한 뒤 마지막에 n!로 나눠줬더니 말도 안되게 시간이 오래 걸렸다.
그 이후에도 combination 개념을 사용해서 계속 답은 나왔지만 N이 8이상이 되면 10초를 넘어갔다. 답을 본 후에야 10초 안에 풀 수 있었다.
https://www.youtube.com/watch?v=Enz2csssTCs&t=1161s 여기에서 설명을 봤다.
한 row에는 퀸을 1개만 둘 수 있고, 한 column에는 1개만 둘 수 있고, 각각의 대각선을 하나의 배열로 둘 때도 퀸을 1개만 둘 수 있다는데 착안한 풀이였다.
"""

## 시간초과
# combination처럼 품. O(196C14)면 시간초과
N = int(input())
board = [[0 for _ in range(N)] for __ in range(N)]
axis_li = []
for i in range(N):
    for j in range(N):
        axis_li.append((i, j))
dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)

def QueenRoute(y, x, operation):
    global board
    if operation == "+":
        board[y][x] += 1
        for direct in range(8):
            index = 1
            while True:
                new_y, new_x = y + dy[direct] * index, x + dx[direct] * index
                if not 0 <= new_y < N or not 0 <= new_x < N:
                    break
                board[new_y][new_x] += 1
                index += 1
    elif operation == "-":
        board[y][x] -= 1
        for direct in range(8):
            index = 1
            while True:
                new_y, new_x = y + dy[direct] * index, x + dx[direct] * index
                if not 0 <= new_y < N or not 0 <= new_x < N:
                    break
                board[new_y][new_x] -= 1
                index += 1

def Dfs(depth, index):
    global answer, board
    if depth == N: # depth가 N이 되면 성공
        answer += 1
        return

    for i, j in axis_li[index:]: # 사실상 2차원 배열 순회와 다르지 않음
        if board[i][j] == 0:
            QueenRoute(i, j, "+")
            Dfs(depth + 1, i * N + j)
            QueenRoute(i, j, "-")
    return

answer = 0
Dfs(0, 0)
print(answer)


## 정답
# 답을 봤을 때는 rows뿐만 아니라 대각선 list 두 개를 더 선언해서 총 세 가지를 비교했다.
# 다른 방식으로 풀어보고자 axis_li로 좌표를 저장해봤다.
# 대각선으로 위치할 수 있는지 여부를 표시하기 위함이다.
N = int(input())
columns = [False for _ in range(N)] # 각각의 row에 대해 몇 번째에 퀸이 위치했는지 여부 표시. True면 퀸이 존재
axis_li = [] # 대각선에 대해 판단하기 위해 좌표 저장

def Dfs(depth): # depth이자 row_index
    global answer, columns, axis_li
    if depth == N: # depth가 N이 되면 성공
        answer += 1
        return

    for i in range(N): # column index
        if not columns[i]:
            flag = True
            for y, x in axis_li:
                if abs(y - depth) == abs(x - i): # 대각 방향에 퀸이 존재하면
                    flag = False
                    break
            if not flag:
                continue
            
            columns[i] = True
            axis_li.append((depth, i))
            Dfs(depth + 1)
            columns[i] = False
            axis_li.pop()
    return

answer = 0
Dfs(0)
print(answer)
