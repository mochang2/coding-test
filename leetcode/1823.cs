/*
medium Find the Winner of the Circular Game
url: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
후기: 요세푸스 문제였다. 백준 1158에서 시간초과를 많이 겪으며 풀었던 경험이 없었으면 오래걸렸을 것 같다.
*/

public class Solution {
    public int FindTheWinner(int n, int k) {
        List<int> li = new List<int>();
        for (int i = 1; i <= n; i++) li.Add(i);
        int pointer = 0;
        while (n != 1) {
            pointer = (pointer + k - 1) % n;
            li.RemoveAt(pointer);
            n--;
        }
        
        return li[0];
    }
}
