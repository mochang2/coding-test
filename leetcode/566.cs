/*
easy Reshape the Matrix
url: https://leetcode.com/problems/reshape-the-matrix/
후기: 2차원 array(가변, 고정길이) 다루는게 파이썬이랑 달라서 약간 고민했다. 그래도 금방 익혀야겠다.
*/

public class Solution {
    public int[][] MatrixReshape(int[][] mat, int r, int c) {
        int m = mat.Length;
        int n = mat[0].Length;
        if (r * c != m * n) return mat;
        
        int[][] new_mat = new int[r][];
        for (int i = 0; i < r; i++) new_mat[i] = new int[c];
        
        int mat_r = 0;
        int mat_c = 0;
        int new_mat_r = 0;
        int new_mat_c = 0;
        for (int i = 0; i < r * c; i++) {
            if (mat_c == n) { 
                mat_c = 0;
                mat_r++;
            }
            if (new_mat_c == c) {
                new_mat_c = 0;
                new_mat_r++;
            }
            new_mat[new_mat_r][new_mat_c] = mat[mat_r][mat_c];
            mat_c++;
            new_mat_c++;
        }
        
        return new_mat;
    }
}