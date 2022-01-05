/*
medium Valid Sudoku
url: https://leetcode.com/problems/valid-sudoku/
후기: 처음으로 주어진 class만이 아니라 나만의 class를 선언하여 문제를 풀었다.
풀이가 좀 지저분한 것 같지만 같은 3 by 3에 있는지 아닌지 판단하려면 어쩔 수 없는 문제 같다.
*/

public class Hash_Table_Pair {
    public HashSet<int> rows;
    public HashSet<int> columns;
    public Hash_Table_Pair() {
        this.rows = new HashSet<int>();
        this.columns = new HashSet<int>();
    }
}

public class Solution {
    public bool IsValidSudoku(char[][] board) {
        List<Hash_Table_Pair> li = new List<Hash_Table_Pair>();
        List<HashSet<int>> mini_board = new List<HashSet<int>>(); // 0 1 2 / 3 4 5 / 6 7 8
        for (int i = 0; i < 9; i++) {
            li.Add(new Hash_Table_Pair());
            mini_board.Add(new HashSet<int>());
        }
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                // check rows and columns
                char c = board[i][j];
                if (c == '.') continue;
                
                int num = (int)Char.GetNumericValue(c);
                if (li[i].rows.Contains(num) || li[j].columns.Contains(num)) {
                    return false;
                }
                else {
                    li[i].rows.Add(num);
                    li[j].columns.Add(num);
                }
                
                // check 3 by 3 board
                if (i < 3 && j < 3) { // zero grid
                    if (mini_board[0].Contains(num)) return false;
                    else mini_board[0].Add(num);
                }
                else if (i < 3 && j < 6) { // 1st grid
                    if (mini_board[1].Contains(num)) return false;
                    else mini_board[1].Add(num);
                }
                else if (i < 3 && j < 9) { // 2nd grid
                    if (mini_board[2].Contains(num)) return false;
                    else mini_board[2].Add(num);
                }
                else if (i < 6 && j < 3) { // 3rd grid
                    if (mini_board[3].Contains(num)) return false;
                    else mini_board[3].Add(num);
                }
                else if (i < 6 && j < 6) { // 4th grid
                    if (mini_board[4].Contains(num)) return false;
                    else mini_board[4].Add(num);
                }
                else if (i < 6 && j < 9) { // 5th grid
                    if (mini_board[5].Contains(num)) return false;
                    else mini_board[5].Add(num);
                }
                else if (i < 9 && j < 3) { // 6th grid
                    if (mini_board[6].Contains(num)) return false;
                    else mini_board[6].Add(num);
                }
                else if (i < 9 && j < 6) { // 7th grid
                    if (mini_board[7].Contains(num)) return false;
                    else mini_board[7].Add(num);
                }
                else { // (i < 9 && j < 9) 8th grid
                    if (mini_board[8].Contains(num)) return false;
                    else mini_board[8].Add(num);
                }
            }
        }
        
        return true;
    }
}