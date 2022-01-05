/*
easy Contains Duplicate
url: https://leetcode.com/problems/contains-duplicate/
후기: array DS 문제였다. hashset을 익힐 수 있었다.
*/

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> uniqueNums = new HashSet<int>();
        
        foreach(int num in nums) {
            if (uniqueNums.Contains(num)) return true;
            else uniqueNums.Add(num);
        }
        
        return false;
    }
}