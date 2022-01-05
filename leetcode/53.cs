/*
easy Maximum Subarray
url: https://leetcode.com/problems/maximum-subarray/
후기: array문제였다. 시간초과가 나서 답을 봤다. 파이썬으로 풀었어도 못 풀었을 것 같다. 신박했다.
*/

using System;

public class Solution {
    public int MaxSubArray(int[] nums) {
    	int currentSum = nums[0];
    	int maxSum = nums[0];
    	
    	for(int i = 1; i < nums.Length; i++) {
    		currentSum = Math.Max(nums[i]+currentSum, nums[i]);
    		maxSum = Math.Max(currentSum, maxSum);
    	}
    	
    	return maxSum;
    }
}