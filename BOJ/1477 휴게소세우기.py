"""
20220312
골드4 휴게소 세우기
url: https://www.acmicpc.net/problem/1477
후기: binary search(parametric search) 문제였다. 전에 프로그래머스 3단계 문제 중에서 비슷한 문제를 푼 적이 있다.
휴게소의 "위치"가 중요한 게 아니라 휴게소 간의 "거리"가 중점이다.
이유는 모르겠지만 초기 left를 0으로 설정하거나 left, right를 distance의 min, max 값으로 잡으면 틀린다.
테스트 케이스 공개가 안돼서 도저히 이유는 모르겠고, 저것 때문에 결국 답을 찾아봤다.
어떤 블로그를 보니 right는 L - 1로 해도 문제가 없는 것 같다.
"""

import sys

def Count(mid):
    # mid를 휴게소가 없는 구간이라고 가정할 때 설치해야 하는 최소 휴게소의 수를 출력
    global distances

    cnt = 0
    for distance in distances:
        if distance % mid == 0:
            cnt += (distance // mid) - 1
        else:
            cnt += distance // mid
        # cnt += (distance - 1) // mid로 해도 됨
    return cnt

N, M, L = map(int, sys.stdin.readline().strip().split())
pos = [0]
pos.extend(sorted(list(map(int, sys.stdin.readline().strip().split()))))
pos.append(L)
distances = []
for i in range(N + 1):
    distances.append(pos[i + 1] - pos[i])

left = 1 # min(distances)
right = L # max(distances)

# 휴게소가 없는 구간의 최댓값을 binary search로 찾을 때 추가 휴게소의 개수가 M개가 되는지 확인
while left <= right:
    mid = (left + right) // 2    
    cnt = Count(mid)
    if cnt > M: # 불가능한 상황
        left = mid + 1
    else: # 가능한 상황
        right = mid - 1
        result = mid
print(result)
