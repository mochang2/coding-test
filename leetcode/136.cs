/*
easy Single Number
url: https://leetcode.com/problems/single-number/
후기: 나는 이런 문제가 나오면 항상 Dictionary를 쓰고 나중에 한 번더 Dictionary를 확인해왔다.
혹시 다른 사람들은 어떻게 푸나 궁금했는데 정말 획기적이라서 놀라웠다.
*/

// 내 풀이
// O(n) + O(dic.Keys)
public class Solution {
    public int SingleNumber(int[] nums) {
        Dictionary<int, int> dic = new Dictionary<int, int>();
        
        foreach(int i in nums) {
            if (!dic.ContainsKey(i)) dic.Add(i, 1);
            else dic[i]++;
        }
        foreach(KeyValuePair<int, int> kvp in dic) {
            if (kvp.Value == 1) return kvp.Key;
        }
        
        return 0;
    }
}

// 다른 사람 풀이
public class Solution {
    public int SingleNumber(int[] nums) {
        var singleNumber = 0;
        foreach (var num in nums) {
            singleNumber ^= num;
        }
        return singleNumber;
    }
}
