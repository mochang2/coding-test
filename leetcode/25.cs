/*
hard Reverse Nodes in k-Group
url: https://leetcode.com/problems/reverse-nodes-in-k-group/
후기: 제정신이 아닌 상태에서 풀었다. 정말 드럽고 비효율적인 코드 같다...
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
    public ListNode ReverseKGroup(ListNode head, int k) {
        if (k == 1) return head;
        ListNode prevNewTail = new ListNode(0, head);
        ListNode subHead = head;
        ListNode subTail = head;
        bool flag = true;
        while (flag) {
            int n = 1;
            while (n <= k){ // subTail = subTail.next 할 때 null 처리 예외를 안 하면 에러가 나서 별 조건을 다 걸었다.
                if (subTail.next == null && n == k) {flag = false; subTail = null;}
                else if (subTail.next == null && n != k) return head;
                else subTail = subTail.next;
                n++;
            }
            
            // reverse
            ListNode prev = subHead;
            ListNode curr = subHead.next;
            while (curr != subTail) {
                ListNode tmp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = tmp;
            }
            if (prevNewTail.next == head) head = prev;
            prevNewTail.next = prev;
            prevNewTail = subHead;
            subHead.next = subTail;
            subHead = subHead.next;
        }
        return head;
    }
}
