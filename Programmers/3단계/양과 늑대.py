"""
220528
2022 KAKAO BLIND RECRUITMENT
url: https://programmers.co.kr/learn/courses/30/lessons/92343
후기: 백트래킹 문제였다.
Node라는 클래스를 별도로 선언했다.
tree는 Node[]로 이루어져 있다. tree의 index는 info의 index와 같다.
indexes는 현재 갈 수 있는 노드들, 즉 부분 트리의 자식들의 index를 가지고 있는 변수다.

다만 아래 풀이는 https://blog.encrypted.gg/1029 에 따르면 완벽한 풀이가 아니라고 한다.
백트래킹을 돌 때 겹치게 세는 부분이 있으므로 dfs/bfs 돌듯이 visited를 선언해서 지나간 길인지 확인했어야 한다.
"""

# 첫 번재 시도
# 백트래킹(recursive)의 39th ~ 46th를 잘못 짜줬기 때문에 무한반복한다.

answer = 0

class Node:
    def __init__(self, species):
        self.species = species # 양, 늑대 여부
        self.children = set()
        
    def AddChild(self, child_index):
        self.children.add(child_index)

def MakeTree(info, edges):
    tree = [Node(species) for species in info] # type: Class Node
    for parent, child in edges:
        tree[parent].AddChild(child)
    return tree

def BackTrack(tree, indexes, sheep, wolf):
    global answer
    if len(indexes) == 0: # 갈 수 있는 모든 길을 탐색
        return sheep
    if sheep != 0 and sheep <= wolf: # 불가능한 길
        return

    for index in indexes:
        if tree[index].species == 0: # 이렇게 하면 BackTrack return한 뒤에 다시 -= 1 해줘야 함
            sheep += 1
        else:
            wolf += 1
        indexes.remove(index)
        result = BackTrack(tree, indexes.union(tree[index].children), sheep, wolf)
        indexes.add(index) # set은 순서를 보장하지 않으므로 이렇게 하면 39th에서 for 문에 끝나지 않음
        if result:
            answer = max(answer, result)

    return sheep

def solution(info, edges):
    tree = MakeTree(info, edges)
    BackTrack(tree, {0}, 0, 0)
    return answer

  
# 두 번째 시도
# 통과

answer = 0

class Node:
    def __init__(self, species):
        self.species = species # 양, 늑대 여부
        self.children = set()
        
    def AddChild(self, child_index):
        self.children.add(child_index)

def MakeTree(info, edges):
    tree = [Node(species) for species in info] # type: Class Node
    for parent, child in edges:
        tree[parent].AddChild(child)
    return tree

def BackTrack(tree, indexes, sheep, wolf):
    global answer
    if len(indexes) == 0: # 갈 수 있는 모든 길을 탐색
        return sheep
    if sheep != 0 and sheep <= wolf: # 늑대가 양을 잡아먹음. 가면 안 되는 길
        return

    for index in indexes:
        s = {index} # int -> set
        if tree[index].species == 0:
            result = BackTrack(tree, indexes.difference(s).union(tree[index].children), sheep + 1, wolf)
        else: # tree[index].species == 1:
            result = BackTrack(tree, indexes.difference(s).union(tree[index].children), sheep, wolf + 1)
            
        if result:
            answer = max(answer, result)
    return sheep # 어쨌든 return 해주기 위해 추가

def solution(info, edges):
    global answer
    tree = MakeTree(info, edges)
    BackTrack(tree, {0}, 0, 0)
    return answer

