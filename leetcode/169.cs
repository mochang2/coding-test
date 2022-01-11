/*
easy Majority Element
url: https://leetcode.com/problems/majority-element/
후기: Count랑 Length 헷갈리거나 길이가 1인 array에 대한 예외를 처리하지 않아서 많이 틀림.
*/

public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int, int> dic = new Dictionary<int, int>();
        foreach(int i in nums) {
            if (!dic.ContainsKey(i)) dic.Add(i, 1);
            else {
                dic[i]++;
                if (dic[i] > (nums.Length / 2)) return i;
            }
        }
        return nums[0];
    }
}
