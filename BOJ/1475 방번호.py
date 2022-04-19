"""
211029
실버5 방 번호
url: https://www.acmicpc.net/problem/1475
후기: 문자열 다루기를 잘 하면 된다. 파이썬이 그래서 좋은 듯
"""
import sys   # input 받기 위해
import math  # 올림(ceil) 함수 사용을 위해

def main(n_str):
    li = [0] * 10  # len == 10인 배열 초기화
    for s in n_str:
        if s == "6" or s == "9":
            li[6] += 0.5
            li[9] += 0.5
        else:
            li[int(s)] += 1
            
    res = 0
    for i in li:
        res = max(math.ceil(i), res)

    return res

    
if __name__ == "__main__":
    n_str = sys.stdin.readline().strip()
    print(main(n_str))
