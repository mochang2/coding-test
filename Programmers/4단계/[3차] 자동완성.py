"""
221123
url: https://school.programmers.co.kr/learn/courses/30/lessons/17685
후기: 트라이 문제였다(4단계 문자열 문제여서 KMP 같은 건가 고민했었다).
얼마전 BOJ 14725 개미굴을 풀지 않았다면 도저히 못 풀었을 문제라고 생각한다.

요지는 간단하다.
사전에서 해당 단어가 있는지 효율적으로 확인하는 구조가 트라이이다.
다만 공간 복잡도는 약간 희생한다.

각 단어들을 순회하며 해당 문자열들이 이미 사전에 존재하는지 확인한다.
없으면 새로운 Node를 추가하고, 아니라면 기존 Node를 그대로 반환한다.

Node 클래스에서 관리하는 정보는 각 Node의 데이터(char 값), count, childrent이다.
여기서 count는 Trie를 traverse할 때 해당 char을 중복적으로 사용하는 단어가 있는지 여부를 표시하기 위해 사용한다.
"""

class Node:
    def __init__(self, data = None, count = 0):
        self.data = data
        self.count = count # 해당 data를 가지고 있는 단어의 개수
        self.children = dict() # 'data': Node

    def hasChild(self, data):
        return data in self.children.keys()

    def addChild(self, data):
        if self.hasChild(data):
            self.children[data].count += 1
            
            return self.children[data]

        childNode = Node(data, 1)
        self.children[data] = childNode

        return childNode

class Trie:
    def __init__(self):
        self.root = Node()

    def getRoot(self):
        return self.root

    def traverse(self, node):
        if node.count == 1: # 뒤 단어가 중복되는 단어가 없어서 추가적인 탐색이 필요 없음
            return node.count

        count = node.count
        
        for data in node.children.keys():
            count += self.traverse(node.children[data])

        return count

def solution(words):
    trie = Trie()
    
    for word in words:
        node = trie.getRoot()
        
        for char in word:
            node = node.addChild(char)

    root = trie.getRoot()
    
    return trie.traverse(root)
  
