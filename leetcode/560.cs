/*
medium Subarray Sum Equals K
url: https://leetcode.com/problems/subarray-sum-equals-k/
후기: 완전 답을 배꼈다. for문마다 구하는 sum 간의 격차가 k랑 같은지 아닌지를 통해 구하는 문제였다.
이건 내가 풀었다고 할 수는 없다. 나중에 다시 봐야겠다.
*/

public class Solution {
    public int SubarraySum(int[] nums, int k) {
        Dictionary<int, int> dic = new Dictionary<int, int>();
        dic.Add(0, 1);
        int answer = 0;
        int sum = 0;
        
        foreach (int num in nums) {
            int prevVal = 0;
            
            sum += num;
            if (dic.TryGetValue(sum - k, out prevVal))  // answer update
                answer += prevVal; // 
            if (dic.TryGetValue(sum, out prevVal))  // dic update
                dic[sum] = prevVal + 1; 
            else 
                dic.Add(sum, 1);
        }
        
        return answer;
    }
}
