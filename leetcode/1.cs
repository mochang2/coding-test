/*
easy Two Sum
url: https://leetcode.com/problems/two-sum/
후기: 불변길이 array 문제였다. 완전탐색으로만 풀 수 있는 문제였다.
*/

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int n = nums.Length;
        int[] ans = new int[2];
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
            }
        }
        
        return ans;
    }
}