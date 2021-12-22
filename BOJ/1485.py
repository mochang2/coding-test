"""
211113
실버4 정사각형
url: https://www.acmicpc.net/problem/1485

후기 1. 굳이 실제 길이를 구하겠다고 sqrt를 쓸 필요가 없었다. 괜히 부동소수점 때문에 틀릴 수도 있으므로(잘은 모르겠지만)
쓰지 않아도 되면 sqrt를 쓸 필요가 없다.
후기 2. 처음에는 6 edges를 구하고 같은 길이 4개, 2개씩 있으면 무조건 정사각형이라고 했었으나 틀렸다. 반례는 잘 모르겠다.
후기 3. 후기 2처럼하다가 틀려서 그냥 정석대로 55번~65번까지의 조건을 붙이니 맞았다.
후기 4. 중학 수학 문제였던 것 같다. 
"""

import sys

res = []
T = int(input())
for i in range(T):
    li = []
    for _ in range(4):
        li.append(tuple(map(int, sys.stdin.readline().split())))

    dic = dict() # hash에 저장
    edge1 = (li[0][0] - li[1][0]) ** 2 + (li[0][1] - li[1][1]) ** 2  # 굳이 math.sqrt를 안 써도 괜찮음
    dic[edge1] = 1
    
    edge2 = (li[1][0] - li[2][0]) ** 2 + (li[1][1] - li[2][1]) ** 2
    if edge2 not in dic.keys():
        dic[edge2] = 1
    else:
        dic[edge2] += 1
        
    edge3 = (li[2][0] - li[3][0]) ** 2 + (li[2][1] - li[3][1]) ** 2
    if edge3 not in dic.keys():
        dic[edge3] = 1
    else:
        dic[edge3] += 1
        
    edge4 = (li[3][0] - li[0][0]) ** 2 + (li[3][1] - li[0][1]) ** 2
    if edge4 not in dic.keys():
        dic[edge4] = 1
    else:
        dic[edge4] += 1
        
    edge5 = (li[0][0] - li[2][0]) ** 2 + (li[0][1] - li[2][1]) ** 2
    if edge5 not in dic.keys():
        dic[edge5] = 1
    else:
        dic[edge5] += 1
        
    edge6 = (li[1][0] - li[3][0]) ** 2 + (li[1][1] - li[3][1]) ** 2
    if edge6 not in dic.keys():
        dic[edge6] = 1
    else:
        dic[edge6] += 1

    temp = sorted(list(dic.items()))
    if len(temp) != 2: # 길이가 같은 두 개의 대각선과 길이가 같은 네 개의 변만 남는지 확인하는 과정
        res.append(0)
        continue

    if temp[0][0] > temp[1][0]: # 대각선이 변보다는 길이가 길어야 함
        res.append(0)
        continue

    if temp[0][1] != 4:
        res.append(0)
        continue

    res.append(1)

for i in range(T):
    print(res[i])
    
