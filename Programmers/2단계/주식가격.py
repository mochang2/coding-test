"""
211213
스택 / 큐
url: https://programmers.co.kr/learn/courses/30/lessons/42584
후기: 효율성에서 통과 못 할까봐 걱정했는데 break 덕분에 상관이 없었나보다.
"""

def solution(prices):
  # prices의 각 가격은 1이상이랬으므로 제일 마지막에 0 추가
  prices.append(0)
  answer = []
  for i in range(len(prices)):
    price = prices[i]
    for j in range(i + 1, len(prices)):
      if price > prices[j]:
        # 0을 만났을 때와 만나지 않았을 때 개수 세는 것을 구분
        if prices[j] == 0:
          answer.append(j - i - 1)
        else:
          answer.append(j - i)
        break
        
  return answer