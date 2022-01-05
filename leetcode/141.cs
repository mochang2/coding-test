/*
easy Linked List Cycle
url: https://leetcode.com/problems/linked-list-cycle/
후기: 뒤돌아갈 수 없는 자료 구조인 linked list.
지난 것들을 가지고 있으면 시간 복잡도가 낮아지겠지만, 공간 복잡도가 늘어날 것 같아 아래와 같이 풀었다.
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
    public bool HasCycle(ListNode head) {
        if (head == null) return false;
        for (int i = 0; i < 10001; i++) {
            // ListNode 자체를 저장하고 있으면 이렇게 많이 반복문을 돌릴 필요가 없음
            // 다만 문제에 val + next가 유니크한 것이 아니라고 했으니 내 풀이가 맞을듯
            if (head.next == null) return false;
            else head = head.next;
        }
        return true;
    }
}