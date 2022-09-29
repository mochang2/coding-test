"""
220929
url: https://programmers.co.kr/learn/courses/30/lessons/64062
후기: 효율성 통과가 너무 안 됐다.
결국 답을 보고 다.
마지막 코드를 제외하고 아래 모든 코드는 정확성은 통과했으나 효율성에서 실패했다.

첫 번째 시도는 슬라이딩 윈도우 방식으로 해서 매번 stones[left:right]의 max 값을 구한 뒤 answer와 비교했다.
당연히 시간 초과로 실패했다.
"""

# 두 번째 시도
# 시간 초과 실패
# 세그먼트 트리
# 세그먼트 트리는 query에 대해 O(log n + k)의 시간 복잡도
# k = 100,000이고 len(stones) == 200,000 이면 O(100,000^2)의 시간 복잡도를 가짐

def merge(left_value, right_value):
    return max(left_value, right_value)

def makeSegment(segment, original_list, node, left_range, right_range):
    if left_range == right_range:
        segment[node] = original_list[left_range]
        return segment[node]
    
    mid = left_range + (right_range - left_range) // 2
    left_value = makeSegment(segment, original_list, node * 2, left_range, mid)
    right_value = makeSegment(segment, original_list, node * 2 + 1, mid + 1, right_range)
    
    segment[node] = merge(left_value, right_value)
    
    return segment[node]

def getSegment(segment, query_left, query_right, node, left_range, right_range):
    if query_left > right_range or query_right < left_range:
        return 0
    
    if query_left <= left_range and right_range <= query_right:
        return segment[node]
    
    mid = left_range + (right_range - left_range) // 2
    left_value = getSegment(segment, query_left, query_right, node * 2, left_range, mid)
    right_value = getSegment(segment, query_left, query_right, node * 2 + 1, mid + 1, right_range)
    
    return merge(left_value, right_value)

def solution(stones, k):
    answer = 10 ** 9
    n = len(stones)
    segment = [0 for _ in range(4 * n)]
    makeSegment(segment, stones, 1, 0, n - 1)
    
    for index in range(len(stones) - k + 1):
        left = index
        right = index + k - 1
        max_count_at_current_range = getSegment(segment, left, right, 1, 0, n - 1)
        answer = min(answer, max_count_at_current_range)
    
    return answer



# 세 번째 시도
# 파라메트릭 서치
# 이거는 아직도 왜 시간 초과가 나는지 모르겠음
# twoPointer 함수가 O(n)인 것 같은데 사실은 아닌건가 싶음

def twoPointer(stones, friends, k):
    left = 0
    right = 0
        
    while left < len(stones):
        while right < len(stones) and stones[right] < friends: # 해당 인원이 넘어갈 수 있는 최대 거리를 구함
            right += 1

        if right - left + 1 > k: # 해당 인원이 넘어갈 수 없음
            return False
        
        left = right
        while left < len(stones) and stones[left] >= friends: # 다음 시작점을 구함
            left += 1
        
        right = left
        
    return True

def solution(stones, k):
    answer = 0
    min_ = 1
    max_ = 200000000
    
    #파라메트릭 서치
    while min_ <= max_:
        friends = (min_ + max_) // 2 # min_ + (max_ - min_) // 2 를 사용하면 시간 초과가 1개 더 났다
        can_jump = twoPointer(stones, friends, k)
        
        if can_jump:
            answer = max(answer, friends)
            min_ = friends + 1
        else:
            max_ = friends - 1
    
    return answer
  

  
# 네 번째 시도
# 정답
# 이분탐색
# 세 번째 시도에서 투포인터로 구한 것을 stone_count 하나의 변수로 해결

def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000
    
    while left <= right:
        mid = (left + right) // 2
        
        stone_count = 0 # mid의 인원으로 건널 때 한 번에 점프해야 하는 길이
        for stone in stones:
            if stone < mid:
                stone_count += 1
            else:
                stone_count = 0
            
            if stone_count == k:
                break
                
        if stone_count == k:
            right = mid - 1
        else:
            answer = max(answer, mid)
            left = mid + 1
        
    return answer
  
