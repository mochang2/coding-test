/*
medium Design Linked List
url: https://leetcode.com/problems/design-linked-list/
후기: 예외처리할 게 너무 많았고, 테스트를 직접해보기가 귀찮아서 엄청 많이 틀렸다.
결국에 성공은 했지만 딱히 의미있는 문제는 아니었던 것 같다.
*/

public class MyLinkedList {
    
    private Node head;
    private int len;

    public MyLinkedList() {
        len = 0;
        head = null;
    }
    
    public int Get(int index) {
        if (len <= index) return -1;
        
        int i = 0;
        Node pointer = head;
        while (i != index) {
            pointer = pointer.next;
            i++;
        }
        return pointer.val;
    }
    
    public void AddAtHead(int val) {
        Node new_head = new Node();
        new_head.val = val;
        new_head.next = head;
        head = new_head;
        len++;
    }
    
    public void AddAtTail(int val) {
        if (head == null) {
            AddAtHead(val);
            return;
        }
        Node pointer = head;
        while (pointer.next != null) pointer = pointer.next;
        Node new_tail = new Node();
        new_tail.val = val;
        new_tail.next = null;
        pointer.next = new_tail;
        len++;
    }
    
    public void AddAtIndex(int index, int val) {
        if (len < index) return;
        if (index == 0) {
            AddAtHead(val);
            return;
        }
        
        int i = 0;
        Node pointer = head;
        while (i < index - 1) {
            pointer = pointer.next;
            i++;
        }
        Node new_node = new Node();
        new_node.val = val;
        new_node.next = pointer.next;
        pointer.next = new_node;
        len++;
    }
    
    public void DeleteAtIndex(int index) {
        if (len - 1 < index) return;
        if (index == 0) {
            Node temp = head;
            head = head.next;
            temp.next = null;
            len--;
            return;
        }
        
        int i = 0;
        Node pointer = head;
        while (i < index - 1) {
            pointer = pointer.next;
            i++;
        }
        pointer.next = pointer.next.next;
        
        len--;
    }
}

public class Node {
    public int val;
    public Node next;
    public Node() {
        this.val = 0;
        this.next = null;
    }
}
