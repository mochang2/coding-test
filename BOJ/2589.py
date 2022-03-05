"""
골드5 보물섬
url: https://www.acmicpc.net/problem/2589
후기: 약간 변형된 bfs + brute force 문제였다. python으로는 시간 초과가 나서 pypy로 풀었다.
처음 위치를 Visited = True로 바꿔주지 않아서 첫 제출에서 틀렸었다.
"""

import sys

def InitVisited():
    global visited, H, W
    for i in range(H):
        for j in range(W):
            if visited[i][j] == True:
                visited[i][j] = False

def Bfs(pos_li):
    global dy, dx, visited, H, W, treasure_map
    next_pos_li = []
    for pos in pos_li:
        for direction in range(4):
            new_y = pos[0] + dy[direction]
            new_x = pos[1] + dx[direction]
            if not 0 <= new_y < H or not 0 <= new_x < W:
                continue
            if treasure_map[new_y][new_x] == "L" and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                next_pos_li.append([new_y, new_x])
                
    return next_pos_li

def CalcFarestLand(pos_li):
    res = 0
    while len(pos_li) != 0:
        pos_li = Bfs(pos_li)
        res += 1
        
    return res

# 초기화
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0
treasure_map = []
start_pos = []

H, W = map(int, sys.stdin.readline().strip().split())
visited = [[False for _ in range(W)] for __ in range(H)]
for i in range(H):
    treasure_map.append(input())
for i in range(H):
    for j in range(W):
        if treasure_map[i][j] == "L":
            start_pos.append((i, j))

# BFS
# 모든 L을 시작점으로 삼아 BFS를 돌고, 그 중 거리가 가장 먼 곳을 가는 시간을 구함
# BFS를 한 번 돌면 1시간 동안 최단 거리로 갈 수 있는 모든 위치를 찾는 것이고,
# BFS를 두 번 돌면 2시간 동안 최단 거리로 갈 수 있는 모든 위치를 찾는 것...
for pos in start_pos:
    visited[pos[0]][pos[1]] = True
    res = CalcFarestLand([pos])
    answer = max(answer, res)
    InitVisited()

print(answer - 1)
