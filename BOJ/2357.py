"""
20220416
골드1 최솟값과 최댓값
url: https://www.acmicpc.net/problem/18436
후기: 18436번을 풀고 세그먼트 트리를 연습하기 위해 바로 같이 풀었다.
단순히 linear하게 접근하면 시간초과가 난다.
그렇다고 부분합처럼 일정 구간의 최댓값, 최솟값을 저장해놓을 수도 없다.
풀 수 있는 유일한 방법은 세그먼트 트리이다.

세그먼트 트리. 0번째 인덱스는 사용하지 않음.
이는 complete tree의 장점 leftChild의 인덱스가 2i, rightChild의 인덱스가 2i + 1임을 이용하기 위함.
https://www.youtube.com/watch?v=075fcq7oCC8 여기 설명을 참고함.
세그먼트 트리와 부분합은 모두 일정 구간에 대한 답(합, gcd, max, min 등)을 빠르게 구할 수 있음.
다만 부분합과 달리 처음에 입력된 sequence가 변경되면 세그먼트 트리가 효율적이라고 함.
"""

import sys
input_ = sys.stdin.readline
maxInt = sys.maxsize
minInt = -sys.maxsize

def InitInput(x):
    return int(x) - 1

def Merge(option, leftValue, rightValue):
    if option == 'min':
        return min(leftValue, rightValue)
    return max(leftValue, rightValue)

def MakeSegment(option, node, leftRange, rightRange):
    global segment, sequence
    if leftRange == rightRange:
        if option == 'min':
            segment[node][0] = sequence[leftRange]
            return segment[node][0]
        else:
            segment[node][1] = sequence[leftRange]
            return segment[node][1]
            
    mid = (leftRange + rightRange) // 2
    leftValue = MakeSegment(option, node * 2, leftRange, mid)
    rightValue = MakeSegment(option, node * 2 + 1, mid + 1, rightRange)
    if option == 'min':
        segment[node][0] = Merge(option, leftValue, rightValue)
        return segment[node][0]
    else:
        segment[node][1] = Merge(option, leftValue, rightValue)
        return segment[node][1]

def Get(option, queryLeft, queryRight, node, leftRange, rightRange):
    global segment, maxInt, minInt
    if queryLeft > rightRange or queryRight < leftRange: # 고려할 부분이 아님. 결과에 영향을 끼치지 않아야 함
        if option == 'min': # 무조건 엄청 큰 값 반환
            return maxInt
        else: # 무조건 엄청 작은 값 반환
            return minInt

    if queryLeft <= leftRange and rightRange <= queryRight: # query range에 포함되면
        if option == 'min': # 본인의 최솟값 반환
            return segment[node][0]
        else: # 본인의 최댓값 반
            return segment[node][1]

    mid = (leftRange + rightRange) // 2
    leftValue = Get(option, queryLeft, queryRight, node * 2, leftRange, mid)
    rightValue = Get(option, queryLeft, queryRight, node * 2 + 1, mid + 1, rightRange)
    return Merge(option, leftValue, rightValue)

N, M = map(int, input_().strip().split())
sequence = []
for _ in range(N):
    sequence.append(int(input_().strip()))
segment = [[0, 0] for _ in range(4 * N)] # [min, max]
MakeSegment('min', 1, 0, N - 1)
MakeSegment('max', 1, 0, N - 1)
for _ in range(M):
    a, b = map(InitInput, input_().strip().split()) # start index, end index
    print(Get('min', a, b, 1, 0, N - 1), end=" ")
    print(Get('max', a, b, 1, 0, N - 1))
