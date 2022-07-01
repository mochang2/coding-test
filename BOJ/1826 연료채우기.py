"""
20220701
골드3 연료 채우기
url: https://www.acmicpc.net/problem/1826
후기: 1 ≤ N ≤ 10,000 인 것을 보고 O(N log N)으로 풀 수 있는 방법에 대해 고민을 했다.
힙이나 DP일 것 같았는데, 예전에 푼 11000번 강의실배정 문제와 같은 느낌이 나서 힙으로 푸니 해결됐다.
"""

# 1826
import sys
import heapq as h

input_ = sys.stdin.readline

def CalcStopCounts(gas_stations, L, P):
    answer = 0
    heap = [] # 기본적으로 최소힙
    curr_pos = 0

    for distance, gas in gas_stations:
        #print()
        #print('distance', distance)
        #print('gas', gas)
        P -= distance
        #print('현재 기름양', P)
        
        # 도착
        if curr_pos >= L:
            #print('도착')
            #print(curr_pos, L)
            break

        # P < 0이라면 기름을 가장 많이 얻을 수 있는 위치에서 주유했어야 함
        while heap and P < 0:
            #print('주유')
            #print('heap', heap)
            gas_plus = -h.heappop(heap)
            P += gas_plus
            answer += 1

        # 목적지 도달 불가능
        if P < 0:
            return -1

        #print('keep')
        h.heappush(heap, -gas)

    return answer

# initialization
N = int(input_().strip())
gas_stations = [list(map(int, input_().strip().split())) for _ in range(N)]
L, P = map(int, input_().strip().split()) # 최종 거리, 기본 연료
gas_stations.sort(key=lambda x: (x[0], -x[1])) # 거리순으로 오름차순, 기름양으로 내림차순
gas_stations.append([L - gas_stations[-1][0], 0]) # 최종 지점까지의 거리도 
for i in range(N - 1, 0, -1): # stop 지점마다의 거리를 구함
    gas_stations[i][0] -= gas_stations[i - 1][0]
#print(gas_stations)

# print
print(CalcStopCounts(gas_stations, L, P))
