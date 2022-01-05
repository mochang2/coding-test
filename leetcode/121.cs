/*
easy Best Time to Buy and Sell Stock
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
후기: 53번을 푼 이후에 푼 문제라 느낌이 왔다. 선형 탐색으로 풀 수 있는 방법을 고민하여 풀었다.
*/

public class Solution {
    public int MaxProfit(int[] prices) {
        // 선형탐색을 하면서 감소하는 구간은 index를 조정하여 패스
        // 가장 큰 이득을 보는 곳은 답만 기억
        int ans = 0;
        int pass_increasing = 0;
        for (int i = 1; i < prices.Length; i++) {
            int p1 = prices[i];
            int p2 = prices[pass_increasing];
            if (p1 - p2 > ans) ans = p1 - p2;
            if (p1 - p2 < 0) pass_increasing = i;
        }
        return ans;
    }
}