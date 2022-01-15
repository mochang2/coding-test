/*
medium Product of Array Except Self
url: https://leetcode.com/problems/product-of-array-except-self/
후기: 돌았다고밖에 생각이 안 든다. 나눗셈에 너무 갇혀서 생각한 것 같다.
본인 index를 제외하고 곱하는 방법이면 dfs로 되나 계속 고민했었지만 도저히 O(n)이 되지 않을 것 같아서 답을 봤다.
*/

public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] answer = new int[n];
        answer[0] = 1;
        for (int i = 1; i < n; i++) {  // 왼쪽에서부터 쭉 곱해서 계산
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        
        int uncalculated = 1;
        for (int i = n - 1; i >= 0; i--) {// 오른쪽에서부터 계산 못 해준 부분 쭉 곱해서 계산
            answer[i] *= uncalculated;
            uncalculated *= nums[i];
        }
        
        return answer;
    }
}
