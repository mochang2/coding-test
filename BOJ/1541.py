"""
211208
실버2 잃어버린 괄호
url: https://www.acmicpc.net/problem/1541
후기: 그리디라는데 그리디로 푼건 아닌 거 같다. 그냥 문자열 파싱으로 풀었다.
문자열에서는 파이썬이 진짜 최고인 것 같다. 더할 수 있는 수 모두 더한 뒤 빼면 최솟값이라 생각하고 푸니 풀렸다.
"""

expressions = input().split("-")  # - 기호를 기준으로 split

for index, expression in enumerate(expressions):
  # expressions 원소를 모두 더함
  tmp_split = list(map(int, expression.split("+")))
  expressions[index] = sum(tmp_split)

# input의 시작값은 무조건 숫자랬으니 res 초기화
res = int(expressions[0])
for num in expressions[1:]:
  res -= num
print(res)