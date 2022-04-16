"""
20220416
골드1 수열과 쿼리 37
url: https://www.acmicpc.net/problem/18436
후기: O(NM) > 1억이므로 단순히 풀면 안 됐다.
처음에는 부분합이라고 생각했으나 1억 번 이내에 해결할 수 있는 방도를 생각이 안 나서 문제 구분을 확인해보니 세그먼트 트리라고 했다.
세그먼트 트리를 만드는 쉬운 모듈이 있나 싶어서 찾아봤지만 pip install을 해야 된다. 실제 코딩테스트에서는 써먹을 수 없을 것 같으니 따로 공부하진 않았다.

세그먼트 트리. 0번째 인덱스는 사용하지 않음.
이는 complete tree의 장점 leftChild의 인덱스가 2i, rightChild의 인덱스가 2i + 1임을 이용하기 위함.
https://www.youtube.com/watch?v=075fcq7oCC8 여기 설명을 참고함.
세그먼트 트리와 부분합은 모두 일정 구간에 대한 답(합, gcd, max, min 등을 빠르게 구할 수 있음.
다만 부분합과 달리 처음에 입력된 sequence가 변경되면 세그먼트 트리가 효율적이라고 함.
"""

# 세그먼트 트리가 sum을 나타날 때의 코드 예시
def Merge(leftValue, rightValue): # 입력: 좌,우 자식의  value
    return leftValue + rightValue # 출력: 자식 value들의 합

def Make_Segment(node, rangeLeft, rangeRight):
    # 입력: 해당 노드의 세그먼트 트리 번호 / 커버하는 자식들의 수열 인덱스
    # 출력: 해당 노드의 value
    global segment, sequence
    if rangeLeft == rangeRight: # 커버하는 자식들의 구간이 동일 -> 재귀를 통해 leaf 도달
        segment[node] = sequence[rangeLeft]
        return segment[node]

    mid = (rangeLeft + rangeRight) // 2
    leftValue = Make_Segment(node * 2, rangeLeft, mid)
    rightValue = Make_Segment(node * 2 + 1, mid + 1, rangeRight)
    segment[node] = Merge(leftValue, rightValue)
    return segment[node]

def Get(queryLeft, queryRight, node, rangeLeft, rangeRight):
    # 입력: 쿼리의 수열 좌우 끝 인덱스 / 해당 노드의 세그먼트 트리 번호 / 커버하는 자식들의 수열 인덱스
    # 출력: 쿼리의 결과문
    global segment
    if queryRight < rangeLeft or queryLeft > rangeRight: # 쿼리 인덱스를 전혀 커버하지 않으면
        return 0 # default 값
    if queryLeft <= rangeLeft and rangeRight <= queryRight: # 쿼리 인덱스가 커버 인덱스를 포함하면
        return segment[node] # leaf가 포함된 현재 세그먼트 트리의 값

    # 커버 인덱스가 쿼리 인덱스를 일부분 포함하고 있다면
    mid = (rangeLeft + rangeRight) // 2
    leftValue = Get(queryLeft, queryRight, node * 2, rangeLeft, mid)
    rightValue = Get(queryLeft, queryRight, node * 2 + 1, mid + 1, rangeRight)
    return Merge(leftValue, rightValue)

def Update(queryIndex, newValue, node, rangeLeft, rangeRight): # 인덱스 하나에 대해서만 업데이트. 여러 개를 업데이트 하고 싶어도 성능은 비슷하다고 함.
    # 입력: 쿼리의 수열 인덱스 / 해당 노드의 세그먼트 트리 번호 / 커버하는 자식들의 수열 인덱스 / 변화되는 값
    # 쿼리: 세그먼티 트리에서 업데이트된 값
    global segment
    if queryIndex < rangeLeft or queryIndex > rangeRight: # 쿼리 인덱스를 전혀 커버하지 않으면
        return segment[node] # 현재값
    
    if rangeLeft == rangeRight: # 세그먼트 트리에서 업데이트 해야되는 위치를 찾으면
        segment[node] = newValue
        return segment[node]

    # 커버 인덱스가 쿼리 인덱스를 포함하고 있다면
    mid = (rangeLeft + rangeRight) // 2
    leftValue = Update(queryIndex, newValue, node * 2, rangeLeft, mid)
    rightValue = Update(queryIndex, newValue, node * 2 + 1, mid + 1, rangeRight)
    segment[node] = Merge(leftValue, rightValue)
    return segment[node]
  
  

## 실제 코드
# 홀수의 개수를 저장하는 세그먼트 트리를 만듦
# 홀수의 개수를 원하면 세그먼트 트리 값의 합을 반환
# 짝수의 개수를 원하면 last index - false index + 1 - 홀수의 개수(세그먼트 트리 참조)를 반환
import sys
input_ = sys.stdin.readline

def Merge(leftValue, rightValue):
    return leftValue + rightValue

def Make_Segment(node, leftRange, rightRange):
    global segment, sequence
    if leftRange == rightRange:
        segment[node] = sequence[leftRange] % 2
        return segment[node]

    mid = (leftRange + rightRange) // 2
    leftValue = Make_Segment(node * 2, leftRange, mid)
    rightValue = Make_Segment(node * 2 + 1, mid + 1, rightRange)
    segment[node] = Merge(leftValue, rightValue)
    return segment[node]

def Get(queryLeft, queryRight, node, leftRange, rightRange):
    global segment
    if queryLeft > rightRange or queryRight < leftRange:
        return 0

    if queryLeft <= leftRange and rightRange <= queryRight:
        return segment[node]

    mid = (leftRange + rightRange) // 2
    leftValue = Get(queryLeft, queryRight, node * 2, leftRange, mid)
    rightValue = Get(queryLeft, queryRight, node * 2 + 1, mid + 1, rightRange)
    return Merge(leftValue, rightValue)

def Update(index, newValue, node, leftRange, rightRange):
    global segment
    if index < leftRange or index> rightRange:
        return segment[node]

    if leftRange == rightRange:
        segment[node] = newValue % 2
        return segment[node]

    mid = (leftRange + rightRange) // 2
    leftValue = Update(index, newValue, node * 2, leftRange, mid)
    rightValue = Update(index, newValue, node * 2 + 1, mid + 1, rightRange)
    segment[node] = Merge(leftValue, rightValue)
    return segment[node]
    

N = int(input_().strip())
sequence = list(map(int, input_().strip().split()))
segment = [0 for _ in range(4 * N)]
Make_Segment(1, 0, N - 1)
M = int(input_().strip())
for _ in range(M):
    num, i, x = map(int, input_().strip().split()) # i sequence의 index, x는 sequence의 index 또는 update로 바꿀 값
    if num == 1:
        Update(i - 1, x, 1, 0, N - 1)
    elif num == 2:
        print(x - i + 1 - Get(i - 1, x - 1, 1, 0, N - 1))
    else: # num == 3:
        print(Get(i - 1, x - 1, 1, 0, N - 1))

 
