"""
20220529
골드5 AC
url: https://www.acmicpc.net/problem/5430
후기: 오랜만에 엄청 많이 틀렸다.
단순 구현 문제였는데 엣지 케이스를 잡는데 오래 걸렸다.

찾아본 반례
2
D
0
[] # error
R
0
[] # []
"""

# O(len(funcs)) = 100,000, O(n) = 100,000 이므로 모든 funcs마다 list를 reverse하면 시간 초과가 난다.
# deque을 써서 head, tail 모두에서 pop을 할 수 있도록 해야 시간초과가 나지 않는다.


# 오답
""" 반례 74th line. sys.exit(0) 때문에 틀림 => continue로 바꿔주기
3
D
0
[] 
R
0
[]
R
0
[]
"""

import sys
from collections import deque
input_ = sys.stdin.readline

def StringToInt(string):
    return int(string.strip())

def MakeList(input_):
    # 입력 받은 내용 중 '[', ']'를 제외하고 deque로 변환
    string_li = input_[1:-1]
    if string_li:
        return deque(list(map(StringToInt, string_li.split(','))))
    else: # 빈 리스트를 입력받았으면 StringToInt 함수에서 throw exception이 발생
        return deque([])

T = int(input_().strip())
for _ in range(T):
    try:
        right = True # list가 역순인지(left) 아닌지(right).
        funcs = input_().strip()
        n = int(input_().strip())
        li = MakeList(input_().strip())

        for func in funcs:
            if func == 'R':
                right = not right
            elif func == 'D':
                n -= 1
                if right:
                    li.popleft()
                else:
                    li.pop()
                    
        if not right:
            li.reverse()
            
        if n == 0: # 아래에 li[-1]에서 에러가 나지 않도록 하기 위해
            print('[]')
            sys.exit(0)
            
        li = list(li) # deque은 index slicing이 되지 않음. itertools.islice로도 해결가능
        print('[', end='')
        for num in li[:-1]:
            print(str(num) + ',', end='')
        print(str(li[-1]) + ']')
    except Exception as e:
        print('error')


# 정답
# int로 변환할 필요가 없었음
import sys
from collections import deque
input_ = sys.stdin.readline

def MakeDeque(input_):
    # 입력 받은 내용 중 '[', ']'를 제외하고 deque로 변환
    string_li = input_[1:-1]
    if string_li:
        return deque(string_li.split(','))
    else: # 빈 리스트를 입력받았을 때
        return deque([])

T = int(input_().strip())
for _ in range(T):
    try:
        right = True # list가 역순인지(left) 아닌지(right).
        funcs = input_().strip()
        n = int(input_().strip()) # 사용 X
        queue = MakeDeque(input_().strip())

        for func in funcs:
            if func == 'R':
                right = not right
            elif func == 'D':
                if right:
                    queue.popleft()
                else:
                    queue.pop()
                    
        if not right:
            queue.reverse()
        print('[' + ','.join(queue) + ']')
        
    except Exception as e:
        print('error')

