/*
medium Reorder List
url: https://leetcode.com/problems/reorder-list/
후기: 발상이 어렵진 않았다. 근데 이번 문제는 효율성을 원하는 문제였으면 틀렸을 것 같다.
https://leetcode.com/problems/reorder-list/discuss/44992/Java-solution-with-3-steps 다른 사람의 풀이다. 아마 훨씬 빠를 것 같다.
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
    public void ReorderList(ListNode head) {
        ListNode start = head;
        ListNode pointer = head.next;
        while(pointer != null && pointer.next != null) {
            while(pointer.next != null && pointer.next.next != null) pointer = pointer.next;
            ListNode tmp = pointer;
            pointer = pointer.next;
            tmp.next = null;
            
            pointer.next = start.next;
            start.next = pointer;
            start = start.next.next;
            pointer = start.next;
        }
    }
}
