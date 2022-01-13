/*
medium Spiral Matrix II
url: https://leetcode.com/problems/spiral-matrix-ii/
후기: 빡구현. 2차원 배열을 어떻게 0으로 초기화하냐가 고민거리였다. 어렵진 않았다.
*/

public class Solution {
    public int[][] GenerateMatrix(int n) {
        int[][] matrix = new int [n][];
        for (int i = 0; i < n; i++) {
            matrix[i] = new int[n];
        }
        
        int num = 1;
        int direction = 1; // 0: up, 1: right, 2: down, 3: left
        int y = 0;
        int x = 0;
        while (num <= n * n) {
            matrix[y][x] = num++;
            switch(direction) {
                case 0:
                    if (y - 1 == -1 || matrix[y - 1][x] != 0) {
                        direction = 1;
                        x++;
                    }
                    else y--;
                    break;
                case 1:
                    if (x + 1 == n || matrix[y][x + 1] != 0) {
                        direction = 2;
                        y++;
                    }
                    else x++;
                    break;
                case 2:
                    if (y + 1 == n || matrix[y + 1][x] != 0) {
                        direction = 3;
                        x--;
                    }
                    else y++;
                    break;
                case 3:
                    if (x - 1 == -1 || matrix[y][x - 1] != 0) {
                        direction = 0;
                        y--;
                    }
                    else x--;
                    break;
                default:
                    break;
            }
        }
        
        return matrix;
    }
}
