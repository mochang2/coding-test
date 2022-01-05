/*
easy Intersection of Two Arrays II
url: https://leetcode.com/problems/intersection-of-two-arrays-ii/
후기: array 문제였다. Dictionary를 익힐 수 있었다.
*/

public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        Dictionary<int, int> count1 = new Dictionary<int, int>();
        Dictionary<int, int> count2 = new Dictionary<int, int>();
        foreach(int i in nums1) {
            if (!count1.ContainsKey(i)) count1.Add(i, 1);
            else count1[i]++;
        }
        foreach(int i in nums2) {
            if (!count2.ContainsKey(i)) count2.Add(i, 1);
            else count2[i]++;
        }
        
        List<int> answer = new List<int>();
        int min;
        foreach(KeyValuePair<int, int> each in count1) {
            int k = each.Key;
            if (count2.ContainsKey(k)) {
                min = Math.Min(each.Value, count2[k]);
                for (int i = 0; i < min; i++) answer.Add(k);
            }
        }
        return answer.ToArray();
    }
}