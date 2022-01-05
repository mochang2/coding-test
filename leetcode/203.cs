/*
easy Remove Linked List Elements
url: https://leetcode.com/problems/remove-linked-list-elements/
후기: 오랜만에 접한 linked list였다. doubly linked가 아니라서 head를 가리키는 변수 하나를 갖고 있어야 했다.
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
    public ListNode RemoveElements(ListNode head, int val) {
        if (head is null) return head;
        while (head.val == val) {
            // 앞 부분 잘라내기
            head = head.next;
            if (head is null) return head;
        }
        
        ListNode ans = head;
        ListNode prev = head;
        
        while (head is not null) {
            if (head.val != val) {
                prev = head;
                head = head.next;
            }
            else {
                head = head.next;
                prev.next = head;
            }
        }
        
        return ans;
    }
}