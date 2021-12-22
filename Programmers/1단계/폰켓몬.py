"""
211207
찾아라 프로그래밍 마에스터
url: https://programmers.co.kr/learn/courses/30/lessons/1845
후기: dictionary보다 더 좋은 set를 쓰니까 1줄 안에 끝낼 수 있었다.
"""

def solution(nums):
  # N / 2, 서로 다른 폰켓몬 종류의 수  중 더 작은 값이 가질 수 있는 서로 다른 폰켓몬 종류이 최대임.
  return min(len(nums) // 2, len(set(nums)))