/*
medium Partition Labels
url: https://leetcode.com/problems/partition-labels/
후기: 문제를 끝까지 이해를 못했어서 못 푼 문제이다. 처음에 dictionary에 넣어서 각각의 문자에 대해 (시작 index, 끝 index)를 저장해서
stack 같은 곳에서 지지고 볶고 할 예정이었다. 그런데 그럴 필요가 없는 간단한 문제였다.
*/

public class Solution {
    public IList<int> PartitionLabels(string s) {
        // alphabet, end index
        int n = s.Length;
        Dictionary<char, int> dic = new Dictionary<char, int>();
        for (int i = 0; i < n; i++) {
            if(!dic.ContainsKey(s[i])) dic.Add(s[i], i);
            else dic[s[i]] = i;
        }
        
        int index = 0;
        int start = 0;
        List<int> answer = new List<int>();
        while (index < n) {
            int end = dic[s[index]]; 
            while (end != index) {
                end = Math.Max(end, dic[s[index]]);
                index++;
            }
            answer.Add(end - start + 1);
            start = end + 1;
            index++;
        }
        
        return answer;
    }
}
