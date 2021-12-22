"""
211119
정렬
url: https://programmers.co.kr/learn/courses/30/lessons/42746
후기: 풀이 보고 얼탱이가 없었다. 포기

참고할 테스트 케이스
[500, 11, 12, 13] "500131211"
[2, 20, 220] "222020"
[6, 646] "6646"
[0, 0, 0, 0] "0"
[0, 0, 70] "7000"
[2357, 235785] "2357852357"
[3, 30, 31, 33] "3333130"
[343, 34] "34343"
"""

# 첫 시도와 반례
def solution(numbers):
    res = ""
    chars_li = [[] for _ in range(10)]
    for i in numbers: # O(n). 제일 높은 자리 수를 기준으로 나눔
        s = str(i)
        index = 0
        while len(s) < 4:
            index += 1
            s += s[0]
        chars_li[int(s[0])].append((s, index))
    
    for chars in chars_li[::-1]: # O(n * log n)
        chars.sort()
        print(chars)
        for char in chars[::-1]:
            print(char)
            res += char[0][0:4 - char[1]]
            
    return res
print(solution([343,34]))


# 두 번째 시도와 반례
def solution(numbers):
    res = ""
    div_by_first_digit = [[[] for _ in range(3)] for __ in range(10)]
    for i in numbers:
        if i == 0 or i == 1000:
            div_by_first_digit[0][0].append(str(i))
        else:
            s = str(i)
            if len(s) == 1:
                div_by_first_digit[int(s[0])][1].append(s)
            elif s[1] < s[0]:
                div_by_first_digit[int(s[0])][0].append(s)
            else:
                div_by_first_digit[int(s[0])][2].append(s)

    for div_by_second_digit in div_by_first_digit[::-1]:
        for chars in div_by_second_digit[::-1]:
            print(chars)
            chars.sort()
            for char in chars[::-1]:
                res += char

    return res
	
print(solution([2,20,220]))
print(solution([343,34]))


# 세 번째 시도와 반례
def solution(numbers):
    res = ""
    comparison = [["11","111"],["22","222"],["33","333"],["44","444"],["55","555"],["66","666"],["77","777"],["88","888"],["99","999"]]
    div_by_first_digit = [[[] for _ in range(3)] for __ in range(10)]
    for i in numbers:
        if i == 0 or i == 1000:
            div_by_first_digit[0][0].append(str(i))
        else:
            s = str(i)
            first_digit = int(s[0])
            if len(s) == 1:
                div_by_first_digit[first_digit][1].append(s)
            elif len(s) == 2:
                if s < comparison[first_digit - 1][0]:
                    div_by_first_digit[first_digit][0].append(s)
                elif s > comparison[first_digit - 1][0]:
                    div_by_first_digit[first_digit][2].append(s)
                else: # ==
                    div_by_first_digit[first_digit][1].append(s)
            else: #len(s) == 3:
                if s < comparison[first_digit - 1][1]:
                    div_by_first_digit[first_digit][0].append(s)
                elif s > comparison[first_digit - 1][1]:
                    div_by_first_digit[first_digit][2].append(s)
                else: # ==
                    div_by_first_digit[first_digit][1].append(s)
    print(div_by_first_digit)
    for div_by_second_digit in div_by_first_digit[::-1]:
        for chars in div_by_second_digit[::-1]:
            chars.sort()
            print(chars)
            for char in chars[::-1]:
                res += char

    return res
print(solution([343,34]))


# 최종(답을 봄)
def solution(numbers):
    strings = []
    
    for i in numbers:
        strings.append(str(i))
    strings.sort(key=lambda x: (x*3), reverse=True)
    
    return str(int("".join(strings))) # 000 인 경우 0으로 출력해야 한다고 함..
