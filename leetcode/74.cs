/*
medium Search a 2D Matrix
url: https://leetcode.com/problems/search-a-2d-matrix/
후기: 사실 input이 작아서 brute force를 해도 풀 수 있었다. easy만큼 쉬웠던 것 같다.
*/

public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int row = matrix.Length;
        int column = matrix[0].Length;
        int i;
        for (i = 1; i < row; i++) {
            if (matrix[i][0] > target) break;
        }
        i--;
        
        for (int j = 0; j < column; j++) {
            if (matrix[i][j] == target) return true;
        }
        return false;
    }
}