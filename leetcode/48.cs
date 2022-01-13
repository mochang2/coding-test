/*
medium Rotate Image
url: https://leetcode.com/problems/rotate-image/
후기: 그냥 개빡구현이었는데 너무 오래걸렸다.. 제자리에서 rotate하라고 해서 더 귀찮았던 거 같다.
*/

public class Solution {
    public void Rotate(int[][] matrix) {
        // y, x -> x, len - 1 - y
        
        int n = matrix.Length;
        int step = 0;
        while (step < (n / 2)) {
            List<int> temp = new List<int>();
            // temp <- up
            for (int i = step + 1; i < n - step; i++) {
                temp.Add(matrix[step][n - i]);
            }
            
            // up <- left
            for (int i = step + 1; i < n - step; i++) {
                matrix[step][n - i] = matrix[i - 1][step];
            }
            
            // left <- down
            for (int i = step + 1; i < n - step; i++) {
                matrix[i - 1][step] = matrix[n - 1 - step][i - 1];
            }
            
            // down <- right
            for (int i = step + 1; i < n - step; i++) {
                matrix[n - 1 - step][i - 1] = matrix[n - i][n - 1 - step];
            }
            
            // right <- temp
            int idx = 0;
            for (int i = step + 1; i < n - step; i++) {
                matrix[n - i][n - 1 - step] = temp[idx++];
            }
            
            step++;
        }
    }
}
