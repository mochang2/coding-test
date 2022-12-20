"""
20220606
골드4 거짓말
url: https://www.acmicpc.net/problem/20056
후기: 오랜만에 푸는 삼성 구현 문제였다.
매번 실수하지만 문제에서 ~~한 경우 ~게 처리해라 라는 한 줄을 놓쳐서 개고생하고 틀리는 것 같다.
문제 꼼꼼히 읽고 필요한 부분은 항상 주석에 남겨서 잊지 않도록 해야겠다.
이번에도 '질량이 0이 된 파이어볼은 소멸되어 없어진다'라는 구문을 제대로 구현하지 않아서 계속 틀렸었다.
51번째 줄(2번째 단계)부터와 DecideDirection 함수가 이 문제의 제일 중요한 부분이었다.
"""

import sys
input_ = sys.stdin.readline
dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)

def Calc(li, divider):
    return sum(li) // divider

def IsEven(x):
    return x % 2 == True

def DecideDirection(directions):
    set_ = set(map(IsEven, directions))
    if len(set_) == 1:
        return True
    else:
        return False

# initialization
N, M, K = map(int, input_().strip().split())
fireballs = []
for _ in range(M):
    y, x, m, s, d = map(int, input_().strip().split())
    y -= 1
    x -= 1
    fireballs.append((y, x, m, s, d))

# 상어의 명령 K번 반복
for _ in range(K):
    # 0. board 초기화
    board = [[[] for _ in range(N)] for __ in range(N)]
    
    # 1. 모든 파이어볼이 이동
    for y, x, m, s, d in fireballs:
        new_y = (y + dy[d] * s) % N
        new_x = (x + dx[d] * s) % N
        board[new_y][new_x].append((m, s, d))
    fireballs = []
    
    # 2. 2개 이상의 파이어볼이 있는 칸에 변화
    for i in range(N):
        for j in range(N):
            balls = board[i][j]
            if len(balls) == 0:
                continue

            if len(balls) == 1:
                fireballs.append((i, j, balls[0][0], balls[0][1], balls[0][2])) # y, x, m, s, d
            else:
                m_list = [ball[0] for ball in balls]
                s_list = [ball[1] for ball in balls]
                d_list = [ball[2] for ball in balls]
                new_m = Calc(m_list, 5)
                if new_m == 0: # 질량이 0인 공은 소멸
                    continue
                new_s = Calc(s_list, len(balls))
                is_even = DecideDirection(d_list)

                if is_even:
                    for new_d in range(0, 8, 2):
                        fireballs.append((i, j, new_m, new_s, new_d))
                else:
                    for new_d in range(1, 9, 2):
                        fireballs.append((i, j, new_m, new_s, new_d))

# 질량의 합 출력
print(sum([fireball[2] for fireball in fireballs]))
