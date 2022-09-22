"""
220922
2019 KAKAO BLIND RECRUITMENT
url: https://school.programmers.co.kr/learn/courses/30/lessons/42892
후기: leetcode에서 문제를 풀었던 것이 생각나서 생각보다는 쉽게 풀었지만 시간을 오래 걸렸다.
그리고 recursion depth 때문에 6, 7번째 테스트 케이스에서 런타임 에러가 났다.
재귀할 때는 반드시 depth 확인하자.
"""

import sys

sys.setlimitrecursion(10 ** 5)

MIN_AXIS = -1
MAX_AXIS = 100001

class Node:
    def __init__(self, left_end, right_end, x, value = None):
        self.left_end = left_end
        self.right_end = right_end
        self.x = x
        self.value = value
        self.left = None
        self.right = None

def sortNodeInfo(nodes_info):
    sorted_info = []
    
    for index, node in enumerate(nodes_info):
        sorted_info.append([node[0], node[1], index + 1])
        
    return sorted(sorted_info, key=lambda x: (-x[1], x[0]))

def extractYAxis(node):
    return (node[0], node[2])

def groupByY(nodes_info):
    nodes_info_grouped_by_y = []
    left = 0
    right = 0
    
    while left < len(nodes_info):
        while right < len(nodes_info) and nodes_info[left][1] == nodes_info[right][1]:
            right += 1

        same_y_axis = list(map(extractYAxis, nodes_info[left:right]))
        nodes_info_grouped_by_y.append(same_y_axis)
        left = right
        
    return nodes_info_grouped_by_y

def makeTree(parent_node, nodes_info, child_index):
    if len(nodes_info) <= child_index:
        return
    
    left_end = parent_node.left_end
    right_end = parent_node.right_end
    parent_x = parent_node.x

    for info in nodes_info[child_index]:
        x, value = info

        if left_end < x < parent_x:
            node = Node(left_end, parent_x, x, value)
            parent_node.left = node
            makeTree(node, nodes_info, child_index + 1)
        elif parent_x < x < right_end:
            node = Node(parent_x, right_end, x, value)
            parent_node.right = node
            makeTree(node, nodes_info, child_index + 1)

def preOrder(node, result):
    result.append(node.value)
    if node.left:
        preOrder(node.left, result)
    if node.right:
        preOrder(node.right, result)

    return result
    
def postOrder(node, result):
    if node.left:
        postOrder(node.left, result)
    if node.right:
        postOrder(node.right, result)
    result.append(node.value)

    return result

def solution(nodes_info):
    sorted_nodes_info = sortNodeInfo(nodes_info)
    nodes_info_grouped_by_y = groupByY(sorted_nodes_info)
    
    head = Node(MIN_AXIS, MAX_AXIS, nodes_info_grouped_by_y[0][0][0], nodes_info_grouped_by_y[0][0][1])
    makeTree(head, nodes_info_grouped_by_y, 1)

    return [preOrder(head, []), postOrder(head, [])]
    
