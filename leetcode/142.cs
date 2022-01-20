/*
medium Linked List Cycle II
url: https://leetcode.com/problems/linked-list-cycle-ii/
후기: 수학을 못해서 못 풀었다... 토끼와 거북이처럼 풀까 생각은 했는데 시작 위치를 어떻게 return하지? 하다가 막혔다.
결국 답을 봐버렸다.
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode DetectCycle(ListNode head) {
        // 토끼와 거북이란다. https://dev-note-97.tistory.com/277 거지같은 수학문제
        if (head == null) return null;
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (fast == slow) {
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }
        
        return null;
    }
}
