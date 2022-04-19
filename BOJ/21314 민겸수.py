"""
211225
실버1 민겸 수
url: https://www.acmicpc.net/problem/21314
후기: 그리디 문제라는데 이게 그리디 풀이법이 맞는지 모르겠다. 그냥 규칙 찾아서 문자열 잘 다루면 되는 것 같은데..
그리디 공부해야겠다. 마지막 max 처리하는 부분 때문에 많이 틀렸다.
"""

string = input()
max_ = ""
min_ = ""

# calc
Mcount = 0
for char in string:
    if char == "M":
        Mcount += 1
        
    else: # char == "K":
        # max_
        max_ += str(10 ** Mcount * 5)

        # min_
        if Mcount != 0:
            min_ += str(10 ** (Mcount - 1))
            Mcount = 0
        min_ += "5"
        
if string[-1] == "M":
    max_ += "1" * Mcount
if Mcount != 0:
    min_ += str(10 ** (Mcount - 1))


print(int(max_))
print(int(min_))
