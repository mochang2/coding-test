/*
medium Search a 2D Matrix II
url: https://leetcode.com/problems/search-a-2d-matrix-ii/
후기: 사실 완전 탐색으로 돌아도 충분한 input 수였다. 충분히 잘 생각한 거라고 생각했지만 생각보다 빠르지 않았다.
그래서 가장 따봉 많이 받은 java를 보니까 똑똑한 풀이였다. 안 돌려봤지만 딱 봐도 훨씬 빠르다.
*/

// 내 풀이
public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        
        int i;
        int j;
        for (i = 0; i < m - 1; i++) {
            if (target >= matrix[i][0]) break;
        }
        int temp = i;
        for (; i < m; i++){   
            for (j = 0; j < n; j++) {
                if (target == matrix[i][j]) return true;
            }
        }
        
        for (j = 0; j < n - 1; j++) {
            if (target >= matrix[0][j]) break;
        }
        for (; j < n; j++){
            for (i = 0; i < temp; i++) {
                if (target == matrix[i][j]) return true;
            }
        }
            
        return false;
    }
}

// 
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null || matrix.length < 1 || matrix[0].length <1) {
            return false;
        }
        int col = matrix[0].length-1;
        int row = 0;
        while(col >= 0 && row <= matrix.length-1) {
            if(target == matrix[row][col]) {
                return true;
            } else if(target < matrix[row][col]) {
                col--;
            } else if(target > matrix[row][col]) {
                row++;
            }
        }
        return false;
    }
}
