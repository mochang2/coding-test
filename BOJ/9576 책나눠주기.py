"""
20220715
골드2 책 나눠주기
url: https://www.acmicpc.net/problem/9576
후기: 그리디 문제이다. 대부분의 그리디가 그렇듯 일단 책을 원하는 학생에게 배정해주고 보는 구조이니 정렬이 필요할 거라고 생각했다.
그래서 (원하는 책의 시작 번호, 원하는 책의 끝 번호) 순으로 정렬한 뒤 책의 번호가 낮은 것부터 무조건 학생에게 매칭해주면 될 거라고 생각했다.
하지만 

1
7 4
1 7
1 7
1 7
2 2

과 같은 반례가 있어서 처음에는 틀렸고, (원하는 책의 끝 번호)만을 오름차순으로 정렬하니 두 번째 제출에서는 맞았다.

추가로 이분 매칭이라는 알고리즘으로도 풀 수 있는 문제라고 한다.
이분매칭: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ndb796&logNo=221240613074
킹갓 

(참고 추가 예시)
1
8 5
4 5
4 5
5 8
3 4
2 3

1
6 6
1 5
1 2
2 3
3 4
4 5
5 6
"""

# 실패
# 오름차순 정렬. 그리디
# 가능한 가장 작은 수의 번호 책을 부여
import sys

input_ = sys.stdin.readline

T = int(input_().strip())
for _ in range(T):
    # initialization
    answer = 0
    N, M = map(int, input_().strip().split())
    books = [False for __ in range(N + 1)] # 책이 대여됐는지 여부
    students = [tuple(map(int, input_().strip().split())) for __ in  range(M)]
    
    students.sort() # 오름차순 정렬

    for start, end in students:
        for book_number in range(start, end + 1):
            if not books[book_number]:
                books[book_number] = True
                answer += 1
                break

    print(answer)


# 성공
# end를 기준으로 오름차순, start는 상관없음
# 가능한 가장 작은 수의 번호 책을 부여
import sys

input_ = sys.stdin.readline

T = int(input_().strip())
for _ in range(T):
    # initialization
    answer = 0
    N, M = map(int, input_().strip().split())
    books = [False for __ in range(N + 1)] # 책이 대여됐는지 여부
    students = [tuple(map(int, input_().strip().split())) for __ in  range(M)]
    
    students.sort(key=lambda x:(x[1])) 

    for start, end in students:
        for book_number in range(start, end + 1):
            if not books[book_number]:
                books[book_number] = True
                answer += 1
                break

    print(answer)


# 이분매칭
# O(간선^2 * 정점) = 1,000^3 이므로 시간초과할 줄 알았으나.. 테스트 케이스가 빈약한지 통과
import sys

sys.setrecursionlimit(1000 ** 3)
input_ = sys.stdin.readline

def dfs(index: int) -> bool: # input: student index, output: 매칭됐는지 여부
    global students, books, matchings
    
    start, end = students[index][0], students[index][1]
    for book_num in range(start- 1, end):
        if books[book_num]: # 이미 소유권이 있음이 인정된 book
            continue

        books[book_num] = True
        if matchings[book_num] == -1 or dfs(matchings[book_num]): # 기존에 매칭되지 않은 book이거나 앞에 매칭됐던 학생이 새롭게 매칭이 가능한 책이 존재한다면
            matchings[book_num] = index
            return True
        
    return False

T = int(input_().strip())
for _ in range(T):
    # initialization
    answer = 0
    N, M = map(int, input_().strip().split())
    students = [tuple(map(int, input_().strip().split())) for __ in  range(M)] 
    matchings = [-1 for _ in range(N)] # 책이 몇 번째 학생에게 골랐졌는지를 저장하는 정보

    for index in range(len(students)):
        books = [False for __ in range(N)] # 책이 대여됐는지 여부
        if dfs(index):
            answer += 1
            
    print(answer)

