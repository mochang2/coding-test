/*
easy Remove Duplicates from Sorted List
url: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
후기: current.val과 after.val이 같은지 아닌지만 비교하면 됐다. 쉬웠다.
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
        if (head == null || head.next == null) return head;  // length == 0 || length == 1
        ListNode current = head;
        ListNode after = current.next;
        
        while (after != null) {
            if (current.val == after.val) {
                after = after.next;
                current.next = after;
            }
            else {
                current = after;
                after = after.next;
            }
        }
        
        return head;
    }
}
