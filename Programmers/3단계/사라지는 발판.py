"""
220505
2022 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/92345
후기: 게임이론 미니맥스 알고리즘을 알아야 한다고 한다. 문제로 나오면 절대 못 풀 거 같다.

흐름
1. 선공인 친구가 dy, dx 에 따라 순서대로 하나씩 움직여봄
2. 이에 따라 후공인 친구도 dy, dx에 따라 순서대로 하나씩 움직여봄
(3부터는 선공인 친구 위주로 서술)
3. 최종적으로 결과가 이기면 이기는 방법 고수 또는 다른 방향으로 움직여봄으로써 더 빠르게, 반드시 이길 수 있는지 파악
4. 지면 최대한 늦게 지는 방법을 고수 또는 다른 방향으로 움직여봄으로써 이길 수 있는지 파악
"""

"""
각 위치에서 완전탐색으로 갈 수 있는 모든 방향을 탐색했을 때,
이길 수 있는 케이스가 있다면 그 중에서도 최선으로 이기는 케이스를 리턴한다.
질 수 밖에 없다면 최대한 오래 버티는 케이스를 리턴한다.
"""
# print는 디버깅

dy = (-1, 0, 1, 0)
dx = (0, 1, 0 ,-1)
col_len = 0
row_len = 0

def outOfRange(y, x):
    return not 0 <= y < row_len or not 0 <= x < col_len

def isFinished(loc, board):
    for direct in range(4):        
        y, x = loc[0], loc[1]
        new_y, new_x = y + dy[direct], x + dx[direct]
        if not outOfRange(new_y, new_x) and board[new_y][new_x] == 1:
            return False
    return True

def dfs(aloc, bloc, board, whosTurn): # aloc: 현재 순서, bloc: 다음 순서
    # return (canWin: bool, turn: int)
    if isFinished(aloc, board): # dfs 끝나는 조건 1. 더이상 움직일 수 없다.
        return (False, 0) # 현재 차례인 애가 움직일 수 없어서 짐
        # return 받는 애는 그 다음 차례이므로 이김
    if aloc == bloc: # dfs 끝나는 조건 2. 둘의 위치가 같다.
        return (True, 1) # 현재 차례인 애가 움직임으로써 이김
        # return 받는 애는 그 다음 차례이므로 짐

    maxTurn = 0
    minTurn = 1000000
    canWin = False # 위로 가면 질 수도 있는데, 아래로 가면 반드시 이길 수도 있는 경우가 존재
    # 그러한 경우 때문에 for문 밖에서 초기화 필요
    
    for direct in range(4):
        y, x = aloc[0], aloc[1]
        new_y, new_x = y + dy[direct], x + dx[direct]
        if outOfRange(new_y, new_x):
            continue

        if board[new_y][new_x] == 1:
            print("in for (", y, x, ") -> (", new_y, new_x, ")")
            board[y][x] = 0
            gameResult = dfs(bloc, [new_y, new_x], board, -whosTurn)
            board[y][x] = 1

            if not gameResult[0]: # return 값의 반대. 내가 이긴다면
                minTurn = min(minTurn, gameResult[1])
                turn = minTurn
                canWin = True
                print("win", whosTurn, "turn", turn)
            elif not canWin:
                maxTurn = max(maxTurn, gameResult[1])
                turn = maxTurn
                print("cannot win", whosTurn, "turn", turn)

    print("out for", whosTurn, turn + 1)
    print()
    return (canWin, turn + 1)
    
def solution(board, aloc, bloc):
    global col_len, row_len
    
    row_len = len(board)
    col_len = len(board[0])
    answer = dfs(aloc, bloc, board, 1) # 마지막 인자 whosTurn은 디버깅 용도로 넣음
    
    return answer[1]

print("solution:", solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
