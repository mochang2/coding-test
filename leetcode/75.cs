/*
medium Sort Colors
url: https://leetcode.com/problems/sort-colors/
후기: 기본적인 int sort다. Array.Sort를 쓰지 말라고 해서 bubble sort로 구현했다.
당연히 효율성인 갖다 버린 코드다.
*/

public class Solution {
    public void Swap(ref int a, ref int b) {
        int temp = a;
        a = b;
        b = temp;
    }
    
    public void SortColors(int[] nums) {
        // 귀찮으니 버블 sort
        for (int i = 0; i < nums.Length - 1; i++) {
            for (int j = i + 1; j < nums.Length; j++) {
                if (nums[i] >= nums[j]) Swap(ref nums[i], ref nums[j]);
            }
        }
    }
}
