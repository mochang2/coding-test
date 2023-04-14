"""
20230317
실버2 두 직선의 교차 여부
url: https://www.acmicpc.net/problem/6487
후기: 거의 처음 풀어보는 기하학 문제다.
특별한 알고리즘이 필요하기보다는 노가다성 문제다.
조금 풀이가 깔끔하지 않아 아쉽다.

vertical인 함수는 division by zero 에러가 나므로 vertical 여부를 판단해야 한다.
둘다 vertical이면 같은 직선이거나 평행한 직선이다.
하나만 vertical이면 한 점에서 만난다.
둘다 vertical이 아니라면 기울기가 같은지 판단해 평행인지, 일치인지 확인하다.
앞에 모든 조건에 걸리지 않은 점들이라면 한 점에서 만난다.
"""

from sys import stdin

class Line:
    def __init__(self):
        self.a = 0
        self.b = 0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def isVertical(x1, x2):
    return x1 == x2

def calculateInclination(p1, p2):
    return (p1.y - p2.y) / (p1.x - p2.x)

def calculateYIntercept(p, inclination):
    return p.y - p.x * inclination

def isSameLine(l1, l2):
    return l1.a == l2.a and l1.b == l2.b

def isParallel(l1, l2):
    return l1.a == l2.a and l1.b != l2.b

for _ in range(int(stdin.readline().strip())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, stdin.readline().strip().split())

    if isVertical(x1, x2) and isVertical(x3, x4):
        if x1 == x3:
            print("LINE")
        else:
            print("NONE")
        continue
    
    elif isVertical(x1, x2) or isVertical(x3, x4):
        if isVertical(x1, x2):
            x1, x2, x3, x4 = x3, x4, x1, x2
            y1, y2, y3, y4 = y3, y4, y1, y2

        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        
        line = Line()
        line.a = calculateInclination(p1, p2)
        line.b = calculateYIntercept(p1, line.a)

        print("POINT {:.2f} {:.2f}".format(x3, x4 * line.a + line.b))

        continue

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)

    line1 = Line()
    line1.a = calculateInclination(p1, p2)
    line1.b = calculateYIntercept(p1, line1.a)
    line2 = Line()
    line2.a = calculateInclination(p3, p4)
    line2.b = calculateYIntercept(p3, line2.a)

    if isSameLine(line1, line2):
        print("LINE")
        continue
    elif isParallel(line1, line2):
        print("NONE")
        continue

    intersect_x = (line2.b - line1.b) / (line1.a - line2.a)

    print("POINT {:.2f} {:.2f}".format(intersect_x, intersect_x * line1.a + line1.b))
    
