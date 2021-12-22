"""
211201
실버1 줄어드는 수
url: https://www.acmicpc.net/problem/1174
후기: 손으로도 셀 수 있으니 뭔가 조건에 맞는 모든 경우의 수를 조사하는 것 같았음. 다만 8중 while을 돌리는 것이 애매한 것 같아서 더 깔끔한 방법을 고민하다가 결국 답을 봄.
"""
# 1차 시도
# 1차 시도
def decreasing_num():
    global N
    if N < 10:
        return N - 1
    if N >= 500000:
        return -1
    # 1의 자리 시작 가능 숫자: 0
    # 10의 자리 시작 가능 숫자: 1
    # 100의 자리 시작 가능 숫자: 2
    # 1000의 자리 시작 가능 숫자: 3
    # 10000의 자리 시작 가능 숫자: 4
    # 100000의 자리 시작 가능 숫자: 5
    # 1000000의 자리 시작 가능 숫자: 6
    # 10000000의 자리 시작 가능 숫자: 7
    # 100000000의 자리 시작 가능 숫자: 8
    # 1000000000의 자리 시작 가능 숫자: 9
    # 9876543210 초과의 숫자는 감소하는 숫자가 될 수 없음.
    # 1의 자리 숫자를 1씩 더하다가 10의 자리 숫자랑 같아지면 10의 자리 숫자 + 1, 1의 자리 숫자는 0 => 10의 자리 숫자가 10이 되면 끝.
    # 이제 100의 자리 숫자를 변화시킴.
    
    num_of_digit = 2   # 몇 자리로 이루어진 수인가?
    count = 11 # 몇 번째인지
    while True:
        digit_li = [i for i in range(num_of_digit)]
        if len(digit_li) > 10: # 해당 숫자 > 9876543210
            return -1

        if count == N:
            return digit_li
        
        if digit_li == sorted(digit_li):
            count += 1

        if digit_li[num_of_digit - 1] == 10:
            continue

N = int(input())

print(decreasing_num())
# 여기까지 짜다가 8중 for문을 돌려야 되나 싶어서 포기.



# 2차 시도
from itertools import combinations

N = int(input())
digit = [i for i in range(10)]
res = []
for num_of_digit in range(1, 11): # 9876543210이 최대로 큰 줄어드는 수이므로, 10번만 돔.
    all_posibilities = list(combinations(digit, num_of_digit)) # 10C1 ~ 10C10까지 생성(총 2^10 - 1개)
    for each_posibility in all_posibilities:
        tmp = 0
        for i in range(num_of_digit, 0, -1):
            tmp += (10 ** (i - 1)) * each_posibility[i - 1]
        res.append(tmp)
res.sort()
    
if N < 1024:
    print(res[N - 1])
else:
    print(-1)
