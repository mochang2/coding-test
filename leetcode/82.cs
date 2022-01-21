/*
medium Remove Duplicates from Sorted List II
url: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
후기: 깨끗하지 않고 되게 논리적이지 못한 코드이지만 효율성은 좋다... 드럽고 애매한 풀이다.
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
    public ListNode DeleteDuplicates(ListNode head) {
        if (head == null) return null;
        else if (head.next == null) return head;
        
        ListNode curr = head;
        ListNode prev = head.val == head.next.val ? new ListNode(head.val, head) : new ListNode(head.val - 1, head);
        while (curr != null) {
            bool flag = false;
            while (curr.next != null && curr.val == curr.next.val) {
                flag = true;
                curr = curr.next;
            }
            if (flag) {
                curr = curr.next;
                if (curr == null) {
                    if (prev.next != head) prev.next = null;  // 끝(tail쪽)에 같은 node.val들이 이어져 있을 때
                    else return null;   // 모든 node의 val가 똑같을 때
                }
            }
            else {
                if (prev.next == head && prev.val == head.val)
                    head = curr;  // 앞(head쪽)에 같은 node.val들이 이어져 있을 때
                prev.next = curr;
                prev = curr;
                curr = curr.next;   
            }
        }
        
        return head;
    }
}
