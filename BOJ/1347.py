"""
실버4 미로 만들기
url: https://www.acmicpc.net/problem/1347
후기: grid를 넉넉히 선언하지 않아서 index error가 났었다. 좀 더 넉넉히 선언할 걸 그랬다.
"""
length = int(input())
string = input()
grid = [["#" for _ in range(101)] for __ in range(101)]
y, x = 50, 50
grid[y][x] = "."
min_x, max_x, min_y, max_y = 50, 50, 50, 50
direction = 2  # 0: 위, 1: 오른, 2: 아래, 3: 왼

for s in string:
    if s == "R":  # 오른쪽으로 방향 전환
        direction = (direction + 1) % 4
    elif s == "L":  # 왼쪽으로 방향 전환
        direction = (direction - 1) % 4
    else:  # s == "F":
        if direction == 0:
            y -= 1
            min_y = min(y, min_y)
        elif direction == 1:
            x += 1
            max_x = max(x, max_x)
        elif direction == 2:
            y += 1
            max_y = max(y, max_y)
        else:  # direction == 3:
            x -= 1
            min_x = min(x, min_x)
        grid[y][x] = "."

for i in range(min_y, max_y + 1):
    for j in range(min_x, max_x + 1):
        print(grid[i][j], end="")
    print()
