"""
220815
골드3 텀 프로젝트
url: https://www.acmicpc.net/problem/9466
후기: dfs / bfs 문제였다. 처음에는 1) visited == True인 index를 만나는 경우, 2) 자기 자신을 투표한 경우, 3) loop가 있는 경우로
총 3가지 경우의 수가 있는 줄 알고 모두 다 커버해보려고 했는데

4
2 3 2 1

과 같이 꼬리가 달린(?) 루프 모양이 생기면 해결할 수가 없었다.

결국 답을 봤는데
https://leeiopd.tistory.com/entry/BOJ-9466-%ED%85%80-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC 와
https://tooo1.tistory.com/505 를 참고해서
지나간 길에 있는 모든 애들을 list에 담고 vistied == True은 index를 만났을 경우 루프가 생기는지 확인하는 방법이었다.

테스트 케이스로는 다음을 넣어보면 웬만한 엣지 케이스를 잡을 수 있다.

5
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
8
2 3 4 5 6 7 8 1
4
2 3 2 1
4
2 3 4 2
"""

import sys

input_ = sys.stdin.readline

def getInput(x):
    return int(x) - 1

T = int(input_().strip()) # 테스트 케이스 개수
for _ in range(T):
    answer = 0
    n = int(input_().strip())
    wants = list(map(getInput, input_().strip().split()))
    visited = [False for __ in range(n)]

    for index in range(n):
        if visited[index]:
            continue

        track = [] # index를 기준으로 지나간 애들을 보관할 track
        want = index
        while True:
            if visited[want]:
                break

            track.append(want)
            visited[want] = True
            want = wants[want]

        if want in track: # loop가 있었는지 
            answer += track.index(want)
        else:
            answer += len(track)
            
    # print
    print(answer)
    
