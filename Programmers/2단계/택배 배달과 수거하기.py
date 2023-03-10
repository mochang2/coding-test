"""
230311
url: https://school.programmers.co.kr/learn/courses/30/lessons/150369
후기: 작년에 이 문제를 못 풀어서 코테 1차 탈했었는데... ㅂㄷㅂㄷ
이번에 편한 마음으로 다시 엣지케이스를 잡자고 생각하니 금방 풀렸다.

그리디로 해결한 문제이다.
1. 배달로 가야 하는 지점 가장 먼 지점(a)과 픽업으로 가야 하는 가장 먼 지점(b) 중 각각 구한다.
2. a와 b 중 더 큰 값의 2배(왕복값)을 total_distance에 더한다.
3. 배달과 픽업 중 각각 해야 할 일이 끝나지 않았으면 일이 완료되지 않은 지점 중 각각 더 먼 지점(a, b)를 구하고 2번부터 다시 반복한다.

아래는 시도한 테스트 케이스들이다.

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 'to be 16')
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 'to be 30')
print(solution(1, 5, [1 ,1 ,1 ,1 ,1], [0, 0, 0, 0, 0]), 'to be 30')
print(solution(1, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 'to be 30')
print(solution(50, 5, [50, 0, 0, 0, 0], [0, 0, 0, 0, 0]), 'to be 2')
print(solution(2, 2, [0, 0], [0, 4]), 'to be 8')
"""

def solution(capacity, n, deliveries, pickups):
    total_distance = 0

     # 시작점 세팅
    farthest_delivery_place = initializeFarthestPlace(n, deliveries)
    farthest_pickup_place = initializeFarthestPlace(n, pickups)
    
    while farthest_delivery_place != 0 or farthest_pickup_place != 0:
        # 배달로, 픽업으로 가야하는 곳 중 더 먼 곳 구해서 왕복 거리를 더함
        total_distance += 2 * max(farthest_delivery_place, farthest_pickup_place)
        farthest_delivery_place = getFarthestPlace(capacity, farthest_delivery_place, deliveries)
        farthest_pickup_place = getFarthestPlace(capacity, farthest_pickup_place, pickups)
    
    return total_distance

def initializeFarthestPlace(n, residues):
    for i in range(n, 0, -1):
        if residues[i - 1] != 0:
            return i

    return 0

def getFarthestPlace(capacity, current_place, residues):
    while current_place != 0 and capacity > 0: # 해야 할 일이 끝나지 않았고, 더 배달하거나 픽업할 수 있다면
        affordable_amount = min(capacity, residues[current_place - 1])
        capacity -= affordable_amount
        residues[current_place - 1] -= affordable_amount

        while current_place != 0 and residues[current_place - 1] == 0: # 해당 지점에서 일이 다 끝났다면, 다음 일을 해야 하는 지점 파악
            current_place -= 1
    
    return current_place
  
