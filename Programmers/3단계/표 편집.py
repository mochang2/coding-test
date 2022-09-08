"""
220908
표 편집
url: https://school.programmers.co.kr/learn/courses/30/lessons/81303
후기: 완벽한 자료구조 문제였다.
일반적인 list를 사용하여 remove, insert를 구현하면 무조건 시간 초과가 나고, soft delete 형식으로 구현해도 무조건 시간 초과가 날 게 뻔했다.
그래서 처음에는 doubly linked list를 직접 구현했는데, D, U, C, Z 모든 연산이 O(n)이 걸려서 시간초과가 발생했다.

https://school.programmers.co.kr/questions/35448 여기에서
답을 본 결과 DoublyLinkedList class를 따로 구현하는 것이 아니라 Node[]를 이용했다.
각각의 Node는 list에서의 left index, right index와 삭제 여부를 데이터로 가지며 실제 delete 발생시 soft delete를 사용한다.
나머지 연산 작업은 DoublyLinkedList를 사용했을 때랑 비슷하다.
이렇게 하면 U, D는 O(n), C, Z는 O(1)의 시간 복잡도를 가진다.

https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python
dictionary를 사용한 예제도 있는데 훨씬 간단하다.
"""

## 오답. 시간 초과
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def getValue(self):
        return self.value

    def setPrev(self, node):
        self.prev = node

    def setNext(self, node):
        self.next = node

    def getPrev(self):
        return self.prev

    def getNext(self):
        return self.next

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        
        self.head.setPrev(None)
        self.head.setNext(self.tail)

        self.tail.setPrev(self.head)
        self.tail.setNext(None)

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def append(self, node):
        last_node = self.tail.prev
        last_node.setNext(node)
        node.setNext(self.tail)

        self.tail.setPrev(node)
        node.setPrev(last_node)

    def remove(self, node):
        prev_node = node.getPrev()
        next_node = node.getNext()

        prev_node.setNext(next_node)
        next_node.setPrev(prev_node)

    def insert(self, prev_node, node):
        next_node = prev_node.getNext()

        prev_node.setNext(node)
        node.setNext(next_node)

        next_node.setPrev(node)
        node.setPrev(prev_node)

def up(current, n):
    current_node = current
    
    for _ in range(n):
        current_node = current_node.getPrev()
        
    return current_node

def down(current, n):
    current_node = current
    
    for _ in range(n):
        current_node = current_node.getNext()
        
    return current_node

def remove(current, doubly_linked_list, garbage, index):
    doubly_linked_list.remove(current)
    garbage.append((index - 1, Node(current.getValue())))

    # 마지막 노드였다면 current_node는 tail
    return (current.getPrev(), index - 1) if current.getNext().getValue() == None else (current.getNext(), index)

def restore(current, doubly_linked_list, last_removed, index):
    last_removed_index, last_removed_node = last_removed
    pointer = current

    if index < last_removed_index:
        for _ in range(last_removed_index - index):
            pointer = pointer.getNext()
    elif index > last_removed_index:
        for _ in range(index - last_removed_index):
            pointer = pointer.getPrev()

    doubly_linked_list.insert(pointer, last_removed_node)

    return index + 1 if index > last_removed_index else index

def solution(n, k, cmds):
    stack = [] # 휴지통과 같은 개념

    doubly_linked_list = DoubleLinkedList()
    for i in range(n):
        doubly_linked_list.append(Node(i))
        
    current_node = doubly_linked_list.getHead()
    for _ in range(k + 1):
        current_node = current_node.getNext()
    index = k # "현재" doubly_linked_list에서 몇 번째 인덱스인지
        
    for cmd in cmds:
        try:
            command = cmd[0]
            if command == 'D':
                count = int(cmd.split(' ')[1])
                index += count
                current_node = down(current_node, count)

            elif command == 'U':
                count = int(cmd.split(' ')[1])
                index -= count
                current_node = up(current_node, count)

            elif command == 'C':
                current_node, index = remove(current_node, doubly_linked_list, stack, index)

            elif command == 'Z':
                index = restore(current_node, doubly_linked_list, stack.pop(), index)
                
        except Exception as e:
            pass

    values = ['X' for i in range(n)]
    pointer = doubly_linked_list.getHead()
    while pointer.getNext() and pointer.getNext().getValue() != None:
        pointer = pointer.getNext()
        values[pointer.getValue()] = 'O'

    return''.join(values)


## 정답

class Node :
    def __init__(self, left = None, right = None):
        self.exist = 'O'
        self.left = left
        self.right = right

def init(n):
    linked_list = [Node(i - 1, i + 1) for i in range(n)]
    linked_list[0].left = None
    linked_list[n - 1].right = None
    
    return linked_list

def solution(n, k, cmds):
    linked_list = init(n)
    pointer = k
    stack = []

    for cmd in cmds:
        command = cmd[0]

        if command == 'U':
            count = int(cmd.split(' ')[1])
            for _ in range(count):
                pointer = linked_list[pointer].left
                
        elif command == 'D':
            count = int(cmd.split(' ')[1])
            for _ in range(count):
                pointer = linked_list[pointer].right
                
        elif command == 'C':
            stack.append(pointer)
            linked_list[pointer].exist = 'X'
            
            prev, next_ = linked_list[pointer].left, linked_list[pointer].right
            
            if prev != None: # if prev:로 하면 prev == 0인 예외 처리 필요하므로 not None인 경우를 명시해야 한다
                linked_list[prev].right = next_
            if next_ != None:
                linked_list[next_].left = prev

            if not next_:
                pointer = prev
            else:
                pointer = next_
            
        elif command == 'Z':
            current = stack.pop()
            linked_list[current].exist = 'O'

            prev, next_ = linked_list[current].left, linked_list[current].right

            if prev != None:
                linked_list[prev].right = current
            if next_ != None:
                linked_list[next_].left = current

    answer = ''
    for node in linked_list:
        answer += node.exist

    return answer

  
