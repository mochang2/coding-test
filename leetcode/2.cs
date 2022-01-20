/*
medium Add Two Numbers
url: https://leetcode.com/problems/add-two-numbers/
후기: 역순으로 된 linked list의 합을 구하는 것이다. 어렵진 않았다. 다만 해결하는데에만 목적을 두어 약간 효율적이진 않았던 거 같다.
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
    // 내 풀이
    // 180ms
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {        
        ListNode currNode = new();
        ListNode headNode = currNode;
        int carry = 0;
        
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                int res = l2.val + carry;
                if (res == 10) {
                    res = 0;
                    carry = 1;
                }
                else carry = 0;
                currNode.next = new ListNode(res, null);
                currNode = currNode.next;
                l2 = l2.next;
            }
            else if (l2 == null) {
                int res = l1.val + carry;
                if (res == 10) {
                    res = 0;
                    carry = 1;
                }
                else carry = 0;
                currNode.next = new ListNode(res, null);
                currNode = currNode.next;
                l1 = l1.next;
            }
            else {
                int res = l1.val + l2.val + carry;
                if (res >= 10) {
                    carry = 1;
                    res %= 10;
                }
                else carry = 0;
                currNode.next = new ListNode(res, null);
                currNode = currNode.next;
                l1 = l1.next;
                l2 = l2.next;
            }
        }
        if (carry != 0) currNode.next = new ListNode(1, null);
        
        return headNode.next;
    }
    
    // 따봉 많이 받은 사람 풀이
    // 153ms
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            int carry = 0;
            ListNode dummy = new ListNode(0);
            ListNode pre = dummy;

            while (l1 != null || l2 != null || carry == 1)
            {
                int sum = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;
                carry = sum < 10 ? 0 : 1;
                pre.next = new ListNode(sum % 10);
                pre = pre.next;

                if (l1 != null)
                {
                    l1 = l1.next;
                }

                if (l2 != null)
                {
                    l2 = l2.next;
                }
            }

            return dummy.next;
        }
}
