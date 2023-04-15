"""
20230415
골드3 소풍
url: https://www.acmicpc.net/problem/2026
후기: 백트래킹 문제다.
백트래킹 문제답게 역시 재귀 중단 조건이 가장 큰 문제의 핵심이었다.
첫 번째는 친구들을 무조건 작은 숫자부터 순회해야 한다.
두 번째는 친구인지 한 번 확인한 친구는 다시 확인하지 않아야 한다.
in_friends(visited 처럼 선언)을 사용하지 않아 계속 실패했고 결국 답을 봤다.

문제는 다음과 같은 순서로 풀었다.
1. 친구 관계를 정의한다. 본인은 본인을 친구라고 인식한다.
2. 모든 학생을 시작점(n)으로 반복문을 돈다.
3. 현재까지 친구인 애들을 friends라는 list에 넣고, 현재 선택된 학생(student)이 friends에 있는 모든 애들과 친구인지 확인한다.
   (처음에는 set으로 썼었다고 바꿨는데 사실 이 문제에서는 크게 중요한 부분인 거 같지 않다)
4. 친구가 아니라면 재귀를 종료한다.
5. 친구라면 friends에 소풍 보낼 친구의 수가 될 때까지 새로운 학생을 찾는다.
6. 재귀를 돌면서 한 번 확인한 친구는 다시는 확인하지 않는다.
   (이 문제의 핵심이다)
   만약 1,2번이 친구 관계(friends)이고, 3번이 친구인지 확인했는데 아니었다고 하자.
   그렇다면 이후에 1,2,4번이 friends일 때 다시 3번 친구는 확인하지 않아도 된다는 뜻이다. 
7. n을 시작점으로 소풍 보낼 친구를 찾지 못했으면 n + 1 친구를 시작점으로 2번부터 반복한다.
"""

from sys import stdin, exit as exit_

def initializeRelations():
    friend_lists = [[student] for student in range(total_students_count)]
    is_friend = [[False for _ in range(total_students_count)] for __ in range(total_students_count)]

    for student in range(total_students_count):
        is_friend[student][student] = True

    for _ in range(number_of_relations):
        student1, student2 = map(lambda student: int(student) - 1, stdin.readline().strip().split())
        
        friend_lists[student1].append(student2)
        friend_lists[student2].append(student1)

        is_friend[student1][student2] = True
        is_friend[student2][student1] = True

    return list(map(lambda students: sorted(students), friend_lists)), is_friend

def findEveryIsFriendRelationship(student, friends):
    is_friend_with_friends = all(is_friend[student][friend] for friend in friends)
    if not is_friend_with_friends:
        return
    
    if len(friends) == picnic_students_count:
        for friend in sorted(friends):
            print(friend + 1)
        exit_(0)

    for friend in friend_lists[student]:
        if in_friends[friend]:
            continue

        friends.append(friend)
        in_friends[friend] = True
        
        findEveryIsFriendRelationship(friend, friends)
        
        friends.pop()
        # in_friends[friend] = False # 이 부분을 빼지 않으면 시간 초과 

picnic_students_count, total_students_count, number_of_relations = map(int, stdin.readline().strip().split())
friend_lists, is_friend = initializeRelations()
for student in range(total_students_count):
    in_friends = [False for _ in range(total_students_count)]
    in_friends[student] = True
    
    findEveryIsFriendRelationship(student, [student])

print(-1)
