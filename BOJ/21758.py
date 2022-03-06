"""
실버1 꿀 따기
url: https://www.acmicpc.net/problem/21758
후기: 벌통이 가장 왼쪽, 가장 오른쪽, 중간에 있을 세 가지 경우를 모두 계산해봐야 한다.
처음 제출했을 때는 N == 3일 때만 벌통이 중간에 있을 수 있다고 생각했지만
6
1 10000 3 6 12 1
out; 20021 (10000이 꿀. 벌들은 양끝에서 시작)
라는 반례가 존재했다.

그 다음 제출할 때는 honey_li의 max 값들이 벌통 위치 후보가 된다고 생각했다.
하지만 이것도 반례가 존재했다(반례가 무엇인지는 확인하지 못 했다).

결국 답을 봤고 부분합이라는 것을 알았다.
답을 본 후에도 부분합을 따로 저장해두지 않고 매번 sum(어떤 list) 값을 계산해서 55점밖에 나오지 않았다.
부분합 변수를 선언한 후에 100점을 맞을 수 있었다.
"""

## 1차 시도. N == 3일 때만 계산. 반례 때문에 실패
import sys

N = int(sys.stdin.readline().strip())
honey_li = list(map(int, sys.stdin.readline().strip().split()))
answer = 0

# 꿀통 위치를 두, 세 군데 놓아보고 최댓값을 찾는다.
# 후보 1. 가장 오른쪽
bee1 = 0
bee2 = 1
while bee2 < N - 1 and honey_li[bee2] > 2 * honey_li[bee2 + 1]:
    bee2 += 1
answer = max(answer, sum(honey_li[bee1 + 1:N]) + sum(honey_li[bee2 + 1:N]) - honey_li[bee2])

# 후보 2. 가장 왼쪽
bee1 = N - 1
bee2 = N - 2
while bee2 > 0 and honey_li[bee2] > 2 * honey_li[bee2 - 1]:
    bee2 -= 1
answer = max(answer, sum(honey_li[0:bee1]) + sum(honey_li[0:bee2])  - honey_li[bee2])

# 후보 3. 중간. N == 3일 때만
if N == 3:
    answer = max(answer, 2 * honey_li[1])

print(answer)


## 2차 시도. max 값이 꿀통 위치 후보라고 생각. 반례 때문에 실패
import sys

N = int(sys.stdin.readline().strip())
honey_li = list(map(int, sys.stdin.readline().strip().split()))
answer = 0

# 꿀통 위치를 두, 세 군데 놓아보고 최댓값을 찾는다.
# 후보 1. 가장 오른쪽
bee1 = 0
bee2 = 1
while bee2 < N - 1 and honey_li[bee2] > 2 * honey_li[bee2 + 1]:
    bee2 += 1
answer = max(answer, sum(honey_li[bee1 + 1:N]) + sum(honey_li[bee2 + 1:N]) - honey_li[bee2])

# 후보 2. 가장 왼쪽
bee1 = N - 1
bee2 = N - 2
while bee2 > 0 and honey_li[bee2] > 2 * honey_li[bee2 - 1]:
    bee2 -= 1
answer = max(answer, sum(honey_li[0:bee1]) + sum(honey_li[0:bee2])  - honey_li[bee2])

# 후보 3. 양끝이 아닐 때
max_ = max(honey_li)
for i in range(N):
    if i == 0 or i == N - 1 or honey_li[i] != max_:
        continue
    answer = max(answer, sum(honey_li[1:i + 1]) + sum(honey_li[i:N - 1]))

print(answer)


## 3차 시도. 비효율적인 코드: 55점(93, 99번째 줄)
import sys

N = int(sys.stdin.readline().strip())
honey_li = list(map(int, sys.stdin.readline().strip().split()))
sum_ = sum(honey_li)
answer = 0

# 꿀통 위치를 두, 세 군데 놓아보고 최댓값을 찾는다.
# 후보 1. 가장 오른쪽
bee1 = 0
tmp_sum = sum_ - honey_li[bee1]
for bee2 in range(1, N - 1):
    answer = max(answer, (tmp_sum - honey_li[bee2]) + (sum_ - sum(honey_li[:bee2 + 1])))

# 후보 2. 가장 왼쪽
bee1 = N - 1
tmp_sum = sum_ - honey_li[bee1]
for bee2 in range(1, N - 1):
    answer = max(answer, (tmp_sum - honey_li[bee2]) + (sum_ - sum(honey_li[bee2:])))

# 후보 3. 양끝이 아닐 때 => 벌은 각각 양 끝
tmp_sum = sum_ - honey_li[0] - honey_li[N - 1]
for pot in range(1, N - 1):
    answer = max(answer, tmp_sum + honey_li[pot])

print(answer)


## 4차 시도. 100점
import sys

N = int(sys.stdin.readline().strip())
honey_li = list(map(int, sys.stdin.readline().strip().split()))
sums = [0 for _ in range(N)] # 부분합 저장
for i in range(N):
    sums[i] = sums[i - 1] + honey_li[i]
answer = 0

# 꿀통 위치 후보
# 후보 1. 가장 오른쪽 => 벌 하나는 무조건 가장 왼쪽
bee1 = 0
tmp_sum = sums[-1] - honey_li[bee1]
for bee2 in range(1, N - 1):
    answer = max(answer, (tmp_sum - honey_li[bee2]) + (sums[-1] - sums[bee2]))
    
# 후보 2. 가장 왼쪽 => 벌 하나는 무조건 가장 오른쪽
bee1 = N - 1
tmp_sum = sums[-1] - honey_li[bee1]
for bee2 in range(1, N - 1):
    answer = max(answer, (tmp_sum - honey_li[bee2]) + (sums[bee2 - 1]))

# 후보 3. 양끝이 아닐 때 => 벌은 무조건 각각 양 끝
tmp_sum = sums[-1] - honey_li[0] - honey_li[N - 1]
for pot in range(1, N - 1):
    answer = max(answer, tmp_sum + honey_li[pot])

print(answer)
