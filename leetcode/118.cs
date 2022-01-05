/*
easy Paskal's Triangle
url: https://leetcode.com/problems/pascals-triangle/
후기: IList 타입이 interface라는 것을 알아도 추상화 개념이 부족해서 그런지 구현을 못 했다.
*/

public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        IList<IList<int>> Paskal_T = new List<IList<int>>();
        Paskal_T.Add(new List<int>() {1});
        if (numRows == 1) return Paskal_T;
        Paskal_T.Add(new List<int>() {1,1});
        if (numRows == 2) return Paskal_T;
        
        for (int i = 2; i < numRows; i++) {
            IList<int> layer = new List<int>();
            layer.Add(1);
            for (int j = 1; j < i; j++) {
                layer.Add(Paskal_T[i - 1][j - 1] + Paskal_T[i - 1][j]);
            }
            layer.Add(1);
            Paskal_T.Add(layer);
        }
        
        return Paskal_T;
    }
}