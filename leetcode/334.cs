/*
mediumn Increasing Triplet Subsequence
url: https://leetcode.com/problems/increasing-triplet-subsequence/
후기: 너무 복잡하게 생각했던 것 같다. LIS로 풀려고 했으나 처음에는 시간 초과가 났다.
LIS를 N log N으로 풀 수 있는 방법이 있다고 하여 그 알고리즘을 보고 난 후에 풀 수 있었다.
LIS에 대해서는 https://rebro.kr/33 에서 설명을 잘해놨다.
*/

public class Solution {
    public int binarySearch(List<int> li, int num) { // li: vector, num: 이번에 넣을 수
        return num; 
        // 사실  정석적인 LIS는 lower bound를 찾아서 return해줘야 하지만 
        // 어차피 LIS의 최대 길이가 3이면 결과가 끝나니까 + 귀찮으니까 여기서는 구현 안 함.
    }
    
    public bool IncreasingTriplet(int[] nums) {
        // O(n^2) LIS => time exceeded
        int n = nums.Length;
        int[] dp = new int[n];
        dp[0] = 1;  // no need to initialize
        for (int i = 1; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j] && dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
                if (dp[i] == 3) return true;
            }
        }
        
        return false;
     
        
        // O(n log n) LIS
        List<int> li = new List<int>();
        li.Add(nums[0]);
        foreach(int num in new ArraySegment<int>(nums, 1, nums.Length - 1)) { // list slicing
            if (li[li.Count - 1] < num) li.Add(num);
            else {
              for (int i = 0; i < li.Count; i++) {
                  if (li[i] >= num) {
                      li[i] = num;
                      break;
                  }
              }  
            }  
            
            if (li.Count == 3) return true;
        }
        return false;
    }
}


// 다른 사람의 java 코드
/*
public boolean increasingTriplet(int[] nums) {
    // start with two largest values, as soon as we find a number bigger than both, while both have been updated, return true.
    int small = Integer.MAX_VALUE, big = Integer.MAX_VALUE;
    for (int n : nums) {
        if (n <= small) { small = n; } // update small if n is smaller than both
        else if (n <= big) { big = n; } // update big only if greater than small but smaller than big
        else return true; // return if you find a number bigger than both
    }
    return false;
}
*/
