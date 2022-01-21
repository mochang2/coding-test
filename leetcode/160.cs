/*
easy Intersection of Two Linked Lists
url: https://leetcode.com/problems/intersection-of-two-linked-lists/
후기: (오늘은 시간이 없어서)5분 안에 생각이 안 나서 그냥 답을 봐버렸다. 전날 풀었던 142번 토끼와 거북이보다 더 소름돋는 풀이였다.
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {
        // a -> headA가 아니라 headB로 옮기는 이유는 반드시 두 번째 iteration에서는 만나게 하기 위해
        // a -> headA로 해도 언젠가는 만나겠지만 시간은 훨씬 비효율적일 것임.
        ListNode a = headA;
        ListNode b = headB;
        
        while (a != b) {
            a = a == null ? headB : a.next;
            b = b == null ? headA : b.next;
        }
        
        return a;
    }
}
