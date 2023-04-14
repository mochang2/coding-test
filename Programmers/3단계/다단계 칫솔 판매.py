"""
230414
그래프
url: https://school.programmers.co.kr/learn/courses/30/lessons/77486
후기: 확실히 카카오 3단계가 아니니까 쉽다.

Node는 2가지만 기억하면 된다. parent, profit. (아래 코드에는 name도 있는데 사실 사용하질 않았다) children도 기억하지 않아도 된다.
다만 이 문제를 풀면서 가장 고민이 된 게 profit을 구한 뒤 마지막에 이름 순서대로 해당 profit을 매칭시키는지였다.
root부터 pre-order / in-order 탐색을 고민해봤지만 반드시 그렇게 입력이 들어올거란 보장이 없다.
그래서 그냥 편히 dictionary에 key는 name, value에 Node를 집어넣었다.
겹치는 이름이 있을까봐 name/parent_name을 key로 할까 했지만, sellers라는 입력에 겹치는 이름에 대한 조건이 없어서 이러한 고민은 필요 없는 문제 같았다.

나머지는 profit을 절삭하면서 구한 뒤, root 노드이거나 / group_profit이 0인지 확인하며 root 노드까지 확인하면 된다.
"""

ROOT_NAME = '-'
UNIT_PRICE = 100

class Node:
    def __init__(self, name):
        self.name = name
        self.profit = 0
        self.parent = None
        
    def earn(self, profit):
        self.profit += profit
        
        return self.parent

def solution(enrolls, referrals, sellers, amounts):
    tree = makeTree(enrolls, referrals)
    
    for index in range(len(sellers)):
        seller = tree[sellers[index]]
        group_profit = amounts[index] * UNIT_PRICE
        
        while True:
            if seller.name == ROOT_NAME:
                tree[ROOT_NAME].earn(group_profit)
                break
                
            own_profit, group_profit = getProfit(group_profit)
            next_seller = seller.earn(own_profit)
            seller = tree[next_seller]
            
            if group_profit < 1:
                break
                
    profits = [tree[enroll].profit for enroll in enrolls]
    
    return profits
    
def makeTree(enrolls, referrals):
    tree = dict()
    
    root = Node(ROOT_NAME)
    tree[ROOT_NAME] = root
    
    for index in range(len(enrolls)):
        enroll, referral = enrolls[index], referrals[index]
        
        node = Node(enroll)
        node.parent = referral
        tree[enroll] = node
        
    return tree

def getProfit(amount):
    group_profit = int(amount * 0.1)
    
    if group_profit < 1:
        return amount, 0
    else:
        return amount - group_profit, group_profit
