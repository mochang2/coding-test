"""
211104
골드5 도서관
url: https://www.acmicpc.net/problem/1461
후기: 여러 경우의 수를 생각해보니 어찌 됐다. 크리티컬한 알고리즘이 존재하진 않았다.

<4가지 경우의 수>
1. +-좌표로 이루어졌는데 가장 먼 좌표가 +좌표인 경우
2. +좌표로만 이루어진 경우(가장 먼 좌표가 +)
3. +-좌표로 이루어졌는데 가장 먼 좌표가 -좌표인 경우
4. -좌표로만 이루어진 경우(가장 먼 좌표가 -)
"""
import sys
n, m = map(int, sys.stdin.readline().strip().split())
book_place_li = sorted(list(map(int, input().split())))
res = 0
#print(book_place_li)

if abs(book_place_li[0]) <= abs(book_place_li[-1]): # 제일 먼 책이 +좌표에 위치할 때
    if book_place_li[0] < 0: # 경우 1
        index = 0 # -좌표 책들부터 정리
        count = 1 # 한 번에 들고간 책의 수
        while book_place_li[index] < 0:  # -좌표 합
            if count == 1:
                res += abs(book_place_li[index]) * 2
            count += 1
            if count == m + 1:
                count = 1
            index += 1

        index = n - 1
        count = 1
        while book_place_li[index] > 0 : # +좌표 합
            if count == 1:
                if index == n - 1:  # 가장 먼 길은 다시 돌아오지 않아도 되므로 *2를 안 해줌
                    res += book_place_li[index]
                else:
                    res += book_place_li[index] * 2
            count += 1
            if count == m + 1:
                count = 1
            index -= 1


    else: # 경우 2
        index = n - 1
        count = 1
        while index >= 0:
            if count == 1:
                if index == n - 1:
                    res += book_place_li[index]
                else:
                    res += book_place_li[index] * 2
            count += 1
            if count == m + 1:
                count = 1
            index -= 1


else: # 제일 먼 책이 -좌표에 위치할 때
    if book_place_li[-1] > 0: # 경우 3
        index = 0 # -좌표 책들부터 정리
        count = 1 # 한 번에 들고간 책의 수
        while book_place_li[index] < 0:
            if count == 1:
                if index == 0:
                    res += abs(book_place_li[index])
                else:
                    res += abs(book_place_li[index]) * 2
            count += 1
            if count == m + 1:
                count = 1
            index += 1

        index = n - 1
        count = 1
        while book_place_li[index] > 0 :
            if count == 1:
                res += book_place_li[index] * 2
            count += 1
            if count == m + 1:
                count = 1
            index -= 1


    else: # 경우 4
        index = 0
        count = 1
        while index <= n - 1:
            if count == 1:
                if index == 0:
                    res += abs(book_place_li[index])
                else:
                    res += abs(book_place_li[index]) * 2
            count += 1
            if count == m + 1:
                count = 1
            index += 1


print(res)
