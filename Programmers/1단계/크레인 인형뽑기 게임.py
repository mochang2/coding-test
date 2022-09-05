"""
220905
2019 카카오 개발자 겨울 인턴십
url: https://programmers.co.kr/learn/courses/30/lessons/64061
후기: 과거에 풀었던 것이 생각났다. 그때 되게 어렵고 더럽게 풀었는데 이번엔 훨씬 쉽고 간편하게 풀어서 기분이 좋았다.
"""

## 예전에 푼 코드. 정답
def solution(board, moves):
    #initialize
    answer = 0
    result_stack=[]
    n = len(board)
    n_minus_height_of_column = [-1]*n  #counts the number of zero for each column
    
    #i traces row, j traces column
    #board[i][j]
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and n_minus_height_of_column[j] == -1:
                n_minus_height_of_column[j] = i
    

    for j in moves:
        if n_minus_height_of_column[j-1] != n:# and board[n_minus_height_of_column[j-1]][j-1] != 0:
            # if they are same, that column is empty
            result_stack.append(board[n_minus_height_of_column[j-1]][j-1])
            #board[n_minus_height_of_column[j-1]][j-1] = 0
            n_minus_height_of_column[j-1] += 1
        if len(result_stack) >= 2:
            if result_stack[-2] == result_stack[-1]:
                result_stack.pop()
                result_stack.pop()
                answer+=2
        
    return answer


## 새롭게 푼 코드. 정답
def rotate(board): # 왼쪽으로 90도 회전
    n = len(board)
    new_board = [[0 for _ in range(n)] for __ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_board[j][n - 1 - i] = board[i][j]
    
    for index in range(n):
        while new_board[index] and new_board[index][-1] == 0: # 0인 부분 pop
            new_board[index].pop()
    
    return new_board

def solution(board, moves):
    answer = 0
    stack = []
    new_board = rotate(board)
    
    for move in moves:
        if new_board[move - 1]:
            stack.append(new_board[move - 1].pop())
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
                
    return answer
