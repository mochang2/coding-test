"""
골드1 뉴스 전하기
211031
url: https://www.acmicpc.net/problem/1135
후기: 한참 실력에 못 미치는 tree DP였다. 나중에 다시 풀어야 된다.
"""

# 실패한 시도
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    input_li = sorted(list(map(int, sys.stdin.readline().split())))
    
    dic = dict()                               # hash 처럼 이용하기 위해, 부모 - 자식 간의 관계 명시
    num_of_descendents = [0] * n  # 자식의 개수
    result = [0] * n                         # 결과
    
    for i, value in enumerate(input_li): # dic, num_of_descendents 할당
        dic[i] = value
        num_of_descendents[value] += 1
    num_of_descendents[-1] -= 1

    for i in range(1, n):  # height 할당
        cnt = 0
        tmp = i
        while dic[tmp] != -1:
            cnt += 1
            tmp = dic[tmp]
        result[i] = cnt

    for i in range(0, n):   # answer
        tmp = i
        while dic[tmp] != -1:
            result[i] += (num_of_descendents[dic[tmp]] - 1)   # 본인은 제외한 형제의 수만큼 더해줌
            tmp = dic[tmp]

    print(dic)
    print(num_of_descendents)
    print(result)


# 모범답안
n = int(input())
t = list(map(int, input().split()))
tree = [[] for _ in range(n)]

for idx in range(1, n):  #위에서 아래로 내려오는 트리 구조. 부모가 index 자식이 배열 안의 원소들
    tree[t[idx]].append(idx)
print("tree:", tree)
#time[v] = v를 root로 하는 subtree에 정보를 모두 전달하는데 걸리는 시간
time = [0]*n

def dp(v):
    print("dfs 시작 " + str(v) + "번째 노드로 들어갑니다.")
    child_t = []
    for nei in tree[v]:
        dp(nei)
        #각 child를 root로 하는 subtree에 정보 전달하는데 걸리는 시간 모음
        child_t.append(time[nei])
    if not tree[v]:
        #Child가 없으면 0
        child_t.append(0)

    child_t.sort(reverse=True)  #시간이 오래 걸리는 쪽부터 먼저 전화를 돌리기
    need_time = [child_t[i]+i+1 for i in range(len(child_t))]   # i + 1은 형제들을 고려하여 추가하는 수
    
    print("v:", v)
    print("child_t:", child_t)
    print("need_time:", need_time)
    time[v] = max(need_time) #그 중에 가장 오래 걸리는 시간을 assign
    print("time[v]:", time[v])
    print()
    
dp(0)
print(time[0]-1) #Root node에 정보 전달하는 시간은 없으니 1빼기
