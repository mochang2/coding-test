"""
20220412
골드2 가장 긴 증가하는 부분 수열 2
url: https://www.acmicpc.net/problem/12015
후기: LIS를 N log N에 푸는 방법. 11055번을 풀고 바로 이어서 풀었다.
for문으로 li를 순회할 때 dp의 몇 번째에 각각의 인자들이 들어갔는지 별도의 list에 저장하면
해당 list를 역순으로 순회함으로써 LIS의 길이뿐만 아니라 수열도 알 수 있다.
다 풀고 나서 lower bound 찾는 알고리즘을 살펴보니 초기 left, right index 값 설정을 잘못해주었다.
그래서 코드가 좀 지저분하다.
이참에 같이 짚어가야겠다.

알고리즘 참고: https://rebro.kr/33
반례: https://www.acmicpc.net/board/view/32030
binary search로 lower / upper bound 찾는 알고리즘: https://jackpot53.tistory.com/33

leetcode 334, boj 11055 참고
"""

import sys
input_ = sys.stdin.readline

N = int(input_())
li = list(map(int, input_().strip().split()))
dp = [li[0]]

for i in range(1, N):
    if li[i] > dp[-1]:
        dp.append(li[i])
    else:
        # binary search로 lower boundary를 찾음
        left = 0
        right = len(dp) - 1
        while left <= right:
            mid = (left + right) // 2
            if dp[mid] > li[i]:
                right = mid - 1
            elif dp[mid] < li[i]:
                left = mid + 1
            else:
                break
        if dp[mid] >= li[i]:
            dp[mid] = li[i]
        else:
            dp[mid + 1] = li[i] # 인덱스 유효성 검사할 필요가 없음
print(len(dp))
