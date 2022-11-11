"""
20221111
골드2 개미굴
url: https://www.acmicpc.net/problem/14725
후기: trie라는 자료 구조를 몰랐는데 해당 내용을 알고 보니 골드2치고 꽤 쉬웠다.
trie는 사전에서 해당 단어가 존재하는지 빠르게 찾기 위한 자료 구조로, 일일이 비교하는 것보다 시간 복잡도는 낮지만 공간 복잡도는 높다.

풀이는 간단하다.
두 가지 클래스가 존재한다. 각각 Node와 Trie이다.
입력을 받은 대로 children을 추가한다. children은 data를 key, Node를 value로 가지는 dictionary 자료 구조이다.
모든 입력이 끝나면 children을 사전 순서대로 순회한다.
"""

import sys

input_ = sys.stdin.readline
FLOOR = '--'

class Node:
    def __init__(self, data = None):
        self.data = data
        self.children = dict()

    def hasChild(self, data):
        return data in self.children.keys()
        
    def addChild(self, data):
        if self.hasChild(data):
            return self.children[data]

        childNode = Node(data)
        self.children[data] = childNode

        return childNode
        
class Trie:
    def __init__(self):
        self.root = Node()

    def getRoot(self):
        return self.root

    def traverse(self, node, depth = -1):
        global FLOOR
        
        if node.data:
            print(FLOOR * depth + node.data)

        sorted_children_keys = sorted(node.children.keys())

        for key in sorted_children_keys:
            self.traverse(node.children[key], depth + 1)
        

def addNodesInTrie():
    global trie

    foods_count = int(input_().strip())

    for _ in range(foods_count):
        food_info = input_().strip().split()
        food_routes_count = int(food_info[0])
        foods = food_info[1:]

        node = trie.getRoot()

        for food in foods:
            node = node.addChild(food)

# initialize trie
trie = Trie()
addNodesInTrie()

# print
root = trie.getRoot()
trie.traverse(root)
