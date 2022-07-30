"""
20220730
골드4 스도쿠
url: https://www.acmicpc.net/problem/2580
후기: 처음에는 모든 스도쿠가 채워야 하는 칸을 기준으로 가로 9개, 세로 9개, 3x3 정사각형을 확인했을 때
1개만 가능한 위치부터 채워나가면 해결되는 줄 알았다.
그런데 극단적으로 모든 위치가 0인 스도쿠도 들어올 수 있다고 한다(이론상 채울 수 있으니까...).
그래서 문제를 확인해보니 백트래킹이었다.

possible positions를 구하는데 시간 초과가 많이 나서 답을 봤는데 set이 아니라 list를 썼어야 됐다.

그리고 python은 아니지만 c++ 사용자 중에서 sdoku를 전역변수로 사용하지 않고 계속 함수에 넘겨줬다가 시간 초과가 난 사람도 있다고 해서 전역변수로 바꿔줬고,
백트래킹 도중 스도쿠를 완성하면 return하지 않고 sys.exit을 사용하게끔 바꿨는데, 그닥 상관은 없었던 부분인 것 같다.
"""

# 시간 초과
import sys

input_ = sys.stdin.readline
LENGTH = 9

def printMatrix(matrix):
    for i in range(LENGTH):
        for j in range(LENGTH):
            print(matrix[i][j], end=" ")
        print()

def getNumberPositions(matrix, number):
    positions = []
    
    for i in range(LENGTH):
        for j in range(LENGTH):
            if matrix[i][j] == number:
                positions.append((i, j))

    return positions

def getPossibleSet():
    return set([i for i in range(1, LENGTH + 1)])

def getRegions(zero_y, zero_x):
    global sdoku
    
    possibles = getPossibleSet()
    
    divisor = LENGTH // 3
    y, x = (zero_y // divisor) * divisor, (zero_x // divisor) * divisor
    for i in range(y, y + divisor):
        for j in range(x, x + divisor):
            if sdoku[i][j] != 0:
                possibles.remove(sdoku[i][j])

    return possibles

def getAxises(zero_y, zero_x):
    global sdoku
    
    possibles_y = getPossibleSet()
    possibles_x = getPossibleSet()
    
    for axis in range(LENGTH):
        if sdoku[axis][zero_x] != 0:
            possibles_y.remove(sdoku[axis][zero_x])

    for axis in range(LENGTH):
        if sdoku[zero_y][axis] != 0:
            possibles_x.remove(sdoku[zero_y][axis])
    
    return possibles_y.intersection(possibles_x)

def backTrack(zero_positions, index):
    global sdoku
    
    if (index == len(zero_positions)):
        return True

    y, x = zero_positions[index]
    axises = getAxises(y, x)
    regions = getRegions(y, x)

    for number in axises.intersection(regions):
        sdoku[y][x] = number
        if backTrack(zero_positions, index + 1):
            return True
        sdoku[y][x] = 0
        
    return False

# initialization
sdoku = [list(map(int, input_().strip().split())) for _ in range(LENGTH)]
zero_positions = getNumberPositions(sdoku, 0)
backTrack(zero_positions, 0)

# print
printMatrix(sdoku)



# 정답
import sys

input_ = sys.stdin.readline
LENGTH = 9

def printMatrix(matrix):
    for i in range(LENGTH):
        for j in range(LENGTH):
            print(matrix[i][j], end=" ")
        print()

def getNumberPositions(matrix, number):
    positions = []
    
    for i in range(LENGTH):
        for j in range(LENGTH):
            if matrix[i][j] == number:
                positions.append((i, j))

    return positions

def getCandidates(zero_y, zero_x):
    global sdoku
    
    numbers = [i + 1 for i in range(LENGTH)]
    divisor = LENGTH // 3

    for y in range(LENGTH):
        if sdoku[y][zero_x] in numbers:
            numbers.remove(sdoku[y][zero_x])

    for x in range(LENGTH):
        if sdoku[zero_y][x] in numbers:
            numbers.remove(sdoku[zero_y][x])

    y, x = (zero_y // divisor) * divisor, (zero_x // divisor) * divisor
    for i in range(y, y + divisor):
        for j in range(x, x + divisor):
            if sdoku[i][j] in numbers:
                numbers.remove(sdoku[i][j])

    return numbers

def backTrack(zero_positions, index):
    global sdoku
    
    if (index == len(zero_positions)):
        printMatrix(sdoku)
        sys.exit(0)

    y, x = zero_positions[index]
    for number in getCandidates(y, x):
        sdoku[y][x] = number
        backTrack(zero_positions, index + 1)
        sdoku[y][x] = 0
        
# initialization
sdoku = [list(map(int, input_().strip().split())) for _ in range(LENGTH)]
zero_positions = getNumberPositions(sdoku, 0)
backTrack(zero_positions, 0)

