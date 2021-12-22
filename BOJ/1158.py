"""
211206
실버5 요세푸스 문제
url: https://www.acmicpc.net/problem/1158
후기
첫 번째 시도: print 출력 형식 잘못됨.
두 번째 시도: 시간 초과(매번 len(li)를 세지 않고 출력할 때마다 N을 1씩 감소시킴)
세 번째 시도: 시간 초과(visited라는 변수를 추가. 기존 li에서 pop을 쓰지 않고 출력하고자 함)
네 번째 시도: 시간 초과(deque을 썼는데도 rotate 때문인지 시간초과)
다섯 번재 시도: 성공. 어이가 없다. 자료 구조 문제는 아닌 것 같다. pointer에 차례로 1씩 더 하면 안 됐다.
"""

# 첫 번째 시도
import sys
N, K = map(int, sys.stdin.readline().strip().split())
count = 1
pointer = 0
li = [i + 1 for i in range(N)]

print("<", end="")
while len(li) != 1:
    if count == K:
        print(li.pop(pointer), ",", end=" ")
        count = 1
    pointer = (pointer + 1) % len(li)
    count += 1
print(str(li[0]) + ">")


# 두 번째 시도
import sys
N, K = map(int, sys.stdin.readline().strip().split())
count = 1
pointer = 0
li = [i + 1 for i in range(N)]

print("<", end="")
while N != 1:
    if count == K:
        print(li.pop(pointer), end=", ")
        count = 1
        N -= 1
    pointer = (pointer + 1) % N
    count += 1
print(str(li[0]) + ">")


# 세 번째 시도
import sys
N, K = map(int, sys.stdin.readline().strip().split())
count = 1        # K까지 몇 번 사람을 셌는지.
pointer = 0     # li에서 현재 가리키고 있는 index.
res_count = 0  # 여태껏 총 출력한 개수. <> 출력해야 돼서 개수를 셈.
li = [i + 1 for i in range(N)]
visited = [False for _ in range(N)]

print("<", end="")
while res_count != N - 1:
    if count == K:
        print(li[pointer], end=", ")
        visited[pointer] = True
        count = 0
        res_count += 1
    pointer = (pointer + 1) % N
    if not visited[pointer]:
        count += 1
for i in range(N):
    if not visited[i]:
        print(str(li[i]) + ">")
        break

        
# 네 번째 시도
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
count = 1
pointer = 0
linked_list = deque([i + 1 for i in range(N)])

print("<", end="")
while N != 1:
    if count == K:
        print(linked_list.popleft(), end=", ")
        count = 1
        N -= 1
    linked_list.rotate(-1)
    count += 1
print(str(linked_list[0]) + ">")


# 다섯 번째 시도
import sys
N, K = map(int, sys.stdin.readline().strip().split())
pointer = 0
li = [i + 1 for i in range(N)]

print("<", end="")
while N != 1:
    pointer = (pointer + K - 1) % N
    print(li.pop(pointer), end=", ")
    N -= 1
print(str(li[0]) + ">")
