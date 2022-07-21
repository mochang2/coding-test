"""
20220721
골드5 동전
url: https://www.acmicpc.net/problem/2293
후기: n개의 동전을 (무한히 사용 가능) 사용해서 k원을 만드는 문제는 너무나도 대표적인 DP이다.
다만 이 문제는 메모리 제한이 4MB인데 O(n * k) = 1,000,000 이므로 2차원 배열로 dp를 선언하면 메모리 초과가 난다.
따라서 1차원 배열로 제자리에서 dp 연산을 해야 한다.

    0 1 2 3 4 5 6 7 8 9 10
1   1
2  1
5  1
로 초기화해서 시작( 단 이 문제는 메모리 초과 때문에 1차원 배열로 선언해야 함)

i 번째 동전을 추가로 사용해서 m원을 만들 수 있는 경우의 수
 = i - 1 번째 동전까지만 사용해서 m원을 만들 수 있는 경우의 수
     + i 번째 동전까지 사용해서 m - value_of_i원을 만들 수 있는 경우의 수
"""

# 메모리 초과로 실패
import sys

input_ = sys.stdin.readline

# initialzation
n, k = map(int, input_().strip().split()) # 동전의 종류, 만들어야 하는 값어치
coins = [int(input_().strip()) for _ in range(n)]
dp = [[0 for _ in range(k + 1)] for __ in range(n)]

for i in range(n):
    dp[i][0] = 1 # 동전을 하나도 안 사용하면 0원을 만들 수 있음

for  i in range(n):
    coin = coins[i]
    for j in range(k + 1): # 동전들을 사용해서 만든 가치
        dp[i][j] = dp[i - 1][j] + dp[i][j - coin]

# print
print(dp[-1][-1])


# 통과
import sys

input_ = sys.stdin.readline

# initialzation
n, k = map(int, input_().strip().split()) # 동전의 종류, 만들어야 하는 값어치
coins = [int(input_().strip()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1 # 동전을 하나도 사용하지 않으면 0원을 만들 수 있음

for  i in range(n):
    coin = coins[i]
    for j in range(coin, k + 1): # 동전들을 사용해서 만든 가치
        dp[j] += dp[j - coin]

# print
print(dp[-1])
