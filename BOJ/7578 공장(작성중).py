"""
20221109
플레5 공장
url: https://www.acmicpc.net/problem/7578
후기: 겁나 어려웠다. 답을 안 봤으면 한 달 줘도 못 풀었을 것 같다.
이 문제의 분류는 inversion couting이다.
배열의 인덱스 i, j에서 i < j일 때 arr[i] > arr[j]인 개수를 구하는 문제를 inversion couting이라고 한다.

inversion counting을 해결할 수 있는 방법은 크게 두 가지가 있다.
segment tree와 merge sort이다.

나는 segment tree를 이용했고 다음과 같이 풀었다.
  1. 공장의 모든 bottom lane을 방문하지 않은 상태로 초기화한다.
  2. 공장의 top lane을 하나씩 확인하며, bottom lane에서의 짝꿍 위치를 파악한다.
  3. bottom lane에서 짝꿍의 오른쪽을 확인했을 때 먼저 방문한 지점의 개수를 확인한다. 해당 개수가 교차하는 개수이다.
  4. bottom lane에서 방문한 짝꿍을 방문했다고 표시한다.
그림으로 이해하면 쉽다. https://justicehui.github.io/koi/2018/11/20/BOJ7578 에 잘 나와 있다.
이 문제를 위해 segment tree를 이용한 이유는 완전 탐색을 하면 O(n^2)의 시간 복잡도가 걸리지만
segment tree를 이용하면 O(n log n)으로 가능하기 때문이다.
bottom lane의 특정 위치를 방문하지 않았음을 0으로, 방문했음으로 1로 표현한다면 방문 여부를 구간합처럼 표현할 수 있다.

merge sort는 정렬 시 합병 과정에서 교차하는 개수를 세면 된다.
다른 inversion counting 문제에서 해당 풀이를 이해할 수 있었다.
(https://eine.tistory.com/entry/%EB%B0%B1%EC%A4%80-10090%EB%B2%88-%EB%AC%B8%EC%A0%9C-Counting-Inversions-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4)
이 문제에서 merge sort를 사용하면 sort를 위한 기준이 필요하고(기계의 번호는 unique id일 뿐 크기가 의미가 없으므로),
쌍이 일치하도록 bottom lane을 한 번 더 순회해야 되기 때문에 나는 segement tree를 선택했다.


다음은 내가 만든 테스트들이다(사실 이 문제의 요점은 엣지케이스에서 답이 맞냐보다는 효율성을 위주로 보는 느낌이긴 하다).

1)
input
3
1 2 3
1 2 3

output
0

2)
input
2
1 2
2 1

output
1

3)
input
3
1 2 3
2 3 1

output
2

4)
input
5
1 2 3 4 5
3 4 1 2 5

output
4

5)
input
3
1 2 3 4 5
3 4 1 2 5

output
5

6)
input
3
1 2 3 4 5
4 3 2 1 5

output
6
"""

import sys

input_ = sys.stdin.readline
SEGMENT_DEFAULT_VALUE = 0

def getPosition(iterable):
    position = dict()

    for index, element in enumerate(iterable):
        position[element] = index

    return position

def makeSegment(original_length):
    global SEGMENT_DEFAULT_VALUE
    
    return [SEGMENT_DEFAULT_VALUE for _ in range(original_length * 4)]

def merge(value1, value2):
    return value1 + value2

def getValuesInRange(query_left, query_right, node, range_left, range_right):
    global segment, SEGMENT_DEFAULT_VALUE

    if range_right < query_left or range_left > query_right:
        return SEGMENT_DEFAULT_VALUE

    if query_left <= range_left and range_right <= query_right:
        return segment[node]

    range_mid = range_left + (range_right - range_left) // 2
    left_value = getValuesInRange(query_left, query_right, node * 2, range_left, range_mid)
    right_value = getValuesInRange(query_left, query_right, node * 2 + 1, range_mid + 1, range_right)

    return merge(left_value, right_value)

def updateValuesInRange(position, value, node, range_left, range_right):
    global segment

    if range_right < position or position < range_left:
        return segment[node]

    if range_left == range_right:
        segment[node] = value
        
        return segment[node]

    range_mid = range_left + (range_right - range_left) // 2
    left_value = updateValuesInRange(position, value, node * 2, range_left, range_mid)
    right_value = updateValuesInRange(position, value, node * 2 + 1, range_mid + 1, range_right)
    segment[node] = merge(left_value, right_value)

    return segment[node]

def visit(position):
    global lane_length
    
    updateValuesInRange(position, 1, 1, 0, lane_length - 1)

def countInversion(position):
    global lane_length, SEGMENT_DEFAULT_VALUE

    if position == lane_length - 1:
        return SEGMENT_DEFAULT_VALUE
    
    return getValuesInRange(position + 1, lane_length - 1, 1, 0, lane_length - 1)

def countIntersections():
    global top_lane, bottom_lane, bottom_lane_position
    
    number_of_intersections = 0

    for id_ in top_lane:
        if id_ in bottom_lane_position:
            position_in_bottom = bottom_lane_position[id_]

            number_of_intersections += countInversion(position_in_bottom)
            visit(position_in_bottom)

    return number_of_intersections

# initialization
lane_length = int(input_().strip())
top_lane = tuple(map(int, input_().strip().split()))
bottom_lane = tuple(map(int, input_().strip().split()))
bottom_lane_position = getPosition(bottom_lane)

# print answer
segment = makeSegment(lane_length)
number_of_intersections =  countIntersections()
print(number_of_intersections)
