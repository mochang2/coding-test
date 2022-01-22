/*
medium Swap Nodes in Pairs
url: https://leetcode.com/problems/swap-nodes-in-pairs/
후기: 생각보다 어렵진 않았다. 뭔가 깔끔하게 짰으면 while 문 뒤에 3줄은 더 필요 없었을 것 같다.
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
    public ListNode SwapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode first = head;
        ListNode second = head.next;
        head = head.next;
        
        while (second.next != null && second.next.next != null) {
            ListNode temp1 = second.next; // 1 -> 2 -> 3 -> 4 였으면 2 -> 1 -> 4로 되게끔 만들기
            second.next = first;
            first.next = temp1.next;
            first = temp1;
            second = temp1.next;
        }
        ListNode temp2 = second.next;
        second.next = first;
        first.next = temp2;
        
        return head;
    }
}
