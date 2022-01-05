/*
easy Merge Two Sorted Lists
url: https://leetcode.com/problems/merge-two-sorted-lists/
후기: 203이랑 거의 비슷하다. 이 또한 head를 따로 갖고 있어야 했다. 유튜브에 재귀를 이용한 정말 신박한 풀이가 있었다.
https://www.youtube.com/watch?v=ny1xYCeE2AM 이다.
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
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) return null;
        
        ListNode mergedList = new ListNode(-101);
        ListNode temp;
        temp = mergedList;
        
        while(list1 != null && list2 != null) {
            if (list1 == null || (list2 != null && list1.val >= list2.val)) {
                temp.next = list2;
                list2 = list2.next;
            }
            else {
                temp.next = list1;
                list1 = list1.next;
            }
            temp = temp.next;
        }
        
        temp.next = list1 == null ? list2 : list1;
        
        return mergedList.next;
    }
}