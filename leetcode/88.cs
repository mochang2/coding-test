/*
easy Merged Sorted Array
url: https://leetcode.com/problems/merge-sorted-array/
후기: 문제 이해가 안돼서 시간이 좀 걸렸다. 사실 냅다 합치고 sort해도 풀 수 있는 문제지만 O(n)안에 풀려고 index를 썼다.
*/

using System;

public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int m_ptr = 0;
        int n_ptr = 0;
        
        while (n_ptr < n) {
            while (nums1[m_ptr] != 0) m_ptr++;
            nums1[m_ptr] = nums2[n_ptr];
            m_ptr++;
            n_ptr++;
        }
        Array.Sort(nums1);
    }
}