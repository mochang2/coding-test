/*
easy Reverse Linked List
url: https://leetcode.com/problems/reverse-linked-list/
후기: ListNode 3개를 선언한 후, 순차적으로 넘어가고, next를 바꾸는 법이 많이 헷갈렸다.
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        ListNode before = null;
        ListNode current = head;
        ListNode after = null;
        
        while (current != null) {
            after = current.next;
            current.next = before;
            before = current;
            current = after;
        }
        
        return before;
    }
}
