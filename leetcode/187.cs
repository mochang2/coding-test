/*
medium Repeated DNA Sequences
url: https://leetcode.com/problems/repeated-dna-sequences/
후기: 첫 예제에서 c가 6개인줄 모르고 계속 문제를 이해 못 하다가 어찌저찌 풀었다. 그래도 어려운 문제는 아니었다.
*/

public class Solution {
    public IList<string> FindRepeatedDnaSequences(string s) {
        List<string> answer = new List<string>();
        int n = s.Length;
        if (n <= 10) return answer;
        Dictionary<string, int> dic = new Dictionary<string, int>();
        for(int i = 0 ; i < n - 9; i++){
            string substr = s.Substring(i, 10);
            if(!dic.ContainsKey(substr)) dic.Add(substr, 1);
            else {
                dic[substr]++;
                if (dic[substr] == 2) answer.Add(substr);
            }
        }
        
        return answer;
    }
}
