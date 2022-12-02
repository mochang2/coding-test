"""
20221203
실버3 계단 오르기
url: https://www.acmicpc.net/problem/2579
후기: DP 문제였다.
이번에도 역시나 점화식을 떠올리지 못하겠어서 답을 봤다.

i-2, i-1, i번째 계단을 가지고 이리저리 굴려봤지만 답이 안 나왔다.
왜냐하면 i-3번째까지 고려해야 됐기 때문이다...


scores는 list로 index번째 계단까지 존재할 때 scores[index]는 해당 계단을 통해 얻을 수 있는 최대 점수를 말한다.
다음과 같은 순서로 푼다.

1. DP를 초기화한다.
   scores[0] = stairs[0]
   scores[1] = stairs[0] + stairs[1]
   scores[2] = max(stairs[0], stairs[1]) + stairs[2]
   
2. 점화식을 이용한다.
   scores[index]를 구할 때 이미 scores[index - 1]까지는 최선의 선택을 진행한 것이다.
   index - 3, index - 2, index - 1, index 번째 계단이 존재할 때, index 번째를 최대 높이라고 가정하므로 반드시 밟아야 한다.
   문제 조건에 따라 index - 3도 반드시 밟아야 하며, idnex - 2와 index - 1을 밟을지 말지 정해야 한다.
   둘 중 밟을 때 더 높은 점수를 얻는 계단을 밟는다.
   
3. 정답을 반환한다.
   scores[-1]이 정답이다.
"""

from sys import stdin

def initializeScores(number_of_stairs, stairs):
    scores = [0] * number_of_stairs

    for index in range(min(2, number_of_stairs)):
        scores[index] = sum(stairs[:index + 1])

    if number_of_stairs >= 3:
        scores[2] = max(stairs[0], stairs[1]) + stairs[2]

    return scores

def calculateBestScores(scores, stairs):
    for index in range(3, len(stairs)):
        score_stepping_on_last_stair = scores[index - 3] + stairs[index - 1] + stairs[index]
        score_stepping_on_second_last_stair = scores[index - 2] + stairs[index]

        scores[index] = max(score_stepping_on_last_stair, score_stepping_on_second_last_stair)
        

input_ = stdin.readline

number_of_stairs = int(input_().strip())
stairs = [int(input_().strip()) for _ in range(number_of_stairs)] # 각 계단의 점수
scores = initializeScores(number_of_stairs, stairs) # 각 index의 계단까지 갈 수 있다고 할 때 얻을 수 있는 최대 점수
calculateBestScores(scores, stairs)

# print
print(scores[-1])
