"""
211105
2020 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/60059
후기: 효율성 테스트가 없었으니 처음부터 끝까지 빡구현하면 된다.

흐름
1. lock을 거대한 널빤지 중간에 위치시킴
2. key를 0도, 90도, 180도, 270도 회전시킨 내용을 가지고 있음
3. 모든 key를 한 칸씩 움직이면서 lock과 xor 시킴
4. 거대한 널빤지 중간에 있는 lock의 모든 인자가 1이면 true를 return
5. 인자 중 하나라도 0이 있으면 3 단계부터 반복. 모두 실피하면 false를 return
"""

def locate_lock(m, n, lock):
    new_lock = [[0 for _ in range(2 * m + n - 2)] for __ in range(2 * m + n -2)]
    for i in range(n):
        for j in range(n):
            new_lock[m - 1 + i][m - 1 + j] = lock[i][j]
    return new_lock


def rotate_90_deg(key_li, m):
    tmp = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if key_li[-1][i][j] == 1:
                tmp[j][m-i-1] = 1
    key_li.append(tmp)


def clear_lock(m, n, lock, origin_lock):
    for k in range(n):
        for o in range(n):
            lock[m - 1+ k][m - 1 + o] = origin_lock[k][o]

def move_key(m, n, key, lock, origin_lock):
    for i in range(m + n - 1): # key를 y축으로 이동
        for j in range(m + n - 1): # key를 x축으로 이동
            for k in range(m): # key의 y축
                for o in range(m): # key의 x축
                    lock[i + k][j + o] = key[k][o] ^ lock[i + k][j + o] # 속도: xor > +
            
            flag = True
            for k in range(n):
                for o in range(n):
                    if lock[m - 1 + k][m - 1 + o] != 1: # 넓은 널판지 중간에 있는 lock이 전부 1인지 확인
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                return True # 해결
            else:
                clear_lock(m, n, lock, origin_lock)

    return False


def solution(key, lock):
    m = len(key)
    n = len(lock)

    origin_lock = lock.copy()
    lock = locate_lock(m, n, lock) # 넓은 널판지 중간에 lock을 배치시킴

    key_li = [key] # 0, 90, 180, 270도 회전한 키 모양을 다 모아두는 리스트
    for i in range(3):
        rotate_90_deg(key_li, m)
    
    for i in range(4): # key 각도마다 시도
        if move_key(m, n, key_li[i], lock, origin_lock):
            return True
    return False
